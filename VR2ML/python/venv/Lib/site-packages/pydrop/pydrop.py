import json
import requests
import csv
import os
import argparse
import getpass
import arrow
import datetime


# Get DO API key
try:
    key=os.path.join(os.path.expanduser('~'), 'dokey.csv')
    f=open(key)
    for row in csv.reader(f):
        keyval=str(row).strip("[']")
except Exception:
    print('Save your API key and try again')
    do_key_entry()

headers = {
'Content-Type': 'application/json',
'Authorization': 'Bearer '+str(keyval)
}

def do_key_entry():
    dohome=os.path.join(os.path.expanduser('~'), 'dokey.csv')
    password=getpass.getpass("Enter your Digital Ocean API Key")
    try:
        with open(dohome,'w') as completed:
            writer=csv.writer(completed,delimiter=',',lineterminator='\n')
            writer.writerow([password])
        print('API Key saved')
    except Exception as e:
        print(e)

# Get account info
def account_info():
    response = requests.get('https://api.digitalocean.com/v2/account', headers=headers)
    print('\n')
    if response.status_code == 200:
        acc= json.loads(response.content.decode('utf-8'))
    if acc is not None:
        for k, v in acc['account'].items():
            print('{0}:{1}'.format(k, v))

    else:
        print('[!] Request Failed')


# Get ssh keys
def sshread():
    response = requests.get('https://api.digitalocean.com/v2/account/keys', headers=headers)
    if response.status_code >= 500:
        print('[!] [{0}] Server Error'.format(response.status_code))
        return None
    elif response.status_code == 404:
        print('[!] [{0}] URL not found: [{1}]'.format(response.status_code,api_url))
        return None
    elif response.status_code == 401:
        print('[!] [{0}] Authentication Failed'.format(response.status_code))
        return None
    elif response.status_code == 400:
        print('[!] [{0}] Bad Request'.format(response.status_code))
        return None
    elif response.status_code >= 300:
        print('[!] [{0}] Unexpected Redirect'.format(response.status_code))
        return None
    elif response.status_code == 200:
        ssh_keys = json.loads(response.content.decode('utf-8'))
        if ssh_keys is not None:
            for key, details in enumerate(ssh_keys['ssh_keys']):
                print('\n')
                print('Key {}:'.format(key))
                for k, v in details.items():
                    print('  {0}:{1}'.format(k, v))
    else:
        print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(response.status_code, response.content))
    return None

# Add ssh key
def sshpost(name, filename):
    with open(filename, 'r') as f:
        ssh_key = f.readline()
    ssh_key = {'name': name, 'public_key': ssh_key}
    response = requests.post('https://api.digitalocean.com/v2/account/keys', headers=headers, json=ssh_key)
    if response.status_code >= 500:
        print('[!] [{0}] Server Error'.format(response.status_code))
        return None
    elif response.status_code == 404:
        print('[!] [{0}] URL not found: [{1}]'.format(response.status_code,api_url))
        return None
    elif response.status_code == 401:
        print('[!] [{0}] Authentication Failed'.format(response.status_code))
        return None
    elif response.status_code >= 400:
        print('[!] [{0}] Bad Request'.format(response.status_code))
        print(ssh_key )
        print(response.content )
        return None
    elif response.status_code >= 300:
        print('[!] [{0}] Unexpected redirect.'.format(response.status_code))
        return None
    elif response.status_code == 201:
        added_key = json.loads(response.content)
        print(added_key)
    else:
        print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(response.status_code, response.content))
        return None

# Delete ssh key: Use with Extremee Caution
def sshdelete(keyid):
    if keyid==None:
        sshread()
    else:
        response = requests.delete('https://api.digitalocean.com/v2/account/keys/'+str(keyid), headers=headers)
        json_data = json.loads(response)
        print(json_data)

