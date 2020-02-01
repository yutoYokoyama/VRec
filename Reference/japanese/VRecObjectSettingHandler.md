<<[top](VRec_ja.md)
# **VRecObjectSettingHandler**
class VViewerScript/public delegate

## **説明**
---
<br>


[VViewerScript](VViewerScript_ja.md)内に存在するdelegate型<br>
引数は[VRecEventData](VRecEventData_ja.md)型と対象のオブジェクト。VViewerScript内にはAvatarDataHandler、ModelDataHandler、StaticHandlerの3つが準備されています

VViewerScript内では毎フレームごとに記録された内容を実行・反映します。それらの内容はVRecEventData内のTypeによって呼ばれるHandlerが変わり、その対応表は以下の通りです。

|Type|呼ばれるDelegate|
|:--|:--|
|Avator|AvatarDataHandler|
|Model|ModelDataHandler|
|StaticObject|StaticHandler|

その他のTypeについては[ObjectDataSettingHandler](ObjectDataSettingHandler_ja.md)を参照してください

詳しい用法については、[ExRecord](ExRecord_ja.md)を参照してください。