import os
import argparse
import pytesseract
from PIL import Image
from tqdm import tqdm
import datetime

# コマンドライン引数の設定
parser = argparse.ArgumentParser(description="OCRを使用して縦書き日本語テキストを抽出する")
parser.add_argument("img_dir", help="画像ファイルが含まれるディレクトリのパス")
args = parser.parse_args()

# 出力ファイル名の生成
now = datetime.datetime.now()
output_filename = "out-{}.txt".format(now.strftime("%Y%m%d"))

# 出力ファイルのパスを生成
output_file = os.path.join(args.img_dir, output_filename)

# すべての画像ファイルを順に処理
with open(output_file, "w", encoding="utf-8") as f:
    # tqdmを使用して進捗を表示する
    for filename in tqdm(os.listdir(args.img_dir)):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            filepath = os.path.join(args.img_dir, filename)
            image = Image.open(filepath)
            text = pytesseract.image_to_string(image, lang="jpn_vert")
            f.write(text)
