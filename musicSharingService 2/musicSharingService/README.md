# 各ファイルの説明

## バックエンド

- app.py: バックエンド本体。Flaskを使っている。
- requirements.txt: インストールするPythonパッケージのリスト
- musicSharingServiceVenvForMac/: Pythonの仮想環境。Mac向けのもの。

## フロントエンド
- templates/: テンプレートフォルダ。app.pyで動的に書き換えたり値を渡すようなページはここに入れる。
  - ***要約: HTMLページはここに入れればOK**
  - ここに入れるとapp.pyのrender_templateからhtmlファイルが返せる。
  - index.html: トップページ
  - music.html: 音楽ページ
  - upload.html: 投稿ページ

### コンポーネント
- **パーツ的なもの**が入っている
- components/header.html
  - 上に出てくるメニューバーのパーツ。
  - ここを変えれば全てのメニューバーが変わる

### 基本的にいじらなくてOKなファイル
- base.html: テンプレートファイル。共通で使い回す部分をここに書くと他のページで省略できる。

### 静的ファイル
- static/: 静的ファイルのフォルダ
  - **要約: .cssファイル、.jsファイル、画像ファイルなどはここに入れればOK**
  - URLは「/static/style.css」のようにアクセスできる
    - 例: http://localhost/static/style.css
  - script.js: JavaScriptファイル。これはすべてのページで読み込まれる。
    - (base.htmlで読み込んでいるので)
  - style.css: CSSファイル。これも全てのページで読み込まれる。
    - (base.htmlで読み込んでいるので)

## その他
- db/music.db: 音楽のデータを保存しておくデータベース。
  - SQLiteなのでこのファイルを読み込むだけで使える。サーバーはいらない。
  - あまり手動ではいじらない方がいい
- dev_only: 開発中にだけ使うプログラム
  - delete_music.py: 音楽の削除を手動で行うためのプログラム
  - init_db.py: DBの初期化のためのプログラム。
    - 構造をガラッと変える時などにも使う。
      - 例: 全ての音楽がタグを持てるようにするなど
