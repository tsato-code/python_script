import os
import tempfile

# 一時ファイル作成
with tempfile.TemporaryFile('w+') as tmp:
    print(tmp)
    print('hoge', file=tmp)
    print(0.123456, file=tmp)
    print('一時ファイルも簡単！', file=tmp)
    tmp.seek(0)
    print(tmp.read())
    
# 名前のある一時ファイル作成
with tempfile.NamedTemporaryFile('w+') as tmp:
    print(tmp.name)
    print('fuga', file=tmp)
    print(0.123456, file=tmp)
    print('名前付き一時ファイルも簡単！！', file=tmp)
    tmp.seek(0)
    print(tmp.read())

# 一時ディレクトリ作成
with tempfile.TemporaryDirectory() as tmp:
    print(tmp)
    with open(os.path.join(tmp, 'test.txt'), 'w+') as f:
        print('piyo!!!', file=f)
        print('一時ディレクトリも簡単！！！', file=f)
        f.seek(0)
        print(f.read())


"""
$ python test_tempfile.py
<tempfile._TemporaryFileWrapper object at 0x00000229729FBAC8>
hoge
0.123456
一時ファイルも簡単！

C:/Users/tsk_sato/AppData/Local/Temp/tmpx92jrnzn
fuga
0.123456
名前付き一時ファイルも簡単！！

C:/Users/tsk_sato/AppData/Local/Temp/tmpcoud28zs
piyo!!!
一時ディレクトリも簡単！！！


"""