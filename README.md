# eps converter
ローカルの画像ファイルをeps形式に変換して保存します
対応画像ファイル（上3つしかテストしてないです）
- .jpg
- .jpeg
- .png
- .bmp
- .gif
- .tiff

# 使い方
## 初期セットアップ
```sh
# 家蔵環境を使いたい場合は各自設定してください
pip install requirements.txt
```

## 実行
- プログラム実行
    ```sh
    python eps_converter.py
    ```
- ファイルセレクターが出てくるので，変換したい画像ファイルをGUIで選択
- 保存先のディレクトリを選択

## 注意点
たまにepsに変換すると背景透過部分が黒く塗りつぶされることがあります。
これはPythonの挙動で直すの手間かかりそうなので、その時は外部のサービス使ってください（）


GPTに全部書かせました，すごいね