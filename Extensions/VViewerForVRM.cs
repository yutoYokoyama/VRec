using System;
using VRM;
using UnityEngine;
namespace VRec.Extensions
{
    public class VViewerForVRM : MonoBehaviour
    {
        public VViewerScript VViewer;
        // Use this for initialization
        void Start()
        {
            if (!VViewer)
            {
                VViewer = GetComponent<VViewerScript>();
            }
            VViewer.AvatarDataHandler += BlendShapeSetting;
        }

        private void BlendShapeSetting(VRecRecordObj obj, VRecEventData data)
        {
            if (data.StrData[0] == "BlendShape")
            {
                var blend = obj.Obj.GetComponent<VRMBlendShapeProxy>();
                if (!blend)
                {
                    return;
                }
                var blendNumber = 0;
                foreach (BlendShapePreset key in Enum.GetValues(typeof(BlendShapePreset)))
                {
                    blend.ImmediatelySetValue(BlendShapeKey.CreateFromPreset(key), data.FloatValues[blendNumber]);
                    blendNumber++;
                }
            }
        }
    }
}