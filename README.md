# Tool to Extract Vertical Japanese Text using OCR

This tool is for extracting vertical Japanese text using the pytesseract library, which is a Python OCR library.

※日本語のREADMEは下部にあります。

## Installation

To use this tool, you need to install the following libraries:

- pytesseract
- Pillow
- tqdm

You can install these libraries using the pip command:

```
pip install pytesseract Pillow tqdm
```

In addition, you need to install the Tesseract OCR engine. You can download Tesseract from the following page:

https://github.com/UB-Mannheim/tesseract/wiki

## Usage

This tool can be used from the command line. Execute the command as follows:

```
python ss2txt.py /path/to/image_directory
```

Specify the path to the directory containing image files with vertical Japanese text in `/path/to/image_directory`.

The text will be saved in the specified directory with the name `out-<date>.txt`.

The progress of the processing is displayed using the tqdm library.

## Notes

- This tool is for extracting vertical Japanese text. It may not correctly extract text in horizontal writing.
- This tool uses the Tesseract OCR engine. Although Tesseract supports many languages, its translation accuracy is not perfect.
- This tool may occasionally produce misrecognitions.

---

# OCRを使用して縦書き日本語テキストを抽出するツール

このツールは、PythonのOCRライブラリであるpytesseractを使用して、縦書き日本語テキストを抽出するためのものです。

## インストール

このツールを使用するためには、以下のライブラリをインストールする必要があります。

- pytesseract
- Pillow
- tqdm

これらのライブラリは、pipコマンドを使用してインストールできます。

```
pip install pytesseract Pillow tqdm
```

また、OCRエンジンであるTesseractをインストールする必要があります。Tesseractは以下のページからダウンロードできます。

https://github.com/UB-Mannheim/tesseract/wiki

## 使い方

このツールは、コマンドラインから使用することができます。以下のようにコマンドを実行してください。

```
python ss2txt.py /path/to/image_directory
```

`/path/to/image_directory`には、縦書き日本語テキストが含まれる画像ファイルが入っているディレクトリのパスを指定してください。

テキストは、指定したディレクトリ内に、`out-<日付>.txt`という名前で保存されます。

また、処理の進捗状況は、tqdmライブラリを使用して表示されます。

## 注意事項

- このツールは、縦書き日本語テキストを抽出するためのものです。横書きの場合は、正しくテキストを抽出できない場合があります。
- このツールは、Tesseract OCRエンジンを使用しています。Tesseractは、多くの言語に対応していますが、翻訳精度は完璧ではありません。
- このツールは、まれに誤認識が発生することがあります。
