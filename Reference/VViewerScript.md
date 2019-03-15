<<[top](VRec.html)
# VViewerScript
namespace:VRec/class/継承:MonoBehaviour

## **説明**
---
<br>
3Dコンテンツの再生を行う基本クラス、コンポーネント。
<br>

## **Public変数**
---
<br>

|変数名|詳細|
|:-----------|:------------|
|FileName|ファイル名|
|ViewStarted|再生が開始したかどうか。読み取り専用|
|ViewObjs|再生時に操作されるオブジェクト群のリスト。読み取り専用|
|Objs|読み込んだ全ての再生用のデータ。読み取り専用。詳しくは[VRecRecordData](VRecRecordData.html)を参照|
|IsLoop|ループするか否か|
|ViewingTime|再生が始まってから何秒経ったか。読み取り専用|
|ViewIndex|再生されているデータのIndex。読み取り専用|
|VoicePlayer|マイクで録音したAudioClipが再生されているAudioSource。読み取り専用|
|StartOnEditor|TrueにするとEditor上であれば再生を開始する。Update内でStartViewを実行する|
|EndOnEditor|TrueにするとEditor上であれば記録を終了する。Update内でEndViewを実行する|
|||
<br>

## **Protected変数**
<br>

|変数名|詳細|
|:-----------|:------------|
|_initialized|初期化が完了しているかどうか|
|_viewObjectList|再生するオブジェクトのリスト|
|||

## **Publicなデリゲート**
<br>

|変数名|詳細|
|:-----------|:------------|
|OtherObjectSetting|ObjTypeがOtherのときに呼ばれるDelegate。引数は[VRecEventData](VRecEventData.html)のみ|
|VRecHandler|ObjTypeがVRecのときに呼ばれるDelegate。引数はVRecEventDataのみ|
|ActivateHandler|ObjTypeがActivateSetのときに呼ばれるDelegate。引数はVRecEventDataのみ|
|AudioHandler|ObjTypeがAudioのときに呼ばれるDelegate。引数はVRecEventDataのみ|
|上記のDelegateに関しての詳細は[ObjectDataSettingHandler](ObjectDataSettingHandler.html)を参照||
|AvatarDataHandler|ObjTypeがAvatarのときに呼ばれるDelegate。引数はVRecEventDataと、対象のオブジェクト|
|ModelDataHandler|ObjTypeがModelのときに呼ばれるDelegate。引数はVRecEventDataと、対象のオブジェクト|
|StaticHandler|ObjTypeがStaticObjectのときに呼ばれるDelegate。引数はVRecEventDataと、対象のオブジェクト|
|上記のDelegateに関しての詳細は[VRecObjectSettingHandler](VRecObjectSettingHandler.html)を参照||
|OnStartHandler|再生が開始したときに呼ばれるDelegate。引数は、VViewerScriptを持つTransformと再生するファイル名|
|OnEndHandler|再生が終端まで到達したときに呼ばれるDelegate。引数は、VViewerScriptを持つTransformと再生するファイル名|
|上記のDelegateに関しての詳細は[VViewerHandler](VViewerHandler.html)を参照||
|||
<br>


## **Public関数**
<br>

|関数名|詳細|
|:-----------|:------------|
|Initialize|FileNameを元に初期化処理を行う|
|DataReset|初期化処理を行った内容を破棄する|
|StartView|再生を開始する|
|StopView|再生を停止する。停止後もStartViewを使えば再開される|
|||