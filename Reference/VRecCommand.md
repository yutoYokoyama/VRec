<<[top](VRec.html)
# **VRecCommand**
namespace:VRec/enum

## **説明**
---
<br>

記録するオブジェクトを、 [ObjType](ObjType.html) がVRecであるものについて、ユーザが発行できるコマンドの列挙型です。
利用者は特に気にする必要はなく、記録が始まる前に対象をAddRecordObjしておけば、自動的に再生・停止を記録します。

事前にイニシャライズを済ませておきたい場合は、AddRecordObjのすぐあとに

```cs:
VRecObjectSet(transform, VRecCommand.Init, fileName);
```
を呼び出せばよいでしょう。

## **一覧**
---

|名称|詳細|
|:-|:-|
|Init|初期化操作を行う|
|Start|再生を開始・再開する|
|Stop|再生を停止する|
|Hide|再生するオブジェクトを非表示にする。再生も止まる|
|Display|再生するオブジェクトの非表示を解除する。再生も開始する|
|PositionSet|座標をセットする|
|||

<br>