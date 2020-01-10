import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

VRecRecordData data;
Converter BitConverter = new Converter();
int frame;
MouseCamera mouseCamera;

void setup() {
  size(600, 600, P3D); //P3Dライブラリを使う
  background(0);
  fill(255);
  stroke(255);
  data= new VRecRecordData().FromByte(loadBytes("bones.vrc"));
  mouseCamera = new MouseCamera(800.0, 0, 0, (height/2.0)/tan(PI*30.0/180.0), 0, 0, 0, 0, 1, 0); // MouseCameraの生成
}

void draw() {
  lights();
  background(0);

  translate(width/2, height/2);
  //rotateY(45);
  //box(300);

  // camera(45.0+100 /*+ 100*(float)Math.cos(frameCount/100.0)*/, -100.0, 150.0+200/*+ 100* (float)Math.sin(frameCount/100.0)*/, 
  //   0.0, -25.0, 0.0, 
  //   0.0, 1.0, 0.0); 
  mouseCamera.update(); // MouseCameraのアップデート
  VRecFrameData frameData= data.Frames.get(frame);
  for (int i = 0; i<frameData.Events.size(); i++) {    
    VRecEventData event =  frameData.Events.get(i);
    HandleEvent(event);
  }
  frame++;
  if (frame>= data.Frames.size()) {
    frame=0;
  }
}
void HandleEvent(VRecEventData event) {
  if (event.Type == 1|| event.Type == 2) {
    Quaternion rot = new Quaternion();
    rot.x = event.FloatValues[3];
    rot.y = event.FloatValues[4];
    rot.z = event.FloatValues[5];
    rot.w = event.FloatValues[6];
    float[] euler = BitConverter.Rot2Euler(rot);


    translate(-50*event.FloatValues[0], -50*event.FloatValues[1], 50*event.FloatValues[2]);
    //  if (event.ObjectId == 0) 
    {
      rotateX((float)Math.PI*euler[0]/180);
      rotateY((float)Math.PI*euler[1]/180);
      rotateZ((float)Math.PI*euler[2]/180);
    }
    if (event.ObjectId == 0)
      box(10);
    else box(5);
    // if (event.ObjectId == 0) 
    {
      rotateZ(-(float)Math.PI*euler[2]/180);
      rotateY(-(float)Math.PI*euler[1]/180);
      rotateX(-(float)Math.PI*euler[0]/180);
    }
    translate(50*event.FloatValues[0], +50*event.FloatValues[1], -50*event.FloatValues[2]);
  }
}
void mousePressed() {
  mouseCamera.mousePressed();
}
void mouseDragged() {
  mouseCamera.mouseDragged();
}
void mouseWheel(MouseEvent event) {
  mouseCamera.mouseWheel(event);
}

