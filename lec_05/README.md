## 第5回
### Pygameでゲーム実装
#### 3限：基本機能
- ゲーム概要：
- rensyu04/dodge_bomb.pyを実行すると，1600x900のスクリーンに草原が描画され，こうかとんを
移動させ飛び回る爆弾から逃げるゲーム
- こうかとんが爆弾と接触するとゲームオーバーで終了する
- 操作方法：矢印キーでこうかとんを上下左右に移動する
- プログラムの説明
- dodge_bomb.pyをコマンドラインから実行すると，pygameの初期化，main関数の順に処理が進む
- ゲームオーバーによりmain関数から抜けると，pygameの初期化を解除し，プログラムが終了する
- Screenクラスは、スクリーンの生成,背景画像の描画を行う
- Birdクラスは,こうかとんの描画を行う
- Bombクラスは,爆弾の描画を行う
- Groupメソッドで、爆弾を５個生成する
- main関数では，clockの生成，スクリーンの生成，背景画像の描画，こうかとんの描画，爆弾の描画
を行う
- main関数の無限ループでは，キー操作に応じたこうかとんの移動，指定速度に応じた爆弾の移動を
行う
- Rectクラスのcolliderectメソッドにより，こうかとんと爆弾の接触を判定する
- check_bound関数では，こうかとんや爆弾の座標がスクリーン外にならないようにチェックする
#### 4限:拡張機能
### 開始直後のゲームオーバー回避
- ゲーム開始時にこうかとんの周りに爆弾が生成されないように設定した
- ゲーム開始時に(0,0)から(100,100)の範囲に爆弾を生成することで工科トンと当たることを避けた
### 時間経過ごとに爆弾が早くなるように設定した
- while分が１度処理されるごとに301/300倍づつ早くなるようにした
### 爆弾の動きを変則的にした
- mathメソッドを使うことでsin,cosを実装して複雑な動きを実現した
### start画面を作った
- 右上のxボタンを押すことで始めることができる関数をつくった