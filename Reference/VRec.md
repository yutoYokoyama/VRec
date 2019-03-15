<<[top](./index.html)
# **VRec**

## **説明**
---
<br>
VRecは3Dコンテンツの記録・再生を行うライブラリです。<br>

単純なアバターの動きの記録、再生を行うだけであれば、[VRecorderScript](VRecorderScript.html)と[VViewerScript](VViewerScript.html)のみを使えば実現できます。

それ以上の、例えばテクスチャの変更やパーティクルの反映などの操作を記録する場合は、それ以外の、特に[ExRecord](ExRecord.html)のドキュメントを参照してください

「.vrc」フォーマットのバイト形式などは[VRecRecordData](VRecRecordData.html)を参照してください

わかりにくい場合は、twitter@[yuto_onizakura](https://twitter.com/yuto_onizakura)にて、リプライやDMでご質問ください。改善を行います

各機能については以下を参照してください
<br>

## **主な機能・コンポーネント**
---
<br>

- [VRecorderScript](VRecorderScript.html) 記録用コンポーネント
    - [MikeRecorder](MikeRecorder.html)
        - マイクからの録音に関わる機能
    - [VRecCommand](VRecCommand)
        - VRecを重ね撮りする際に使うと便利なコマンド
- [VViewerScript](VViewerScript.html)       再生用コンポーネント
    - [ObjectDataSettingHandler](ObjectDataSettingHandler.html)
    - [VRecObjectSettingHandler](VRecObjectSettingHandler.html)
        - 上記2つとも、特定のObjectTypeの際に呼ばれるDelegate
    - [VViewerHandler](VViewerHandler.html)
        - VViewerが開始、あるいは終了した際に呼ばれるDelegate
- [ObjType](ObjType.html) VRecが記録する際の種別
- [ExRecord](ExRecord.html) 独自の操作、イベントを登録・再生したい時に参照してください
- [VRecFilePathHelper](VRecFilePathHelper.html)　ファイルパスに関するヘルパー
- [VRecRecordData](VRecRecordData.html) VRec内で記録・再生されているデータ群に関する詳細、あるいは「.vrc」フォーマットのバイト形式などはこちらを参照してください
<br>


## **連絡先**
---
名古屋大学<br>
情報学研究科<br>
知能システム学専攻<br>
長尾研究室所属<br>
横山勇斗<br>
yokoyama@nagao.nuie.nagoya-u.ac.jp<br>
Twitter: [@yuto_onizakura](https://twitter.com/yuto_onizakura)<br>

<br>