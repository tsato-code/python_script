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
	"category": ["a", "b", "a", "a", "c", "c", "c"],
	"label":    [1, 1, 1, 2, 2, 3, 3]
}


# ------------------
# def
# ------------------
def target_mean_encoding(df, colname):
	label_mean = df.groupby(colname).label.mean()
	label_mean_col = df[colname].map(label_mean).copy()
	return label_mean_col


# ------------------
# main
# ------------------
def main():
	df = pd.DataFrame(a)
	target = "category"
	label_mean_col = target_mean_encoding(df, target)
	df = df.assign(**{target+"_tgt_mean": label_mean_col})
	print(df)


if __name__=="__main__":
	main()


"""
$ python target_mean_encoding.py
  category  label  category_tgt_mean
0        a      1           1.333333
1        b      1           1.000000
2        a      1           1.333333
3        a      2           1.333333
4        c      2           2.666667
5        c      3           2.666667
6        c      3           2.666667
"""