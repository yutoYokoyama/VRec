<<[Nagao Lab homepage top](http://www.nagao.nuie.nagoya-u.ac.jp)
# **VRecTop**

Welcome to Nagao Lab VRecProject page<br>

日本語のページは[こちら](./japanese/index.html)<br>

## **Introduction**
---
<br>
This page provides a reference about VRec and its resources.

VRec is a library for recording the actions of VR users. <br>
It is mainly intended for use in Unity. <br>

Have you ever had any problems with VR development? <br>
- Implement history function of VR / AR application such as Archive function of [Cluster.](https://cluster.mu/en)
- I want to do statistical processing and machine learning for what happened in VR
- I'm doing VR related research and want to make demo videos more easily
- I want to make an animation in VR, but only the actor is myself ...

Please use VRec for these problems.

A similar thing that records movements in VR is [Nuitrack](http://download.3divi.com/Nuitrack/doc/UnityMotionCapture_page.html) which is very different.<br>

Works other than UnityEditor <br>
    - Existing ones can only be used in UnityEditor, but VRec can be used in post-build applications. Therefore, it can be used as an archive tool for 3D applications such as VR and AR. <br>
VRec also uses its own binary file (ie, does not rely on Animation or Animator), so it can be used on other platforms than just Unity. <br>
- Can be used for 3D models without Bone, such as non-avatar objects <br>
    - Most recording tools rely heavily on bones, especially HumanoidBone. Therefore, it is often impossible to record just 3D models without those bones applied. In the VR space, events other than motion, such as sound and effects, also occur. <br>
    VRec has functions and interfaces for recording these events as standard. Of course, the amount of data will increase, but it will provide greater convenience. <br>

<video width="480" height="360" controls>
  <source src="VRec紹介動画.mp4" type="video/mp4">
</video>


## **Terms of service**
---
Nagoya University and Nagao laboratory do not compensate for any damages or disadvantages caused by using this service.<br>

## **Environment**
---
- Unity 5.6.3～2018.2
    - .NET 3.5
- OS    Windows10

## **Link**
---
- [GitHub](https://github.com/yutoYokoyama/VRec)
    - resource files such as library files
- [Reference](./VRec.md)
    - detailed usage
- [Qita](https://qiita.com/yuto_onizakura/items/20e6c55233de9049b6e0)
    - simple introduction page (japanese)

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


Copyright © 2017-2020 Nagao Laboratory of Nagoya Univerisity.
All Rights Reserved.
<br>