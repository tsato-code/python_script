"""
target mean encoding の実装例
"""
# ------------------
# module
# ------------------
import pandas as pd


# ------------------
# constant parameters
# ------------------
a = {
	"cat1": ["a", "b", "a", "a", "c", "c", "c"],
	"cat2": ["A", "A", "B", "B", "B", "C", "C"],
	"numeric":  [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0],
	"label":    [1, 1, 1, 2, 2, 3, 3]
}


# ------------------
# def
# ------------------
def target_mean_encoding(df, src_col, tgt_col):
	""" target が数値のときに利用できる """
	target_mean = df.groupby(src_col)[tgt_col].mean().astype("float16")
	target_mean_df = df[src_col].map(target_mean).copy()
	target_mean_df.name = src_col+"_"+tgt_col+"_target_mean"
	return target_mean_df


def bin_counting(df, src_col, tgt_col):
    """ target がカテゴリのときに利用できる """
    cross_df         = pd.crosstab(df[src_col], df[tgt_col], normalize="index")
    labels           = [src_col+"_"+tgt_col+"_"+str(col) for col in cross_df.columns]
    cross_df.columns = labels
    bin_counting_df  = pd.merge(df, cross_df, left_on=src_col, right_index=True, how="left")
    return bin_counting_df[labels]


# ------------------
# main
# ------------------
def main():
	# データフレーム作成
	df = pd.DataFrame(a)
	# 集計対称となる列名を定義
	src = "cat1"
	tgt = "label"
	# target mean encoding
	target_mean_df = target_mean_encoding(df, src, tgt)
	df = pd.concat([df, target_mean_df], axis=1)
	# bin counting
	print("bin counting")
	print(df.select_dtypes('O').columns.tolist())

	bin_counting_df = bin_counting(df, src, tgt)
	df = pd.concat([df, bin_counting_df], axis=1)
	print(df)


if __name__=="__main__":
	main()


"""
$ python target_mean_encoding.py
cat1 cat2  numeric  label  cat1_label_target_mean  cat1_label_1  cat1_label_2  cat1_label_3
0    a    A      1.0      1                1.333333      0.666504      0.333252      0.000000
1    b    A      2.0      1                1.000000      1.000000      0.000000      0.000000
2    a    B      3.0      1                1.333333      0.666504      0.333252      0.000000
3    a    B      4.0      2                1.333333      0.666504      0.333252      0.000000
4    c    B      5.0      2                2.666667      0.000000      0.333252      0.666504
5    c    C      6.0      3                2.666667      0.000000      0.333252      0.666504
6    c    C      7.0      3                2.666667      0.000000      0.333252      0.666504
"""