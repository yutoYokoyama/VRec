using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using VRec;

public class VRecorderForIK : VRecorderScript
{
    protected override VRecEventData[] GetAvatarRecordData(VRecRecordObj t)
    {
        if (t.Type != ObjType.Avatar)
        {
            return null;
        }
        else
        {
            var returnData = new List<VRecEventData>();
            var parentData = new VRecEventData
            {
                ObjectId = t.Id,
                Label = t.Obj.name,
                Type = ObjType.Avatar,
                StrData = new string[2] {"Root",t.Obj.name }
            };
            parentData.SetTransform(t.Obj);
            returnData.Add(parentData);
            var solver = t.Obj.GetComponent<RootMotion.FinalIK.VRIK>().solver;
            {
                var h = solver.spine.headTarget;
                if (h)
                {
                    var headData = new VRecEventData
                    {
                        ObjectId = t.Id,
                        Label = t.Obj.name,
                        Type = ObjType.Avatar,
                        StrData = new string[2] { "Head", h.name }
                    };
                    headData.SetTransform(h.transform);
                    returnData.Add(headData);
                }
            }
            {
                var h = solver.leftArm.target;
                if (h)
                {
                    var data = new VRecEventData
                    {
                        ObjectId = t.Id,
                        Label = t.Obj.name,
                        Type = ObjType.Avatar,
                        StrData = new string[2] { "LeftHand", h.name },
                    };
                    data.SetTransform(h);
                    returnData.Add(data);
                }
            }

            {
                var h = solver.rightArm.target;
                if (h)
                {
                    var data = new VRecEventData
                    {
                        ObjectId = t.Id,
                        Label = t.Obj.name,
                        Type = ObjType.Avatar,
                        StrData = new string[2] { "RightHand", h.name },
                    };
                    data.SetTransform(h);
                    returnData.Add(data);
                }
            }
            {
                var h = solver.spine.pelvisTarget;
                if (h)
                {
                    var data = new VRecEventData
                    {
                        ObjectId = t.Id,
                        Label = t.Obj.name,
                        Type = ObjType.Avatar,
                        StrData = new string[2] { "Pelvis", h.name },
                    };
                    data.SetTransform(h);
                    returnData.Add(data);
                }
            }
            {
                var h = solver.leftLeg.target;
                if (h)
                {
                    var data = new VRecEventData
                    {
                        ObjectId = t.Id,
                        Label = t.Obj.name,
                        Type = ObjType.Avatar,
                        StrData = new string[2] { "LeftLeg", h.name },
                    };
                    data.SetTransform(h);
                    returnData.Add(data);
                }
            }
            {
                var h = solver.rightLeg.target;
                if (h)
                {
                    var data = new VRecEventData
                    {
                        ObjectId = t.Id,
                        Label = t.Obj.name,
                        Type = ObjType.Avatar,
                        StrData = new string[2] { "RightLeg", h.name },
                    };
                    data.SetTransform(h);
                    returnData.Add(data);
                }
            }
            return returnData.ToArray();
        }
    }
}
