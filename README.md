# VRecLib
VRecProjectPageへようこそ

VRecは、VRゲームやコミニケーションを対象とした、アバターやそれに付随するオブジェクトの動きを記録するためのライブラリ、フォーマットの総称です。
現在はUnityでのライブラリ提供を行っています。

# 1.ライブラリの導入

本ページからVRec.dllをダウンロードする。

Unityのプロジェクト画面にドラッグ＆ドロップ。

# 2.録画の方法
録画方法は2種類あります。
Editor上で行う方法と、スクリプトからメソッドを呼び出して行う方法です。

## Editor上での方法
---

<details>

1. シーン上に空のオブジェクトを作成する。
2. VRecorderScriptコンポーネントをアタッチ
3. FileNameに保存したいファイル名を入力する
4. RecordObjsのsizeを動きを記録したいオブジェクトの数に設定する
5. RecordObjsの各Elementに対して、Objに記録したいオブジェクトをアタッチする。その後、そのオブジェクトを何として記録したいかを登録する
6. シーンを再生後、Start On Editorのチェックを入れる

録画開始に成功している場合、ログ画面にデバッグメッセージが表示されます

この方法はスクリプトを書かずに利用できますが、途中からのオブジェクトの追加には対応できません。

既にシーンに存在している1つのアバターの動きを記録する場合などに最適です。
</details>

## スクリプトを用いる方法
---

<details>

1. シーン上に空のオブジェクトを作成する。
2. 以下のようなスクリプトをアタッチする。
```cs:
using UnityEngine;

public class VRecRecording : VRec.VRecorderScript
{
    public GameObject AvatarModelRoot;
    pubic string FileName;
    private void Start()
    {
        AddRecordObj(AvatarModelRoot,VRec.ObjType.Avator);
    }

    public void VRecStart()
    {
        StartRecord(FileName);
    }

    public void VRecEnd()
    {
        EndRecord();
    }
}
```
3. シーンを再生あるいはゲームを起動する。
4. VRecStart()が呼ばれてからVRecEnd()が呼ばれる間の、登録したオブジェクトの動きが記録される。

この方法は、スクリプトを書く必要がありますが、その分複雑なオブジェクトの登録や操作が可能です。
</details>

## 録画に関するTips
---

<details>

- オブジェクトに対して指定できるObjTypeとその記録内容は以下のようになります
    - Other
        - 後述するイベントコードを記録するためのType。ライブラリが特別に行うものはありません。位置も記録していません。
    - Model
        - HumanoidBoneの使われていない一般的な3Dモデルの記録に向いています。人型Avatarの記録も可能ですが、データや処理の量が増大するため非推奨です。
    - Avatar
        -　HumanoidBoneが適用されている人型アバターの記録に向いています。HumanoidBoneの座標を利用しているため、記録したものとは別のアバターにも適応できますが、身長が著しく違うアバター間では不具合が発生しがちです。
    - StaticObject
        - Staticなオブジェクト、つまり録画開始から終了まで動かないオブジェクトの記録に適しています。表現上はModelと変わりませんが、遥かに軽量に記録します。もちろんですが、初期位置以外の座標が記録されません。
    - ActiveSet
    - AudioSetting
        - ライブラリ内部で使用するためのObjTypeです。指定しても記録されません。位置も記録していません。
    - VRec
        - VViewerScriptがアタッチされているオブジェクトを記録します。これを用いることで、任意のタイミングで別の.vrcファイルを再生できます。
- 記録される座標はワールド座標であるため、子オブジェクトを登録するのは非推奨

- MeshRenderrerなどの変化は記録されない。個別にObjType.Otherとしてイベントコードを登録する必要がある。詳しくは「#イベントの登録」項を参照。

- VRMアバターのみ、別途配布する「VRecorderForVRM」を使用すると表情などを表現するBlendShapeの値を記録できます

- スペックにもよりますが、問題なくVRが動作する程度であれば、最低でも数万オブジェクトを同時に記録できます。
    - ここでのオブジェクト数は、木構造に含まれるすべてのGameObjectの数。例えば、2つの子オブジェクトを持つGameObjectであればオブジェクト数は3になります。一般的な人型アバターのオブジェクト数は100～200。
- vrcファイルとJSONファイルの双方で出力しますが、vrcファイルの方が遥かに軽量です。動きの激しさにもよりますが、1アバターで10秒ほど記録した場合1MB程度の容量になります。
</details>

# 3. 再生の方法

再生も、録画と同じようにEditor上とスクリプトを書く方法の2つがあります。

## 共通の前準備
---


 Resourcesフォルダ(EditorではAssets/Resources)に「Models」フォルダを作成し、その中に登録したオブジェクトと同一のファイル(.prefabや.fbxなどUnityで使用できるファイル形式)を移動させる必要があります。

 これは、今後THE SEED ONLINEやVRoidHubなどとの連携で不必要にする予定です。