class MouseCamera {
  float eyeX, eyeY, eyeZ;
  float centerX, centerY, centerZ;
  float upX, upY, upZ;
  float radius; // 仮想的な球の半径
  float[][] matrix; // 行列
  PVector preVector; // PVectorはProcessingの組み込みクラス
  MouseCamera(float radius) {
    this(radius, width/2.0, height/2.0, (height/2.0)/tan(PI*30.0/180.0), width/2.0, height/2.0, 0, 0, 1, 0);
  }
  MouseCamera(float radius, float eyeX, float eyeY, float eyeZ, float centerX, float centerY, float centerZ, float upX, float upY, float upZ) {
    this.radius = radius;
    this.eyeX = eyeX;
    this.eyeY = eyeY;
    this.eyeZ = eyeZ;
    this.centerX = centerX;
    this.centerY = centerY;
    this.centerZ = centerZ;
    this.upX = upX;
    this.upY = upY;
    this.upZ = upZ;
    matrix = getIdentityMatrix();
  }
  // 毎フレーム処理
  void update() {
    beginCamera();
    camera(eyeX, eyeY, eyeZ, centerX, centerY, centerZ, upX, upY, upZ);
    applyMatrix(matrix[0][0], matrix[0][1], matrix[0][2], matrix[0][3], 
      matrix[1][0], matrix[1][1], matrix[1][2], matrix[1][3], 
      matrix[2][0], matrix[2][1], matrix[2][2], matrix[2][3], 
      matrix[3][0], matrix[3][1], matrix[3][2], matrix[3][3]);
    endCamera();
  }
  // クリックしたときに呼び出す関数
  void mousePressed() {
    switch(mouseButton) {
    case RIGHT: 
      { // 右ボタンをクリックをしたときの処理
        matrix = getIdentityMatrix();
      } 
      break;
    case LEFT: 
      { // 左ボタンをクリックをしたときの処理
        preVector = mouseOnSphere(mouseX-width/2, mouseY-height/2);
      } 
      break;
    case CENTER: 
      { // 中ボタンをクリックしたときの処理
        preVector = new PVector(mouseX-width/2, mouseY-height/2);
      } 
      break;
    }
  }
  // ドラッグしたときに呼び出す関数
  void mouseDragged() {
    switch(mouseButton) {
    case LEFT: 
      { // 左ボタンをドラッグしたときの処理
        PVector v = mouseOnSphere(mouseX-width/2, mouseY-height/2);
        matrix = mult(getRotationMatrix(preVector, v), matrix);
        preVector = v;
      } 
      break;
    case CENTER: 
      { // 中ボタンをドラッグしたときの処理
        PVector v = new PVector(mouseX-width/2, mouseY-height/2);
        matrix = mult(getTranslationMatrix(preVector, v), matrix);
        preVector = v;
      } 
      break;
    }
  }
  // マウスホイールを動かしたときに呼び出す関数
  void mouseWheel(MouseEvent event) {
    matrix = mult(getScaleMatrix(event.getCount()), matrix);
  }
  // 単位行列の取得
  float[][] getIdentityMatrix() {
    return new float[][] {{1.0, 0.0, 0.0, 0.0}, 
      {0.0, 1.0, 0.0, 0.0}, 
      {0.0, 0.0, 1.0, 0.0}, 
      {0.0, 0.0, 0.0, 1.0}};
  }
  // 回転行列の取得
  float[][] getRotationMatrix(PVector v1, PVector v2) {
    PVector v = v1.cross(v2).normalize(); // 回転軸
    float c = v1.dot(v2); // cos
    float s = v1.cross(v2).mag(); // sin
    return new float[][] {{c + v.x*v.x*(1-c), v.x*v.y*(1-c) - v.z*s, v.x*v.z*(1-c) + v.y*s, 0.0}, 
      {v.y*v.x*(1-c) + v.z*s, c + v.y*v.y*(1-c), v.y*v.z*(1-c) - v.x*s, 0.0}, 
      {v.z*v.x*(1-c) - v.y*s, v.z*v.y*(1-c) + v.x*s, c + v.z*v.z*(1-c), 0.0}, 
      {0.0, 0.0, 0.0, 1.0}};
  }
  // 平行移動行列の取得
  float[][] getTranslationMatrix(PVector v1, PVector v2) {
    return new float[][] {{1.0, 0.0, 0.0, v2.x-v1.x}, 
      {0.0, 1.0, 0.0, v2.y-v1.y}, 
      {0.0, 0.0, 1.0, v2.z-v1.z}, 
      {0.0, 0.0, 0.0, 1.0}};
  }
  // 拡大縮小行列の取得
  float[][] getScaleMatrix(float wheelCount) {
    float temp = 10.0; // wheelCountの値が大きいので定数で割る
    return new float[][] {{exp(-wheelCount/temp), 0.0, 0.0, 0.0}, 
      {0.0, exp(-wheelCount/temp), 0.0, 0.0}, 
      {0.0, 0.0, exp(-wheelCount/temp), 0.0}, 
      {0.0, 0.0, 0.0, 1.0}};
  }
  // マウスの座標から球面上の位置ベクトルを取得する
  PVector mouseOnSphere(float x, float y) {
    float _x = x/radius;
    float _y = y/radius;
    PVector res = new PVector(_x, _y, 0.0);
    if (_x*_x + _y*_y > 1.0) {
      res.normalize();
    } else {
      res.z = sqrt(1.0 - _x*_x - _y*_y);
    }
    return res;
  }
  // 行列の積 (m1 * m2)
  float[][] mult(float[][] m1, float[][] m2) {
    assert(m1[0].length == m2.length);
    float[][] res = new float[m1.length][m2[0].length];
    for (int i=0; i<m1.length; i++) {
      for (int j=0; j<m2[0].length; j++) {
        float sum = 0;
        for (int k=0; k<m1[0].length; k++) {
          sum += m1[i][k]*m2[k][j];
        }
        res[i][j] = sum;
      }
    }
    return res;
  }
}
