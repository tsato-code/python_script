# ------------------
# モジュールインポート
# ------------------
import copy


# ------------------
# 定数パラメータ設定
# ------------------
SIZE = 16


# ------------------
# 関数の定義
# ------------------
def make_orthogonal_array(size=16):
    """ 直交表の生成 """
    A = [[0],[1]]
    while len(A) < size:
        newA = []
        for a in A:
            newA.append(copy.deepcopy(a))
            newA.append(copy.deepcopy(a))
        for i, a in enumerate(newA):
            if i%2==0:
                a.append(0)
            else:
                a.append(1)
        for a in newA:
            a += [i^a[-1] for i in a[:-1]]
        A = newA
    return A


# ------------------
#  メイン処理
# ------------------
def main():
    # 直交表の生成
    A = make_orthogonal_array(SIZE)
    for a in A:
        print(a)


if __name__ == '__main__':
    main()


"""
> python make_orthogonal_array.py
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
[0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1]
[0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]
[0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]
[0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0]
[0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0]
[0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1]
[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
[1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0]
[1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0]
[1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1]
[1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0]
[1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1]
[1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1]
[1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0]
"""