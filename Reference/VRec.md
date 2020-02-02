<<[top](./index.md)
# **VRec**

## **Introduction**
---
<br>
VRec is a library for recording and playing back 3D content. <br>

If you only want to record and play back simple avatar movements, [VRecorderScript](VRecorderScript.md) and [VViewerScript](VViewerScript.md) make it possible.<br>

If you want to record more operations, such as changing textures or reflecting particles, please refer to the other documentation (especially [ExRecord](ExRecord.md ))<br>

Please refer to [VRecRecordData] (VRecRecordData.md) for the byte format of ".vrc" format.<br>

If you want know more information, please ask @[yuto_onizakura](https://twitter.com/yuto_onizakura).<br>

Please Refer to the following for each component.<br>

<br>

## **主な機能・コンポーネント**
---
<br>

- [VRecorderScript](VRecorderScript.md) Recording component
    - [MikeRecorder](MikeRecorder.md)
        - Component for recording with microphone
- [VViewerScript](VViewerScript.md)    Playback component
    - [ObjectDataSettingHandler](ObjectDataSettingHandler.md)
    - [VRecObjectSettingHandler](VRecObjectSettingHandler.md)
        - Delegate called for a specific ObjectType
    - [VViewerHandler](VViewerHandler.md)
        - Delegate called when VViewer starts or ends
- [ObjType](ObjType.md) VRec record type
- [ExRecord](ExRecord.md) Refer to when you want to register and play your own operations and events
- [VRecFilePathHelper](VRecFilePathHelper.md)　Helpers for file paths
- [VRecRecordData](VRecRecordData.md) details on the data group recorded / eeproduced in VRec or the byte format of ".vrc" format
<br>


## **Contact**
---
Nagoya University <br>
Graduate School of Informatics <br>
Department of Intelligent Systems <br>
Nagao Lab.<br>
Yuto Yokoyama<br>
yokoyama@nagao.nuie.nagoya-u.ac.jp<br>
Twitter: [@yuto_onizakura](https://twitter.com/yuto_onizakura)<br>


<br>