# Get image snapshots
def snapshot():
    response = requests.get('https://api.digitalocean.com/v2/snapshots', headers=headers)
    json_data = json.loads(response.text)
    if not len(json_data['snapshots'])==0:
        for snaps in json_data['snapshots']:
            print('\n')
            print('{0}: {1}'.format('Snapshot Name', str(snaps['name'])))
            print('{0}: {1}'.format('Snapshot Created at', str(snaps['created_at'])))
            if len(snaps['tags'])>0:
                print('{0}: {1}'.format('Snapshot tags', str(snaps['tags'])))
            print('{0}: {1}'.format('Snapshot regions', str(snaps['regions'])))
            print('{0}: {1}'.format('Minimum disk size', str(snaps['min_disk_size'])))
            print('{0}: {1}'.format('Minimum disk size', str(snaps['size_gigabytes'])))
    else:
        print('\n'+'No shapshots found')


# Get all volumes in account
def volumeread():
    response = requests.get('https://api.digitalocean.com/v2/volumes', headers=headers)
    json_data = json.loads(response.text)
    if not len(json_data['volumes'])==0:
        for items in json_data['volumes']:
            print('Size in GB: '+str(items['size_gigabytes']))
            print('Volume ID: '+str(items['id']))
            print('Attached Droplet ID: '+str(items['droplet_ids'][0]))
            print('Volume created at: '+str(items['created_at']))
            print('Volume Filesystem Type: '+str(items['filesystem_type']))
    else:
        print('\n'+'No volumes found')


# Read all droplets
def dropletread(tag=None):
    if tag is not None:
        params = (
            ('tag_name', 'awesome'),
        )
        params = (
            ('tag_name', tag),
        )
        response = requests.get('https://api.digitalocean.com/v2/droplets', headers=headers,params=params)
        json_data = json.loads(response.text)
        for items in json_data['droplets']:
            print('Droplet name: '+str(items['name']))
            print('Droplet ID: '+str(items['id']))
            print('Status: '+str(items['status']))
            print('Created at: '+str(items['created_at']))
            print('IPv4 address: '+str(items['networks']['v4'][0]['ip_address']))
            print('No of CPUs: '+str(items['vcpus']))
            print('Memory: '+str(items['memory']))
            print('Disk Size GB: '+str(items['disk']))
            print('Image Used: '+str(items['image']['slug']))
            print('')
        print('Price Summary')
        price_monthly=0
        price_hourly=0
        for items in json_data['droplets']:
            price_monthly=price_monthly+float(items['size']['price_monthly'])
            price_hourly=price_hourly+float(items['size']['price_hourly'])
        print('Total Price Monthly: $'+str(price_monthly))
        print('Total Price Hourly: $'+str(price_hourly))
    elif tag is None:
        response = requests.get('https://api.digitalocean.com/v2/droplets', headers=headers)
        json_data = json.loads(response.text)
        for items in json_data['droplets']:
            print('Droplet name: '+str(items['name']))
            print('Droplet ID: '+str(items['id']))
            print('Status: '+str(items['status']))
            print('Created at: '+str(items['created_at']))
            print('IPv4 address: '+str(items['networks']['v4'][0]['ip_address']))
            print('No of CPUs: '+str(items['vcpus']))
            print('Memory: '+str(items['memory']))
            print('Disk Size GB: '+str(items['disk']))
            print('Image Used: '+str(items['image']['slug']))
            print('')
        print('Price Summary')
        price_monthly=0
        price_hourly=0
        price=[]
        for items in json_data['droplets']:
            price_monthly=price_monthly+float(items['size']['price_monthly'])
            price_hourly=price_hourly+float(items['size']['price_hourly'])
            diff=(datetime.datetime.now().date()-arrow.get(str(items['created_at']).split('T')[0],'YYYY-MM-DD').date())
            days,seconds=diff.days,diff.seconds
            hours=days*24+seconds/3600
            h=float(items['size']['price_hourly'])*hours
            price.append(h)
        print('Total Price Monthly: $'+str(price_monthly))
        print('Total Price Hourly: $'+str(price_hourly))
        print('')
        print('Based on active droplets')
        print('Estimated Price till date: $'+str(sum(price)))


