<<[top](VRec.html)
# **VViewHandler**
class VViewerScript/public delegate

## **説明**
---
<br>

[VViewerScript](VViewerScript.html)内に存在するdelegate型<br>
VViewerScript内にはOnStartHandlerとOnEndHandlerの2つが存在する。
そのVViwerが開始するときと終了するときにそれぞれ呼ばれる。
引数はそのVView自身のTransformとファイル名。

OnStartHandlerは、再生を開始したときに呼ばれる。ループ時にも呼ばれる。
OnEndHandlerは、再生が終端に達したときに呼ばれる。ループ時にも呼ばれる。