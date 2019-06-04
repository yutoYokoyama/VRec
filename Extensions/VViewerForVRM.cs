using System;
using VRM;
namespace VRec.Extensions
{
    public class VViewerForVRM : VRec.VViewerScript
    {

        // Use this for initialization
        void Start()
        {
            AvatarDataHandler += BlendShapeSetting;
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
                foreach (BlendShapePreset t in Enum.GetValues(typeof(BlendShapePreset)))
                {
                    blend.SetValue(t, data.FloatValues[blendNumber]);
                    blendNumber++;
                }
            }
        }
    }
}