# Reset droplet password using ID or Name
def dropreset(idn=None,name=None):
    if idn==None and name==None:
        response = requests.get('https://api.digitalocean.com/v2/droplets', headers=headers)
        json_data = json.loads(response.text)
        for items in json_data['droplets']:
            print('Droplet Name '+str(items['name'])+' has ID '+str(items['id']))
    elif idn==None and name is not None:
        l=[]
        response = requests.get('https://api.digitalocean.com/v2/droplets', headers=headers)
        json_data = json.loads(response.text)
        for items in json_data['droplets']:
            if name==str(items['name']):
                print('Droplet name matched to ID '+str(items['id']))
                print('Now Deleting '+str(items['name']))
                data = '{"type":"password_reset"}'
                response = requests.post('https://api.digitalocean.com/v2/droplets/'+str(items['id']), headers=headers,data=data)
                if response.status_code==201:
                    print('Password reset started')
                    print('')
                else:
                    print('Password Reset failed with Status Code',str(response.status_code))
                    print('')
            else:
                l.append(str(items['name']))
        print('Unmatched Droplets '+str(len(l)))
    elif name==None and idn is not None:
        l=[]
        response = requests.get('https://api.digitalocean.com/v2/droplets', headers=headers)
        json_data = json.loads(response.text)
        for items in json_data['droplets']:
            if idn==str(items['id']):
                print('Droplet ID matched to '+str(items['name']))
                print('Now resetting password for '+str(items['id']))
                data = '{"type":"password_reset"}'
                response = requests.post('https://api.digitalocean.com/v2/droplets/'+str(items['id']), headers=headers,data=data)
                if response.status_code==201:
                    print('Password reset started')
                    print('')
                else:
                    print('Password Reset failed with Status Code',str(response.status_code))
                    print('')
            else:
                l.append(str(items['id']))
        print('Unmatched Droplets '+str(len(l)))


# Use with Extreme Caution: Delete Droplet using ID or Name
def dropdelete(idn=None,name=None):
    if idn==None and name==None:
        response = requests.get('https://api.digitalocean.com/v2/droplets', headers=headers)
        json_data = json.loads(response.text)
        for items in json_data['droplets']:
            print('Droplet Name '+str(items['name'])+' has ID '+str(items['id']))
    elif idn==None and name is not None:
        l=[]
        response = requests.get('https://api.digitalocean.com/v2/droplets', headers=headers)
        json_data = json.loads(response.text)
        for items in json_data['droplets']:
            if name==str(items['name']):
                print('Droplet name matched to ID '+str(items['id']))
                print('Now Deleting '+str(items['name']))
                response = requests.delete('https://api.digitalocean.com/v2/droplets/'+str(items['id']), headers=headers)
                if response.status_code==204:
                    print('Delete Succeeded ')
                    print('')
                else:
                    print('Delete failed with Status Code',str(response.status_code))
                    print('')
            else:
                l.append(str(items['name']))
        print('Unmatched Droplets '+str(len(l)))
    elif name==None and idn is not None:
        l=[]
        response = requests.get('https://api.digitalocean.com/v2/droplets', headers=headers)
        json_data = json.loads(response.text)
        for items in json_data['droplets']:
            if idn==str(items['id']):
                print('Droplet ID matched to '+str(items['name']))
                print('Now Deleting '+str(items['id']))
                response = requests.delete('https://api.digitalocean.com/v2/droplets/'+str(items['id']), headers=headers)
                if response.status_code==204:
                    print('Delete Succeeded ')
                    print('')
                else:
                    print('Delete failed with Status Code',str(response.status_code))
                    print('')
            else:
                l.append(str(items['id']))
        print('Unmatched Droplets '+str(len(l)))


