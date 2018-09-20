# ------------------
# モジュールインポート
# ------------------
import numpy as np
import lightgbm as lgb
from sklearn.datasets import load_boston, load_breast_cancer, load_diabetes, load_digits, load_iris, load_linnerud, load_wine
from sklearn.metrics import accuracy_score, mean_squared_error
from sklearn.model_selection import KFold, train_test_split


# ------------------
# 定数パラメータ設定
# ------------------

# データセット、タスク、評価関数
datasets = [
    (load_boston, 'regression', 'l2'),
    (load_breast_cancer, 'binary', 'binary_logloss'),
    (load_diabetes, 'regression', 'l2'),
    (load_digits, 'multiclass', 'multi_logloss'),
    (load_iris, 'multiclass', 'multi_logloss'),
    (load_linnerud, 'regression', 'l2'),
    (load_wine, 'multiclass', 'multi_logloss'),
]


# ------------------
#  メイン処理
# ------------------
def main():
    acc_list = []
    for data, task, metric in datasets:
        print(str(data))
        dataset = data()

        y = dataset['target']
        X = dataset['data']
        if data==load_linnerud:
            y = y[:, 0]

        # 学習データとテストデータ
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.33, random_state=0
        )

        # create dataset for lightgbm
        lgb_train = lgb.Dataset(X_train, y_train)
        lgb_eval = lgb.Dataset(X_test, y_test, reference=lgb_train)

        # LightGBM parameters
        params = {
                'task' : 'train',
                'boosting_type' : 'gbdt',
                'objective' : task,
                'metric' : {metric},
                'num_leaves' : 31,
                'min_data_in_leaf': 3,
                'learning_rate' : 0.1,
                'feature_fraction' : 0.9,
                'bagging_fraction' : 0.8,
                'bagging_freq': 5,
                'verbose' : -1,
        }
        if task=='multiclass':
            num_class = len(set(y))
            params['num_class'] = num_class
        
        # train
        gbm = lgb.train(params,
                    lgb_train,
                    num_boost_round=100,
                    valid_sets=lgb_eval,
                    early_stopping_rounds=10)
        y_pred = gbm.predict(X_test, num_iteration=gbm.best_iteration)

        # accuracy
        if task=='regression':
            acc = np.sqrt(sum((y_test-y_pred)**2)/len(y_pred))
        elif task=='multiclass':
            y_pred_max = np.argmax(y_pred, axis=1)  # 最尤と判断したクラスの値にする
            acc = sum(y_test == y_pred_max) / len(y_test)
        elif task=='binary':
            y_pred_th = np.where(y_pred>.5, 1, 0)  # 適当な閾値
            acc = sum(y_test == y_pred_th) / len(y_test)
        acc_list.append(acc)
    print(acc_list)


if __name__ == '__main__':
    main()