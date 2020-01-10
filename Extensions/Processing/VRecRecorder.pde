class Quaternion{
float x;
float y;
float z;
float w;
}
class Converter {
  public final  long ToInt64(byte[] bytes, int index) {
    byte[] data = Arrays.copyOfRange(bytes, index, index+8);
    ByteBuffer buf = ByteBuffer.wrap(data);
    buf.order(ByteOrder.LITTLE_ENDIAN);
    return buf.getLong();
  }
  public final  int ToInt32(byte[] bytes, int index) {
    byte[] data = Arrays.copyOfRange(bytes, index, index+4);
    ByteBuffer buf = ByteBuffer.wrap(data);
    buf.order(ByteOrder.LITTLE_ENDIAN);
    return buf.getInt();
  }
  public final float ToSingle(byte[] bytes, int index) {
    byte[] data = Arrays.copyOfRange(bytes, index, index+4);
    ByteBuffer buf = ByteBuffer.wrap(data);
    buf.order(ByteOrder.LITTLE_ENDIAN);
    return buf.getFloat();
  }
  public final short ToInt16(byte[] bytes, int index) {
    byte[] data = Arrays.copyOfRange(bytes, index, index+2);
    ByteBuffer buf = ByteBuffer.wrap(data);
    buf.order(ByteOrder.LITTLE_ENDIAN);
    return buf.getShort();
  }
    
  public final float[] Rot2Euler(Quaternion r){
    float x = r.x;
    float y = r.y;
    float z = r.z;
    float w = r.w;

    float x2 = x * x;
    float y2 = y * y;
    float z2 = z * z;

    float xy = x * y;
    float xz = x * z;
    float yz = y * z;
    float wx = w * x;
    float wy = w * y;
    float wz = w * z;

    // 1 - 2y^2 - 2z^2
    float m00 = 1f - (2f * y2) - (2f * z2);

    // 2xy + 2wz
    float m01 = (2f * xy) + (2f * wz);

    // 2xy - 2wz
    float m10 = (2f * xy) - (2f * wz);

    // 1 - 2x^2 - 2z^2
    float m11 = 1f - (2f * x2) - (2f * z2);

    // 2xz + 2wy
    float m20 = (2f * xz) + (2f * wy);

    // 2yz+2wx
    float m21 = (2f * yz) - (2f * wx);

    // 1 - 2x^2 - 2y^2
    float m22 = 1f - (2f * x2) - (2f * y2);


    float tx, ty, tz;

    if (Float.compare(m21, 1f) == 0)
    {
        tx = (float)Math.PI / 2f;
        ty = 0;
        tz = (float)Math.atan2(m10, m00);
    }
    else if (Float.compare(m21, -1f) == 0)
    {
        tx = -(float)Math.PI / 2f;
        ty = 0;
        tz = (float)Math.atan2(m10, m00);
    }
    else
    {
        tx = (float)Math.asin(-m21);
        ty = (float)Math.atan2(m20, m22);
        tz = (float)Math.atan2(m01, m11);
    }

    tx *= 360/(Math.PI*2);
    ty *= 360/(Math.PI*2);
    tz *= 360/(Math.PI*2);

    return new float[]{tx, ty, tz};
  }
}

public enum ObjType
{
  Other, 
    Model, 
    Avator, 
    StaticObject, 
    ActiveSet, 
    VRec, 
    AudioSetting,
    MLSetting,
}
class VRecEventData {
  public String Label;
  public int ObjectId;
  public byte Type;
  public float[] FloatValues;
  public String[] StrData;

  public VRecEventData FromByte(byte[] bytes)
  {
    short size = BitConverter.ToInt16(bytes, 0);
    ObjectId = BitConverter.ToInt16(bytes, 2);
    short labelLength = BitConverter.ToInt16(bytes, 4);

    Label = new String(Arrays.copyOfRange(bytes, 6, 6+labelLength));// Encoding.UTF8.GetString(bytes, 6, labelLength);
    Type = bytes[labelLength + 6];
    short valuesLength = BitConverter.ToInt16(bytes, 6 + labelLength + 1);
    FloatValues = new float[valuesLength];
    for (int i = 0; i < valuesLength; i++)
    {
      FloatValues[i] = BitConverter.ToSingle(bytes, 6 + labelLength + 1 + 2 + 4 * i);
    }
    short strDataLength = BitConverter.ToInt16(bytes, 6 + labelLength + 1 + 4 + 4 * (valuesLength - 1) + 2);
    short length = (short)(6 + labelLength + 1 + 4 + 4 * (valuesLength - 1) + 2 + 2);
    StrData = new String[strDataLength];
    for (int i = 0; i < strDataLength; i++)
    {
      short strLength = BitConverter.ToInt16(bytes, length);
      StrData[i] =new String(Arrays.copyOfRange(bytes, length+2, length+2+strLength));// Encoding.UTF8.GetString(bytes, length + 2, strLength);
      length += (short)(2 + strLength);
    }
    return this;
  }
}



class VRecFrameData
{
  public boolean Displayed;
  public List<VRecEventData> Events;
  public float Time;

  public VRecFrameData FromByte(byte[] bytes)
  { 

    Time = BitConverter.ToSingle(bytes, 4);
    short dataCount = BitConverter.ToInt16(bytes, 8);
    long index = 0;
    Events = new ArrayList<VRecEventData>();
    for (long i = 0; i < dataCount; i++)
    {
      short size = BitConverter.ToInt16(bytes, 10 + (int)index);
      byte[] toArray =       Arrays.copyOfRange(bytes, 10 + (int)index, 10+(int)index+(int)size);
      Events.add(new VRecEventData().FromByte(toArray));
      index += size;
    }
    return this;
  }
}


class VRecRecordData {
  int Platform=0;
  public List<VRecFrameData> Frames;

  public VRecRecordData FromByte(byte[] bytes)
  {
    long index = 0;
    Platform = bytes[(int)index];
    index++;            
    long objectDataCount = BitConverter.ToInt64(bytes, (int)index);
    index += 8;

    while (index < (long)objectDataCount + 8 + 1)
    {
      int size = BitConverter.ToInt32(bytes, (int)index);  
      index += (long)size + 4;
    }


    long dataCount = BitConverter.ToInt64(bytes, (int)index);

    index += 8;
    Frames = new ArrayList<VRecFrameData>();
    for (long i = 0; i < dataCount; i++)
    {
      int size = BitConverter.ToInt32(bytes, (int)index);
      byte[] toArray =  Arrays.copyOfRange(bytes, (int)index, (int)index+ size);
      Frames.add(new VRecFrameData().FromByte(toArray));
      index += (long)size;
    }
    return this;
  }
}
