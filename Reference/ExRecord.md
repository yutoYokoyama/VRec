<<[top](VRec.md)
# **ExRecord**

## **説明**
---
<br>

VRecでは3Dモデルやアバターの動きを記録しますが、それ以外の定形でないもの、例えばテクスチャの変更やMeshRendererの値の変更などにはその都度、自身でイベントを登録する必要があります。<br>
この項では、記録時にイベントをどう追加するか、再生時に追加したイベントをどう再現するかを解説します。

<br>

## **記録時の操作**
---

記録時にはVRecorderScript.AddExRecordを使ってイベントを追加できます。<br>

AddExRecordは、StartRecordが実行される前であれば、時刻0、つまり再生開始時に、実行された後であればその時の時刻に登録されます。<br>

もし、あなたがそのイベントを毎フレームごとに発生させたい場合は、AddExRecordも毎フレームごとに実行される必要があります。<br>

AddExRecordは、string,float配列,string配列の3つを引数とし持つメソッドです。<br>
引数として与えた3つの要素が再生時に利用できます。<br>
以下にそのサンプルコードを記します。<br>
```cs:
using UnityEngine;
using VRec;

public class MyVRec:VRecorderScript
{

    private void Start
    {
        StartRecord("FileName");
    }

    public bool EventHappen;
    public void Update()
    {
        base.Update();
        if(EventHappen)
        {
            var label = "EventName";
            var floatData = new float[3]{0,1,2};
            var strData = new string{"a","b","c"};
            AddExRecord(label,floatData,strData);
            EventHappen =false;
        }
    }
}

```
labelには、イベントの識別子を入れるべきでしょう。例えば、「炎のパーティクルを発生させる」イベントのときは"FireLaunch",SkinnedMeshRendererのBlendShapesの値を変えるのであれば"ChangeBlendShape"のようにです。

float配列には、例えばイベントを発生させたい座標やMeshRendererの値,あるいは対象としているRecordObjectのIdなどを登録すべきでしょう

string配列には、数値以外の必要なデータを設定する必要があるでしょう。例えば、読み込むテクスチャのパスなどです。列挙型や真偽値の場合、float配列よりもstring配列を用いた方がデータ量は少なくなるでしょう。

## **再生時の操作**
---

再生時には、delegateであるVViewer.[OtherObjectSetting](ObjectDataSettingHandler.md)を用いてイベントの再現を行います。<br>

OtherObjectSettingは[VRecEventData](VRecEventData.md)を引数とし、これには記録時に登録したLabel、float配列、string配列が含まれています。<br>

これらの値を利用し、イベントの再現を行います。<br>

以下にそのサンプルコードを示します。今回は前節で示した記録時のサンプルコードで記録したものと仮定しておきましょう。

```cs:
using UnityEngine;
using VRec;

public class MyVViewer:VViewerScript
{
    private void Start()
    {
        OtherObjectSetting += MyEventHandler
    }

    private void MyEventHandler(VRecEventData data)
    {
        if(data.Label=="EventName"){
            Debug.Log(data.Label);//"EventName"と出ます
            foreach(var f in data.FloatValues){
                Debug.Log(f);//0,1,2と出ます
            }
            foreach(var str in data.StrData)
            {
                Debug.Log(str);//a,b,cと出ます
            }
        }
    }
}
```

複数種類のイベントが存在する場合には、Labelによってその判別を行うべきでしょう。つまり、サンプルコードのようにif文を用いて区別するか、switch(data.Label)としてcaseごとに処理するかです。

## **Tips**
---
ExRecordの機能は柔軟性があり、どのような場合でも使えると言えますが、その分冗長です。あまり多用をおススメしません。<br>
よく使われる機能、例えばSkinnedMeshRendererの値の記録などは拡張機能として実装予定ですが、それ以外のものに関しても順次対応していく予定です。
<br><br>
AddExRecordする部分は以下のように書くと実装が簡単です。

```
//FunctionA(string str)の実行を記録するとき:
    AddExRecord(label,new float[0]{},new string[0]{});
    FunctionA(label)
```
```
//FunctionAの実行を再生するとき:
void Handler(VRecEventData data){
    if(data.Label == "label")
        FunctionA(label)
}
```
つまり、そのイベントの実行そのものを1つのメソッドにしておき、そのメソッドの実行前にAddExRecordを行い、再生時にはそのメソッドを実行する形にしておくのがよいでしょう。

また、ここであげたことはその他の[ObjectDataSettingHandler](ObjectDataSettingHandler.md)や[VRecObjectSettingHandler](VRecObjectSettingHandler.md)などにも適応できます