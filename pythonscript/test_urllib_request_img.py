import os
import re
import urllib.request

URL = "https://upload.wikimedia.org/wikipedia/commons/6/69/Japan_Yokohama.png"
PATH = "./data/image"


def main():
    path_file = download_image(PATH, URL)
    
    
def download_image(path, url):
    """ URL をもとにデータファイルをダウンロード """
    # 既存フォルダの確認
    print("Directory name: {}".format(path))
    if not os.path.exists(path):
        print("Make directory")
        os.makedirs(path)
    else:
        print("Directory exists")
    
    # ファイルをダウンロード
    img_file = re.split(r'/', url)[-1]
    path_file = os.path.join(path, img_file)
    urllib.request.urlretrieve(url, path_file)
    return path_file


if __name__ == "__main__":
	main()