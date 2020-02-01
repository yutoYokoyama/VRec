<<[top](VRec_ja.md)
# **ObjectDataSettingHandler**
class VViewerScript/public delegate

## **説明**
---
<br>

[VViewerScript](VViewerScript_ja.md)内に存在するdelegate型<br>
引数は[VRecEventData](VRecEventData_ja.md)型のみ。VViewerScript内にはOtherObjectSetting、VRecHandler、ActivateHandler、AudioHandlerの4つが準備されています

VViewerScript内では毎フレームごとに記録された内容を実行・反映します。それらの内容はVRecEventData内のTypeによって呼ばれるHandlerが変わり、その対応表は以下の通りです。

|Type|呼ばれるDelegate|
|:--|:--|
|Other|OtherObjectSetting|
|VRec|VRecHandler|
|ActiveSet|ActivateHandler|
|AudioSetting|AudioHandler|

その他のTypeについては[VRecObjectSettingHandler](VRecObjectSettingHandler_ja.md)を参照してください

詳しい用法については、[ExRecord](ExRecord_ja.md)を参照してください。