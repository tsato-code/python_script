@echo off
rem ここはコメント
: ここもコメント
rem 文字コードをutf-8に変更
chcp 65001
echo hoge
echo 0123
echo ふが

python -c print('piyo')
python -c print('ぴよん')

rem 文字コードをshift-jisに戻す
rem chcp 932

: >sample.bat
: Active code page: 65001
: hoge
: 0123
: ふが
: piyo
: ぴよん
