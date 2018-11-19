"""
loggingを使わないログ取得の例
"""
# ------------------
# モジュールインポート
# ------------------
import datetime


# ------------------
# 定数パラメータ設定
# ------------------
LOG_FILE = "../out/log.txt"


# ------------------
# 関数の定義
# ------------------
def mylog(*args):
	msg = " ".join(map(str, [datetime.datetime.now(), ">"] + list(args)))
	print(msg)
	with open(LOG_FILE, "a") as f:
		f.write(msg + "\n")


# ------------------
# メイン処理
# ------------------
def main():
	mylog("hoge", "fuga", "piyon")


if __name__ == "__main__":
	main()


"""
>> python my_logging.py
2018-11-19 13:52:42.813694 > hoge fuga piyon

"""