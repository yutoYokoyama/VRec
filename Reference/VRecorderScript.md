<<[top](VRec.md)
# **VRecorderScript**
namespace:VRec/class/super class:MonoBehaviour

## **Introduction**
---
<br>
Base component for recording 3D content.
<br>

## **Public Variable**
---
<br>

|variable names|details|
|:-----------|:------------|
|FileName|file name|
|IsRecordStarted|Whether the recording has started. Read only|
|IsRecordEnded|Whether the recording has stopped. Read only|
|RecordObjs|List of objects to record. Read only|
|RecordingTime|How many seconds have passed since the recording began. Read only|
|StartOnEditor|If set to True, recording starts on the Editor. Execute StartRecord in Update|
|EndOnEditor|If set to True, recording ends on the Editor. Execute EndRecord in Update|
|IsVoiceRecording|Whether the mike recording is running. Read Only|
|||
<br>

## **Protected Variable**
---
<br>

|variable names|details|
|:-----------|:------------|
|_mike|Manage mike recording。[MikeRecorder](MikeRecorder.md) for details|
|_objs|List of all recorded data recorded. [VRecRecordData](VRecRecordData.md) for details|
|||
<br>

## **Public Function**
---
<br>

|function names|details|
|:--|:--|
|Initialize|Initialize, such as creating a folder. Automatically executed when StartRecord is called|
|AddRecordObj|Add the specified object to the recording target.(it's need object type. [ObjType](ObjType.md) for details)|
|StartRecord|Start Record|
|EndRecord|End Record(not "stop". cannot restart)|
|VoiceRecordSet|Set mike record on/off|
|DeActivateRecordObj|Temporarily exclude specified objects from recording.it's called automatically when the object is invalidated|
|ActivateRecordObj|Make deactivated object recording target.it's called automatically when the object is activated|
|RemoveRecordObj|remove the object from recording target|
|AddExRecord|Function for the user to register their own event. [ExRecord](ExRecord.md) for details|
|||
<br>
