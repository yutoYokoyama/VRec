<<[top](VRec.md)
# **VRecRecordData**
namespace:VRec

## **Introduction**
---
<br>

This page eaplain about VRecRecordData, which is recording / playback data, and the extension ".vrc" converted to a byte array
They are used by [VRecorderScript](VRecorderScript.md) and [VViewerScript](VViewerScript.md).

## **About VRecRecordData**
---

VRecRecordData is a class that has a list of VRecFrameData.

It has implements GetReducedData, a method to reduce data, and ToByte, FromByte methods to convert between Bytes.

Since Serializabled is set, it can be converted with Unity's JsonUtility, but please note that JsonUtility has an upper limit (1.5 GB) in the size of the character string.

### **Property**
---
|name|class|details|
|:--|:--|:--|
|Platform|PlatformVersion|Enumeration indicating platform type and coordinate system. See [PlatformVersion](PlatformVersion)|
|Records|List<[VRecFrameData](#VRecFrameData)>|A list of VRecFrameData, which is a set of events for each frame. In other words, all data of the target|
|ObjectDataes|List< RecordObjectData>|Data about the object to be recorded|
||||

### **Method**
---
|name|Return value|details|
|:--|:--|:--|
|GetReducedData|VRecRecordData|Each frame is compared, and if there is an object whose coordinates have not changed compared with the previous frame, the data is compressed. Empirically, it can be compressed to about 20%|
|FromByte|VRecRecordData|Convert data using byte array as an argument|
|ToByte|byte[]|Convert itself to a byte array|
||||

## PlatformVersion
---
Value indicating the platform coordinate system indicated by 1 byte. <br>

The 3 bits from the front indicate whether the left-right, up-down, and depth directions are reversed compared to the Unity coordinate system. <br>
If it is 0, it is not inverted, and if it is 1, it is inverted. <br>
The latter 5 bits indicate the unit system. It indicates yards, feet, meters, centimeters, and millimeters in order from the left, and the unit to which 1 is assigned corresponds.

|Platform|enum value|bit value|details|
|:--|:--|:--|:--|
|Unity|4|000 00100|Consistent with Unity coordinate system, units of length are meters|
|UE4|130|100 00010|Only the left-right direction is reversed, the unit of length is cm|
|||||

Anything not mentioned here is subject to the above rules.


## VRecFrameData
---
VRecFrameData is a class that manages a set of VRecEventData in a certain frame and information associated with it. In other words, it handles one frame of information. <br>
As with VRecRecordData, conversion between byte arrays can be performed.

#### **Property**
|name|class|details|
|:--|:--|:--|
|Events|List<[VRecEventData](#VRecEventData)>|The set of events that occur in that frame. In other words, an event group for each frame|
|Displayed|bool|Whether the frame was replay|
|Time|float|The number of seconds from the start of playback that frame|
||||

## **VRecEventData**
---
See [VRecEventData] (VRecEventData.md)

## **「.vrc」**
---

".Vrc" is VRecRecordData written as a binary file. <br>
Keep in mind that all variables are big endian. <br>
The following shows the byte structure.

![VRecRecord](vrc1.png)
![VRecRecord](vrc2.png)
![VRecRecord](vrc3.png)
![VRecRecord](vrc4.png)