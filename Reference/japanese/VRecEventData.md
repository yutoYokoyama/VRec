<<[top](VRec_ja.md)
# VRecEventData
namespace:VRec/class

## **説明**
---
毎フレームごとに複数含まれる個々のイベントクラス<br>
本ライブラリではTypeによりその記録・再生の手順が異なる。

|変数名|詳細|
|:-|:-|
|Label|string型のラベル。大抵の場合は対象オブジェクトの名前。TypeがOtherの場合は利用者の定義するイベントラベル|
|ObjectId|int型のId。大抵の場合は対象オブジェクトのId|
|Type|ObjType型の列挙型。[ObjType](ObjType_ja.md)を参照|
|FloatValues|float型の配列|
|StrData|string型の配列|
|||