# Project Gutenberg からテキストファイルをダウンロードして保存
import re
import os
import urllib.request


URL = "http://www.gutenberg.org/cache/epub/35688/pg35688.txt"
PATH = "./data/text"


def main():
    download_text = download(PATH, URL)
    text = reading(download_text)
    print(text)


def download(path, url):
    """ URL をもとにデータファイルをダウンロード """
    
    # 既存フォルダの確認
    print("Directory name: {}".format(path))
    if not os.path.exists(path):
        print("Make directory")
        os.makedirs(path)
    else:
        print("Directory exists")
    print("-"*80)
    
    # ファイルをダウンロード
    txt_file = re.split(r'/', url)[-1]
    path_file = os.path.join(path, txt_file)   
    urllib.request.urlretrieve(url, path_file)
    return path_file


def reading(download_text):
    binarydata = open(download_text, 'rb').read()
    text = binarydata.decode('utf-8')
    text = text.strip()
    return text