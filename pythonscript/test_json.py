import json


def main():
	# 読み込み
	with open("../data/book.json", "r") as f:
		books = json.load(f)
	# 出力
	print(books)
	# 書き込み
	with open("../data/book.json", "w") as f:
		json.dump(books, f)


if __name__ == "__main__":
	main()