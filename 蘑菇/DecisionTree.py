import pymysql as pys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from  sklearn.linear_model import LogisticRegression


class DecitonTree(object):
    def __init__(self):
        try:
            conn = pys.connect(host='10.33.30.14', port=3306, user='oywm', password='oywm123', database='oywm_db',
                               charset='utf8')
            cursor = conn.cursor()
            sql = 'select * from mushroom'
            cursor.execute(sql)
            self.data = cursor.fetchall()
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            raise e

    def data_handle(self):
        data_list = []
        for data_line in self.data:
            data_list.append(list(data_line))

        df = pd.DataFrame(data_list)
        model_label = df[0].replace({"p": 1, "e": 0})
        model_dataset = pd.get_dummies(df.drop([0], axis=1))
        # print(model_dataset.info())
        # print(model_dataset)
        x_train, x_test, y_train, y_test = train_test_split(model_dataset, model_label, test_size=0.25, random_state=33)
        # print(x_train)
        # print(x_test.info())
        # 决策树
        # tr = DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=None,
        #                             max_features=None, max_leaf_nodes=None,
        #                             min_impurity_decrease=0.0, min_impurity_split=None,
        #                             min_samples_leaf=1, min_samples_split=2,
        #                             min_weight_fraction_leaf=0.0, presort=False, random_state=None,
        #                             splitter='best')
        #
        # tr.fit(x_train, y_train)
        # print(tr.score(x_test, y_test))

        # 逻辑回归
        lr = LogisticRegression()
        lr.fit(x_train, y_train)
        print(lr.get_params())
        test_results = lr.predict(x_test)
        # print(type(test_results))
        if list(test_results) == list(y_test.values):
            print('全部预测正确')
        else:
            print('很遗憾没有将全部的预测正确，正确率为：')
            print(lr.score(x_test, y_test))


def main():
    dt = DecitonTree()
    dt.data_handle()


if __name__ == '__main__':
    main()
