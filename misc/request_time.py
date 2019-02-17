import requests
import time


PAGE_URL_LIST = [
	"http://www.shoeisha.co.jp/book/",
	"http://www.shoeisha.co.jp/book/",
	"http://www.shoeisha.co.jp/book/"
]


for page_url in PAGE_URL_LIST:
	res = requests.get(page_url, timeout=10)
	print(
		"ページURL: " + page_url + ", " + \
		"HTTPステータス: " + str(res.status_code) + ", " + \
		"処理時間(sec): " + str(res.elapsed.total_seconds())
	)
	time.sleep(1)