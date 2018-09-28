# ------------------
# モジュールインポート
# ------------------
import requests

# ------------------
# 定数パラメータ設定
# ------------------
"""
以下にアクセスしてトークンキーを取得
https://notify-bot.line.me/my/
../data/line_access_token.txtに保存
"""
IN_FILE = "../data/line_access_token.txt"
URL = "https://notify-api.line.me/api/notify"


# ------------------
# 関数の定義
# ------------------
def line_access_token(in_file=IN_FILE):
    with open(in_file, encoding="shift_jis") as f:
        token = f.read()
    return token


# ------------------
#  メイン処理
# ------------------
def main():
    token = line_access_token()
    headers = {"Authorization" : "Bearer " + token}
    message =  "Windows 10 Home の Python 環境から LINE notify を使って送信！"
    payload = {"message" :  message}
    files = {"imageFile": open("../out/contour.png", "rb")}

    r = requests.post(URL, headers=headers, params=payload, files=files)
    print(r)


if __name__ == '__main__':
    main()