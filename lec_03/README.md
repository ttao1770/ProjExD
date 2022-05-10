## 第3回
### tkinterで迷路ゲーム実装
#### 3限：基本機能
- ゲーム概要：
- rensyu03/maze.pyを実行すると，1500x900のcanvasに迷路が描画され，迷路に
沿ってこうかとんを移動させるゲーム
- 実行するたびに迷路の構造は変化する
- 操作方法：矢印キーでこうかとんを上下左右に移動する
- プログラムの説明
- maze_makerモジュールのshow_maze関数でcanvasに迷路を描画する
- PhotoImageクラスのコンストラクタとcreate_imageメソッドでこうかとんの画
像を(1,1)に描画する
- bindメソッドでKeyPressにkey_down関数を，KeyReleaseにkey_up関数を紐づけ
る
- main_proc関数で矢印キーに応じて，こうかとんを上下左右に1マス移動させ，
afterメソッドで0.1秒後にmain_procを呼び出す

#### 4限：追加機能
- ゴールとスタートを作った
