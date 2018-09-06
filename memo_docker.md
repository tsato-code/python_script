# Docker の作業手順
- 2018-01-24
- Windows 10 Home に Docker をインストールしてコンテナ上で ubuntu を使うための手順。
- ホスト OS Windows 10 Home で動作確認


## インストール
- Docker 入門記事：
https://qiita.com/maemori/items/52b1639fba4b1e68fccd
- 以下のページから "Docker ToolBox on Windows" をダウンロード、インストーラに従う：
https://docs.docker.com/toolbox/toolbox_install_windows/
- "Docker for Windows" はWindows 10 Home に非対応であることに注意。


## コンテナ上で ubuntu を動かす
- Docker Quickstart Terminal を立ち上げる。すべてここで操作することを前提にする。
- 以下コマンドで Docker 公式の ubuntu イメージファイルを探す：
$ docker search ubuntu
- 以下コマンドで適当なイメージファイルを落とす：
$ docker pull ubuntu
- 以下コマンドでイメージファイルを落としたことを確認：
$ docker images
- 以下コマンドで ubuntu のコンテナ作成・起動（--name コンテナの名前は省略可）：
$ docker run -it -- name コンテナ名 ubuntu bash
- 以下コマンドでコンテナを停止することなく、コンテナから抜ける：
$ ctrl+p ctrl+q
- 以下コマンドでコンテナ停止、コンテナから抜ける：
$ exit
- 以下コマンドで、起動中のコンテナを Docker 側から停止・起動できる：
$ docker stop コンテナ名
$ docker start コンテナ名
- Docker から以下コマンドでコンテナ稼働状況を確認：
$ docker ps
- 以下コマンドで、起動中の ubuntu コンテナに入って bash を叩く：
$ docker exec -it コンテナ名 bash
- 以下コマンドでコンテナの削除：
$ docker rm コンテナID
- 以下コマンドでコンテナの一括削除：
$ docker rm `docker ps -aq`


## コンテナに割り当てる CPU コア数やメモリ上限の値を変更
- デフォルトは1コア1024MBの割り当てになるはず。これを変更する。
- まず、 "Docker ToolBox for Windows" と同時にインストールされた "Oracle VM VirtualBox" を GUI で立ち上げる。
- 起動中の VM （"default" という名前がついているはず）を停止させ、設定「システム」からタブ「マザーボード(M)」のメインメモリーのスライドバーと、タブ「プロセッサー(P)」のプロセッサー数のスライドバーをそれぞれ適当な値に操作する。
- コンテナ起動時に以下のコマンドを実行：
$ docker run -m 25600m -it ubuntu bash
- ターミナルから以下のコマンドで割り当てられたコア数を確認：
$ cat /proc/cpuinfo | grep processor
- コンテナ起動時にコア数を指定しなくても、VirtualBox で指定した値が自動的に割り当てられる。
- CPU コア数の細かい指定方法が以下のページに書かれているが、どうもうまくいかない：
https://qiita.com/Yuhsak/items/d1438d83e480a93423c9


## ホスト OS とコンテナ上の ubuntu の共有フォルダ作成
- 基本的にはコンテナ作成時にマウントする。
- （１）インストーラに従ってインストールすると、デフォルトではホスト側 Users ディレクトリ以下しかマウントできないはず：
$ docker run -v /c/Users/tsk_sato/share_test:/tmp/data -it ubuntu /bin/bash
- （２）ホスト側の Users 配下にないディレクトリをマウントするには VirtualBox を操作する。
- 参考ページ：
https://qiita.com/dojineko/items/f623894ef2436bef890e
- まず、 "Docker ToolBox for Windows" と同時にインストールされた "Oracle VM VirtualBox" を GUI で立ち上げる。
- 起動中の VM （"default" という名前がついているはず）の、設定「共有フォルダ」から共有フォルダーリストに D ドライブを追加し、適当なフォルダー名（ここでは D_DRIVE という名前）をつけ、「自動マウント」「永続化する」のチェックボックスにチェックしておく。
- 次に Docker Quickstart Terminal から以下のコマンド：
$ docker-machine ssh default 'sudo mkdir -p /d'
$ docker-machine ssh default 'sudo mount -t vboxsf -o uid=0,gid=0 D_DRIVE /d'
- 最後に、コンテナ起動時に D ドライブは以下のディレクトリを指定：
$ docker run -v /d/share:/mnt/share -it --name TEST_SHARE ubuntu bash
- 上の共有フォルダ設定は、VirtualBox が停止するとマウントが切れるようだ。なので（Docker の裏で動いている） VirtualBox を起動するたびに同じように設定する必要があるかもしれない。


## ubuntu コンテナにパッケージをインストール
- 以下コマンドで apt-get のアップデート（これをやらないとパッケージのインストールができなかった）：
$ apt-get update
- 以下コマンドで python 関連のパッケージ一覧表示：
$ apt-cache search python
- 以下コマンドで python3 をインストール：
$ apt-get install -y python3
$ apt-get install -y python3-pip
- 例えば以下コマンドで pip から PyTorch がインストールできる：
$ pip3 install http://download.pytorch.org/whl/cpu/torch-0.3.0.post4-cp35-cp35m-linux_x86_64.whl 
$ pip3 install torchvision


## python から日本語を扱えるようにする
- ubuntu コンソールから python 実行時に文字コードエラーを起こさないように以下を設定：
$ apt-get install language-pack-ja
$ export LANG=ja_JP.UTF-8
$ update-locale LANG=ja_JP.UTF-8


## ホスト OS からコンテナ上の ubuntu の python を動かす
- 例えば、以下コマンドで簡単な文を出力できる：
$ docker exec コンテナ名 python3 -c "print('hogehoge')"
- 以下コマンドで python のインタプリタ起動：
$ docker exec -it コンテナ名 python3
- 以下コマンドでコンテナ上の ubuntu に置かれた python スクリプトを実行：
$ docker exec コンテナ名 python3 /ubuntuディレクトリ/スクリプト.py
- 以下コマンドでコンテナ上の ubuntu に置かれた python スクリプトを文字コード指定して実行：
$ docker exec -e LANG=ja_JP.UTF-8 コンテナ名 python3 /ubuntuディレクトリ/スクリプト.py


## コンテナの移植
- コンテナの ubuntu をカスタマイズしたものを、ほかのマシンでも簡単に使えるようにするにはいくつか方法がある。
- （１）以下はコンテナから Docker イメージを作成する方法。
- 例えば、以下のコマンドで停止中のコンテナから Docker イメージを作成できる（リポジトリ名は新しくつける Docker イメージの名前のこと、タグ名を省略した場合は latest になる）：
$ docker commit コンテナ名 リポジトリ名:タグ名
- 例えば、以下のコマンドで作成した Docker イメージからコンテナを作る：
$ docker run -it リポジトリ名:タグ名 bash
- あとは DockerHub に push すればよいらしい。
- （２）以下はコンテナから tar ファイルを吐き出して読み込む方法。
- 例えば、以下のコマンドで停止中のコンテナを tar に吐き出しできる：
$ docker export コンテナ名 > test.tar
- 以下のコマンドで tar を読み込みできる（リポジトリ名は Docker イメージの名前のこと、タグ名を省略した場合は latest になる）：
$ cat test.tar | docker import - リポジトリ名:タグ名
- （３）ほかに Dockerfile から Docker イメージを build する方法があるが割愛。
