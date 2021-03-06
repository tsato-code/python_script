### 2018-03-30 Fri

- Git for Windows のインストール。途中でエディタを選択する場面が現れる。Vim, Notepad++, VScodeなどから選ぶ必要があり、シェアと操作性能などを考えていたら、どれにしたらよいのか決まらない。
- リモートリポジトリのコピーコマンド調査。
- ファイルやディレクトリの追加・変更をリポジトリに記録するにはコミットといい、コマンドを調査。
- Git 管理下に置かれた作業中ディレクトリをワークツリーという。これをリポジトリに反映させるには、インデックスというところに置く。

```
$ mkdir test_dir					# ディレクトリ作成
$ cd test_dir						# ディレクトリ移動
$ git init						# カレントディレクトリで Git リポジトリを新規作成
$ echo hoge > sample.txt				# テスト用サンプルファイル作成
$ git status						# Git 管理下のワークツリーとインデックスの状態を確認
$ git add sample.txt					# ワーキングツリーのファイルをインデックスに移動
$ git commit -m "first commit"				# インデックスのファイルをローカルリポジトリに移動
$ git log						# リポジトリの変更履歴確認
$ git remote add origin \
> https://github.com/tsato-code/python_codes.git 	# リモートリポジトリを追加登録
$ git push -u origin master				# リポジトリをプッシュ（ここで GitHub アカウントの Username と Password を入力）
$ git pull origin master				# リモートリポジトリの修正をローカルに反映
$ rm -rf .git/						# ディレクトリを Git 管理から外す
$ git reset HEAD sample.txt				# インデックスのファイルを取り消す
```

### 2018-04-17
- リモートリポジトリの取得。

```
$ git config --global user.name tsato
$ git config --global user.email xxx@example.com
$ git clone http://github.com/tsato-code/python_codes.git
```

### 2018-04-18
- 無視されているファイルを強制追加。

```
$ git add -f sample.txt
```

### 2018-04-26
- ファイルを管理対象から外す。

```
$ git rm --cached sample.txt				# --cached オプションでファイルを残したまま管理対象から外す
$ git rm sample.txt					# --cached なしでファイルごと削除
```


### 2018-05-10
- [学生のための卑近な git・GitHub 入門](https://qiita.com/showmeear/items/ee61984089445e52f794)


### 2018-06-28
- 直前のコミットを取り消し

```
$ git reset --hard HEAD^
```