#Common droplet actions
def doaction(action=None,rname=None,name=None,idn=None):
    if action is None:
        response = requests.get('https://api.digitalocean.com/v2/droplets', headers=headers)
        json_data = json.loads(response.text)
        for items in json_data['droplets']:
            print('Droplet Name '+str(items['name'])+' has ID '+str(items['id']))
    elif action is not None and idn is not None:
        data = {"type":""}
        data["type"]=action
        if action==shutdown:
            url='https://api.digitalocean.com/v2/droplets/'+str(idn)+'/actions'
        if action==power_off:
            url='https://api.digitalocean.com/v2/droplets/'+str(idn)+'/actions'
        if action==power_on:
            url='https://api.digitalocean.com/v2/droplets/'+str(idn)+'/actions'
        if action==rename and rname is not None:
            url='https://api.digitalocean.com/v2/droplets/'+str(idn)+'/actions'
            data = {"type":"","name":""}
            data["type"]=action
            data["name"]=rname
        response = requests.post(url, headers=headers, data=json.dumps(data))
        #print(response.status_code)
        if response.status_code==201:
            json_data = json.loads(response.text)
            print('Action ID '+str(json_data['action']['id']))
            print('Status '+str(json_data['action']['status']))
            print('Action Type '+str(json_data['action']['type']))
        else:
            print('Failed with error code '+str(response.status_code))
    elif action is not None and name is not None:
        response = requests.get('https://api.digitalocean.com/v2/droplets', headers=headers)
        json_data = json.loads(response.text)
        for items in json_data['droplets']:
            if name==str(items['name']):
                idn=str(items['id'])
                data = {"type":""}
                data["type"]=str(action)
                if action=="shutdown":
                    url='https://api.digitalocean.com/v2/droplets/'+str(idn)+'/actions'
                elif action=="power_off":
                    url='https://api.digitalocean.com/v2/droplets/'+str(idn)+'/actions'
                elif action=="power_on":
                    url='https://api.digitalocean.com/v2/droplets/'+str(idn)+'/actions'
                elif action=="rename" and rname is not None:
                    url='https://api.digitalocean.com/v2/droplets/'+str(idn)+'/actions'
                    data = {"type":"","name":""}
                    data["type"]=str(action)
                    data["name"]=rname
                else:
                    print('Unkown action type '+str(action))
                    sys.exit()
                response = requests.post(url, headers=headers, data=json.dumps(data))
                #print(response.status_code)
                if response.status_code==201:
                    json_data = json.loads(response.text)
                    print('Action ID '+str(json_data['action']['id']))
                    print('Status '+str(json_data['action']['status']))
                    print('Action Type '+str(json_data['action']['type']))
                else:
                    print('Failed with error code '+str(response.status_code))

#doaction(action=None,rname=None,name=None,idn=None)
#dropdelete(idn=None,name=None)
#sshpost(name, filename)
#dropletread()
#dropletread(tag="dev")
#sshread()
#account_info()
#sshdelete(keyid=None)
#snapshot()
#dropresetidn=None,name=None)

def do_key_from_parser(args):
    do_key_entry(key=args.key)

def sshread_from_parser(args):
    sshread()

def sshpost_from_parser(args):
    sshpost(name=args.name,filename=args.keyfile)

def sshdelete_from_parser(args):
    sshdelete(keyid=args.keyid)

def accinfo_from_parser(args):
    account_info()

def dropinfo_from_parser(args):
    dropletread(tag=args.tag)

def volinfo_from_parser(args):
    volumeread()

def snapinfo_from_parser(args):
    snapshot()

def dropdelete_from_parser(args):
    dropdelete(idn=args.id,name=args.name)

def dropreset_from_parser(args):
    dropreset(idn=args.id,name=args.name)

