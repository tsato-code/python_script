# test_requests.py
import requests
import pprint
    
url = 'https://www.google.co.jp/search'
params = {'q': '日本代表', 'tbm': 'nws'}
r = requests.get(url, params=params)
print(dir(r))
pprint.pprint(r.text)