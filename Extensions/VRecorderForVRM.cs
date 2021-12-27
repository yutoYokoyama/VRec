using System;
using System.Collections.Generic;
using VRM;
using UnityEngine;

namespace VRec.Extensions
{
    public class VRecorderForVRM : MonoBehaviour
    {
        public VRecorderScript VRec;
        private void Start()
        {
            if (!VRec)
            {
                VRec = GetComponent<VRecorderScript>();
            }
            VRec.AvatarRecordHandler += GetBlendShapes;

        }

        private VRecEventData[] GetBlendShapes(VRecRecordObj obj)
        {
            var data = new VRecEventData()
            {
                ObjectId = obj.Id,
                Label = obj.Obj.name,
                Type = ObjType.Avatar,
                StrData = new string[1] { "BlendShape" },
            };
            var blends = obj.Obj.GetComponent<VRMBlendShapeProxy>();

            if (blends != null)
            {
                var blendValues = new List<float>();
                foreach (BlendShapePreset key in Enum.GetValues(typeof(BlendShapePreset)))
                {
                    var blendValue = blends.GetValue(BlendShapeKey.CreateFromPreset(key));
                    blendValues.Add(blendValue);
                }
                data.FloatValues = blendValues.ToArray();
            }

            return new VRecEventData[1] { data };
        }
    }
}