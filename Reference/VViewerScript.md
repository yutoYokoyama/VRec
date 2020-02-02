<<[top](VRec.md)
# VViewerScript
namespace:VRec/class/super class:MonoBehaviour

## **Introduction**
---
<br>
Base component for replaying 3D content.
<br>

## **Public Variazble**
---
<br>

|variable names|details|
|:-----------|:------------|
|FileName|file name|
|ViewStarted|Whether replaying started.Read Only|
|ViewObjs|List of replaying objects .Read Only|
|Objs|All read data for playback. Read Only. [VRecRecordData](VRecRecordData.md) for details|
|IsLoop|loop function is on/off|
|ViewingTime|How many seconds have passed since started. Read Only|
|ViewIndex|Index of the data being played. Read Only|
|VoicePlayer|AudioSource where the AudioClip recorded by the microphone is playing. Read Only|
|StartOnEditor|If set to True, replaying starts on the Editor. Execute StartView in Update.|
|EndOnEditor|If set to True, replaying stops on the Editor. Execute StopView in Update|
|||
<br>

## **Protected Variable**
<br>

|variable names|details|
|:-----------|:------------|
|_initialized|initialization finished or not|
|_viewObjectList|replaying object list|
|||

## **Public Delegate**
<br>

|variable names|details|
|:-----------|:------------|
|OtherObjectSetting|Delegate called when [ObjType](ObjType.md) is Other|
|ActivateHandler|Delegate called when [ObjType](ObjType.md) is ActiveSet|
|AudioHandler|Delegate called when [ObjType](ObjType.md) is AudioSetting|
|The above three delegate's infomation is [ObjectDataSettingHandler](ObjectDataSettingHandler.md)||
|AvatarDataHandler|Delegate called when [ObjType](ObjType.md) is Avatar|
|ModelDataHandler|Delegate called when [ObjType](ObjType.md) is 3DModel|
|StaticHandler|Delegate called when [ObjType](ObjType.md) is StaticObject|
|The above three delegate's infomation is [VRecObjectSettingHandler](VRecObjectSettingHandler.md)||
|OnStartHandler|Delegate called when replaying started|
|OnEndHandler|Delegatet called when replaying end(not "stop". when reached end of recorded data)|
|The above two delegate's infomation is[VViewerHandler](VViewerHandler.md)||
|||
<br>


## **Public Function**
<br>

|function names|details|
|:-----------|:------------|
|Initialize|initialize|
|DataReset|remove initialized data|
|StartView|start replaying|
|StopView|stop replaying(not "end". it can restart by StartView)|
|||