def dropaction_from_parser(args):
    doaction(idn=args.id,name=args.name,action=args.action,rname=args.rename)

def main(args=None):
    parser = argparse.ArgumentParser(description='Digital Ocean API Python CLI')

    subparsers = parser.add_subparsers()
    parser_do_key = subparsers.add_parser('dokey', help='Enter your Digital Ocean API Key')
    optional_named = parser_do_key.add_argument_group('Optional named arguments')
    optional_named.add_argument('--key', help='Your Digital Ocean API Key')
    parser_do_key.set_defaults(func=do_key_from_parser)

    parser_accinfo = subparsers.add_parser('accinfo', help='Prints your account info')
    parser_accinfo.set_defaults(func=accinfo_from_parser)

    parser_dropletread = subparsers.add_parser('dropinfo', help='Prints information about all your droplets')
    optional_named = parser_dropletread.add_argument_group('Optional named arguments')
    optional_named.add_argument('--tag', help='Use a tag to refine your search',default=None)
    parser_dropletread.set_defaults(func=dropinfo_from_parser)

    parser_volinfo = subparsers.add_parser('volinfo', help='Prints information about all your volumes')
    parser_volinfo.set_defaults(func=volinfo_from_parser)

    parser_snapinfo = subparsers.add_parser('snapinfo', help='Prints information about all your snapshots')
    parser_snapinfo.set_defaults(func=snapinfo_from_parser)

    parser_sshread = subparsers.add_parser('sshread', help='Prints information about your ssh keys')
    parser_sshread.set_defaults(func=sshread_from_parser)

    parser_sshpost = subparsers.add_parser('sshpost', help='Adds new ssh keys to account')
    required_named = parser_sshpost.add_argument_group('Required named arguments.')
    required_named.add_argument('--name', help='name for ssh key', required=True)
    required_named.add_argument('--keyfile', help='file with ssh key', required=True)
    parser_sshpost.set_defaults(func=sshpost_from_parser)

    parser_sshdelete = subparsers.add_parser('sshdelete', help='Deletes a ssh keys from account')
    optional_named = parser_sshdelete.add_argument_group('Optional named arguments')
    optional_named.add_argument('--keyid', help='ssh key id',default=None)
    parser_sshdelete.set_defaults(func=sshdelete_from_parser)

    parser_doaction = subparsers.add_parser('dropaction', help='Performs an action on your droplets')
    optional_named = parser_doaction.add_argument_group('Optional named arguments')
    optional_named.add_argument('--id', help='Use an image ID to perform action',default=None)
    optional_named.add_argument('--name', help='Use an image name to perform action',default=None)
    optional_named.add_argument('--action', help='Action type |shutdown="graceful shutdown"|power_off="hard shutdown"|power_on="power on"|rename="rename',default=None)
    optional_named.add_argument('--rename', help='Incase you are renaming droplet you can provide new name',default=None)
    parser_doaction.set_defaults(func=dropaction_from_parser)

    parser_dropdelete = subparsers.add_parser('dropdelete', help='Permanently deletes the droplet ')
    optional_named = parser_dropdelete.add_argument_group('Optional named arguments')
    optional_named.add_argument('--id', help='Use an image ID to delete droplet',default=None)
    optional_named.add_argument('--name', help='Use an image name to delete droplet',default=None)
    parser_dropdelete.set_defaults(func=dropdelete_from_parser)

    parser_dropreset = subparsers.add_parser('dropreset', help='Resets password for the droplet ')
    optional_named = parser_dropreset.add_argument_group('Optional named arguments')
    optional_named.add_argument('--id', help='Use an image ID to reset password on droplet',default=None)
    optional_named.add_argument('--name', help='Use an image name to reset password on droplet',default=None)
    parser_dropreset.set_defaults(func=dropreset_from_parser)

    args = parser.parse_args()

    #ee.Initialize()
    args.func(args)

if __name__ == '__main__':
    main()
