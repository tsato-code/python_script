import glob, re

text0 = r"test_hoge"
text1 = r"test_hoge.py"
text2 = r"test_hogehoge.py"

# 文字列オブジェクトの先頭にrをつけてエスケープシーケンスを無効化
# 事前に正規表現オブジェクトを生成
# []で集合、+で1回以上の繰り返し、*で0回以上の繰り返し
regrex = r"test_[a-zA-Z]*.py"
pattern = re.compile(regrex)

print( pattern.match(text0) )
print( pattern.match(text1) )
print( pattern.match(text2) )
print('* '*10)

regrex = r"test_[a-zA-Z]+.py"
pattern = re.compile(regrex)

print( pattern.match(text0) )
print( pattern.match(text1) )
print( pattern.match(text2) )
print('* '*10)

# ディレクトリからファイルを取得
# globでは正規表現を使えない
# 代わりにUnixシェルのルールが使える
# * 任意の0文字以上文字列
# ? 任意の1文字
# [...] カッコ内の範囲に含まれる任意の1文字
# [!...] カッコ内の範囲に含まれない任意の1文字
path_list = glob.glob('test_????.py')
print( path_list )


"""
$ python test_re.py
None
<_sre.SRE_Match object; span=(0, 12), match='test_hoge.py'>
<_sre.SRE_Match object; span=(0, 16), match='test_hogehoge.py'>
* * * * * * * * * * 
None
<_sre.SRE_Match object; span=(0, 12), match='test_hoge.py'>
<_sre.SRE_Match object; span=(0, 16), match='test_hogehoge.py'>
* * * * * * * * * * 
['test_glob.py', 'test_time.py', 'test_tqdm.py', 'test_yaml.py']
"""