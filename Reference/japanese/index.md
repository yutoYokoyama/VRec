<<[長尾研ホームページトップへ](http://www.nagao.nuie.nagoya-u.ac.jp)
# **VRecTop**

長尾研究室 VRecProjectページへようこそ

## **説明**
---
<br>
本ページはVRecに関するリファレンスとそのリソースを提供するページです。

VRecはVR利用者の行動を記録するためのライブラリです。<br>
主にUnityで用いられることを想定しています。<br>

VR開発をする上で、このようなことに困ったことはありませんか？<br>
- Clusterのアーカイブ機能のようなVR・ARアプリケーションの履歴機能を実装したい
- VR内で起こったことに対して統計処理・機械学習を行いたい
- VR関連の研究をやっていて、デモ動画をもっと簡単に作りたい
- VRでアニメーションを作りたいけど、役者が自分しかいない…

これらの問題に対して是非VRecを使ってください。

VR内の動きを記録する類似のものに、[Nuitrack](http://download.3divi.com/Nuitrack/doc/UnityMotionCapture_page.html)や[EasyMotionRecorder](https://github.com/duo-inc/EasyMotionRecorder)が存在しますが、これらとは大きく違います。<br>

- UnityEditor以外でも動作<br>
    - 既存のものはUnityEditor上でしか使えませんが、VRecはビルド後のアプリケーションでも使うことが出来ます。そのため、VR・ARなど3Dアプリケーションのためのアーカイブツールとして使うことが出来ます。<br>
またVRecは独自のバイナリファイルを用いるため(つまりAnimationやAnimatorに依存していない)、Unityだけでなく他のプラットフォームでも利用することが可能です。<br>
- 非アバターオブジェクトなど、Boneの使われていない3Dモデルにも利用可能<br>
    - 記録ツールのほとんどはBone、特にHumanoidBoneに強く依存しています。そのため、それらのBoneが適応されていないただの3Dモデルの記録は不可能であることが多いです。また、VR空間内では音やエフェクトの発生など、モーション以外の出来事も発生します。<br>
    VRecはこれらの事象を記録するための機能・インターフェースを標準で備えています。もちろん、データ量としては増大しますが、より大きな利便性を確保しています。<br>

<video width="480" height="360" controls>
  <source src="VRec紹介動画.mp4" type="video/mp4">
</video>


## **利用規約**
---
本大学および本研究室は，本サービスを利用することによって生じたいかなる損害・不利益等を補償しません．<br>

## **動作確認環境**
---
- Unity 5.6.3～2018.2
    - .NET 3.5
- OS    Windows10

## **リソースリンク**
---
- [GitHub](https://github.com/yutoYokoyama/VRec)
    - ライブラリファイルなどのリソースファイルはこちら
- [リファレンス](./VRec.md)
    - 詳しい使い方などはこちら
- [Qita](https://qiita.com/yuto_onizakura/items/20e6c55233de9049b6e0)
    - 簡単な紹介ページ

<br>

## **連絡先**
---
名古屋大学<br>
情報学研究科<br>
知能システム学専攻<br>
長尾研究室所属<br>
横山勇斗<br>
yokoyama@nagao.nuie.nagoya-u.ac.jp<br>
Twitter: [@yuto_onizakura](https://twitter.com/yuto_onizakura)<br>

<br>