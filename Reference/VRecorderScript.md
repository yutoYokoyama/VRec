<<[top](VRec.md)
# **VRecorderScript**
namespace:VRec/class/継承:MonoBehaviour

## **説明**
---
<br>
3Dコンテンツの記録を行う基本クラス、コンポーネント。
<br>

## **Public変数**
---
<br>

|変数名|詳細|
|:-----------|:------------|
|FileName|ファイル名|
|IsRecordStarted|記録が開始したかどうか。読み取り専用|
|IsRecordEnded|記録が終了したかどうか。読み取り専用|
|RecordObjs|記録を行うオブジェクトのリスト。読み取り専用|
|RecordingTime|記録が始まってから何秒経ったか。読み取り専用|
|StartOnEditor|TrueにするとEditor上であれば記録を開始する。Update内でStartRecordを実行する|
|EndOnEditor|TrueにするとEditor上であれば記録を終了する。Update内でEndRecordを実行する|
|IsVoiceRecording|マイクからの録音を行っているか。読み取り専用|
|AudioPositionId|再生時に、マイクの音声を追従させるオブジェクトのID。デフォルトでは動かない。読み取り専用|
|||
<br>

## **Protected変数**
---
<br>

|変数名|詳細|
|:-----------|:------------|
|_mike|マイクの録音を管理する。詳しくは[MikeRecorder](MikeRecorder.md)を参照|
|_objs|それまで記録したすべての記録データのリスト。詳しくは[VRecRecordData](VRecRecordData.md)を参照|
|||
<br>

## **Public関数**
---
<br>

|関数名|詳細|
|:--|:--|
|Initialize|フォルダの作成など、初期のイニシャライズを行う。StartRecordが呼ばれた際にも自動で実行される|
|AddRecordObj|指定したオブジェクトを、記録方法を設定して記録対象に加える。詳しい設定については[ObjType](ObjType.md)を参照|
|StartRecord|記録を開始する|
|EndRecord|記録を終了する|
|VoiceRecordSet|音声を記録する、あるいは記録しないと設定する|
|DeActivateRecordObj|登録されている記録対象を一時的に記録に反映させないようにする。オブジェクトを無効化すると自動的に呼ばれる|
|ActivateRecordObj|DeActivateRecordObjで記録に反映されなくなったものを再び反映するようにする。オブジェクトを有効化すると自動的に呼ばれる|
|RemoveRecordObj|対象を記録対象から取り除く。再び記録するにはAddRecordObjする必要がある|
|VRecObjectSet|VRecを重ね取りする際に使うと便利な関数。詳しくは[VRecCommand](VRecCommand)を参照|
|AddExRecord|利用者が独自のイベントを登録するための関数。詳しくは[ExRecord](ExRecord.md)を参照|
|||
<br>
