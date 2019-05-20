<<[top](VRec.md)
# **VRecRecordData**
namespace:VRec

## **説明**
---
<br>

本ページでは、
[VRecorderScript](VRecorderScript.md)
と[VViewerScript](VViewerScript.md)で扱う記録・再生データであるVRecRecordDataについてと、それをバイト配列に変換した拡張子「.vrc」について解説します。

## **VRecRecordDataについて**
---

VRecRecordDataは、VRecFrameDataのリストを持つクラスです。

データを削減するメソッドであるGetReducedDataと、Byteとの相互変換を行うToByte,FromByteメソッドを実装しています。

Serializabledを設定しているため、UnityのJsonUtilityで変換可能ですが、JsonUtilityはデータの大きさに上限があるため注意してください。
### **プロパティ**
---
|名前|型|解説|
|:--|:--|:--|
|Records|List<[VRecFrameData](#VRecFrameData)>|フレームごとのイベントの集合であるVRecFrameDataのリスト。つまり対象の全データ|
||||

### **メソッド**
---
|名前|戻り値|解説|
|:--|:--|:--|
|GetReducedData|VRecRecordData|各フレームを比較し、前フレームと比較して座標の変わっていないオブジェクトがあればデータを圧縮する。経験的にはおよそ20％程度に圧縮できる|
|FromByte|VRecRecordData|バイト配列を引数としてデータを変換する|
|ToByte|byte[]|自身をバイト配列に変換する|
||||

## VRecFrameData
---
VRecFrameDataはあるフレームにおけるVRecEventDataの集合と、それに付随する情報を管理するクラスです。つまり、1フレームの情報を扱います。<br>
VRecRecordData同様、バイト配列との相互変換を行えます。

#### **プロパティ**
|名前|型|解説|
|:--|:--|:--|
|Events|List<[VRecEventData](#VRecEventData)>|そのフレームに起こるイベントの集合。つまり毎フレームごとのイベント群|
|Displayed|bool|そのフレームが反映されたかどうか|
|Time|float|そのフレームが再生開始から何秒目にあたるかの秒数|
||||

### **メソッド**

|名前|戻り値|解説|
|:--|:--|:--|
|FromByte|VRecFrameData|バイト配列から変換してVRecFrameDataを生成する|
|ToByte|byte[]|VRecFrameDataをバイト配列に変換する|
|

## **VRecEventData**
---
[VRecEventData](VRecEventData.md)を参照してください