## Editor上での方法
---

<details>

1. VViewerScriptをアタッチし、再生したいvrcファイルのファイル名を入力する。
    - このとき、Resources/VRecData/以下にvrcファイルが存在する必要があります。また、そこからの相対パスであれば別の場所でも可能です。
2. シーンを再生し、Start On Editorのチェックを入れる。

読み込みに成功すれば、モデルのロードが終わった後、VRecファイルの再生が行われます。

また、録画時同様、スクリプトを書いた方が細かな動作が行いやすいです。

</details>


## スクリプトを用いる方法
---

<details>
1. シーン上に空のオブジェクトを作成する。

2. 以下のようなスクリプトをアタッチする。
```cs:
using UnityEngine;

public class VRecRecording : VRec.VViewerScript
{
    pubic string FileName;

    public void VViewStart()
    {
        StartView(FileName);
    }

    public void VViewEnd()
    {
        EndView();
    }
}
```

4. シーンを再生あるいはゲームを起動する。

5. StartView()を呼び出すと録画内容が再生される。

</details>

## 再生に関するTips
---

<details>
    
- 「VViewerScript」を持つオブジェクトのスケールは1:1:1以外にすると正しく再生されない可能性があります。逆に1:1:1であれば拡大・回転・移動は正確に行われる。
リソースファイルが正しく配置されていない場合、空のオブジェクトが生成され、空のオブジェクトに移動が反映される。

- 「PrefabLoadError」が出るときは
    - 1. Modlesフォルダが作成されていない
    - 2. Modelsフォルダに対象のオブジェクトがない
    - 3. Modelsフォルダにあるオブジェクトの名前が間違っている(例えばModel.prefabファイルがModel(Clone).prefabになっているとか)
    - などの原因が考えられます

- VViewerScriptを継承したコンポーネントでは、Updateメソッドが上書きされていると上手く再生されません。その場合はbase.Update()を呼び出すことをわすれないでください。
</details>

## **独自にイベントを登録する**
---

モデルの色やSkinnedMeshRendrrerの変化は記録していません。そのため、反映するためには独自にイベントを登録する必要があります。
独自のイベントを登録するためには、録画側と再生側でそれぞれスクリプトを追加しなければなりません。

### 録画側
---
VRecorderScript.AddExRecord()を呼び出すことでイベントコードを追加できます。
<details>

```cs:
AddExRecord(string EventLavel,float[] Values,string[] StrData)
```

- EventLavel:string型で登録されているイベントラベル。これによってイベントを区別する。

- Values:float型の配列で記録できる値

- StrData:string型の配列で記録できる値

あるいは

```cs:
AddExRecord(ObjectData data)
```

 - data
    - Label,Id,FloatValues,StrDataを持つクラス。

以上のメソッドを使用し、1回だけの特別なイベントコードを登録することができます。

例えば、「ある座標にプレハブにしたエフェクトを設置したい」ときには、

```cs:
var effect = Instanciate(EffectPrefab).transform;
AddExRecord("EffectMake",
new float[6]{
    effect.position.x,
    effect.position.y,
    effect.position.z,
    effect.eulerAngles.x,
    effect.eulerAngles.y,
    effect.eulerAngles.z},
    new string[1]{effect.name})
```
あるいは

```cs:
var effectData = new ObjectData{
Label = "EffectMake",
StrData = new string[1]{effect.name},
}
effectData.SetTransform(effect);

AddExRecord(effectData);
```
と書くことで「EffectMake」というラベル、座標、エフェクトのオブジェクト名を登録することができました。

AddExRecordの詳しい引数、詳細はスクリプトレファレンスを参照してください。
</details>

### 再生側
---

再生側では、録画側で設定したイベントコードを元にイベントを実行できます。
delegate型であるVRViewerScript.OtherObjectSetting(ObjectData data)を使い、AddExRecordを用いて登録されたObjectDataのみを受け取り、実行します。

<details>
例えば、前述の「ある座標にプレハブにしたエフェクトを設置したい」ときには、

```cs:
using UnityEngine;

public class VRecRecording : VRec.VViewerScript
{
public GameObject[] Effects;

private void Start(){
VViwer.OtherObjectSetting += EffectHandler;
}

private void EffectHandler(ObjectData data){
    if(data.Label == "EffectMake"){
    var effectName = data[0];

    var  effect = Effects.FirstOrDefault(n => n.name == effectName);

    Instanciate(effect,data.GetPosition(),data.GetEulerAngles());
    }
}
```
というスクリプトを書く必要があります。
</details>

<br>
<br>

お困りの場合は以下までご連絡ください

---
名古屋大学

情報学研究科

知能システム学専攻

長尾研究室所属

横山勇斗

yokoyama@nagao.nuie.nagoya-u.ac.jp

Twitter: @[yuto_onizakura](https://twitter.com/yuto_onizakura)