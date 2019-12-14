'''
模型的保存和导入
knn模型训练
使用k折交叉验证
'''
from sklearn import svm
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, cross_val_score
import pickle
import sklearn
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # 导入iris鸢尾花数据集  4个特征变量
    iris = datasets.load_iris()
    # 输入特征 label
    x, y = iris.data, iris.target
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(
                                                x, y, test_size=0.3)
    score_list = list()
    neighbors_range = range(1, 31)
    for k in neighbors_range:
        # 训练数据  邻近点方式训练数据  选择邻近的k个点
        knn = sklearn.neighbors.KNeighborsClassifier(n_neighbors=k)  #引入训练方法(也就是模型)
        # 拟合  进行训练
        knn.fit(x_train, y_train)
        # 评分方式为accuracy  分为5组
        score = cross_val_score(knn, x, y, cv=5, scoring='accuracy')
        print('5次打分： {}\n平均分: {}'.format(score, score.mean()))
        score_list.append(score.mean())
    plt.figure()
    plt.plot(neighbors_range, score_list)
    plt.title('knn')
    plt.xlabel('Value of n_neighbors for KNN')
    plt.ylabel('CrossValidation accuracy')
    plt.show()

    # 保存模型
    with open('knn.pickle', 'wb') as f:
        pickle.dump(knn, f)

    # 导入模型
    with open('knn.pickle', 'rb') as f:
        knn = pickle.load(f)
        print('预测： ', knn.predict(x_test))
        print('真实值： ', y_test)

    from sklearn.externals import joblib
    # 保存模型 和 导入模型的第二种方法
    # joblib.dump(knn, 'knn.pkl')
    # knn = joblib.load('knn.pkl')
    # print(knn.predict(x[0:1]))