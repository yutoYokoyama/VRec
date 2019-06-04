﻿using UnityEngine;
using VRec;

public class VViewerScriptForIK : VViewerScript
{

    protected override void SetAvatarTransform(VRecRecordObj obj, VRecEventData data)
    {
        Debug.Log(data.StrData[0]);
        var ik = obj.Obj.GetComponent<RootMotion.FinalIK.VRIK>();
        if (!ik)
            ik = obj.Obj.gameObject.AddComponent<RootMotion.FinalIK.VRIK>();
        switch (data.StrData[0])
        {
            case "Head":
                if (!ik.solver.spine.headTarget)
                {
                    ik.solver.spine.headTarget = new GameObject(data.Label + "_Head").transform;
                    ik.solver.spine.headTarget.parent = transform;
                }
                SetTransform(ik.solver.spine.headTarget, data.GetPosition(), data.GetEulerAngles());

                break;
            case "LeftHand":
                if (!ik.solver.leftArm.target)
                {
                    ik.solver.leftArm.target = new GameObject(data.Label + "_LeftArm").transform;
                    ik.solver.leftArm.target.parent = transform;
                }
                SetTransform(ik.solver.leftArm.target, data.GetPosition(), data.GetEulerAngles());
                break;
            case "RightHand":
                if (!ik.solver.rightArm.target)
                {
                    ik.solver.rightArm.target = new GameObject(data.Label + "_RightArm").transform;
                    ik.solver.rightArm.target.parent = transform;
                }
                SetTransform(ik.solver.rightArm.target, data.GetPosition(), data.GetEulerAngles());


                break;
            case "LeftLeg":
                if (!ik.solver.leftLeg.target)
                {
                    ik.solver.leftLeg.target = new GameObject(data.Label + "_LeftLeg").transform;
                    ik.solver.leftLeg.target.parent = transform;
                }
                SetTransform(ik.solver.leftLeg.target, data.GetPosition(), data.GetEulerAngles());

                break;
            case "RightLeg":
                if (!ik.solver.rightLeg.target)
                {
                    ik.solver.rightLeg.target = new GameObject(data.Label + "_RightLeg").transform;
                    ik.solver.rightLeg.target.parent = transform;
                }
                SetTransform(ik.solver.rightLeg.target, data.GetPosition(), data.GetEulerAngles());
                break;
            case "Pelvis":
                if (!ik.solver.spine.pelvisTarget)
                {
                    ik.solver.spine.pelvisTarget = new GameObject(data.Label + "_Pelvis").transform;
                    ik.solver.spine.pelvisTarget.parent = transform;
                }
                SetTransform(ik.solver.spine.pelvisTarget, data.GetPosition(), data.GetEulerAngles());
                break;
            case "RightFinger":
                break;
            case "LeftFinger":
                break;
            case "Root":
                if(obj.Obj)
                {
                    SetTransform(obj.Obj,data.GetPosition(),data.GetEulerAngles());

                }
                break;
            default:
                break;
        }
    }
}
