'''
数据预处理包括：降维 数据归一化 特征提取和特征转换
'''
from sklearn import preprocessing
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets.samples_generator import make_classification
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import sklearn

if __name__ == '__main__':
    # 生成数据集
    x, y = sklearn.datasets.samples_generator.make_classification(
                               n_samples=300, n_features=2, n_redundant=0,
                               n_informative=2, random_state=22,
                               n_clusters_per_class=1, scale=100)
    # 把输入特征scale 缩放 因为有些特征没有接近标准正态分布 表现的性能不好
    x = sklearn.preprocessing.scale(x)
    # 把数据集划分成 训练集 和 测试集 0.7:0.3
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
    # svm模型
    clf = sklearn.svm.SVC()
    # 拟合 训练
    clf.fit(x_train, y_train)
    # 预测
    print(clf.score(x_test, y_test))
    # print(y)

    # 点的坐标x y就是输入特征的两个值 对应label为0是一个颜色 为1是另一个颜色 实现了分类
    plt.scatter(x[:, 0], x[:, 1], c=y)
    plt.show()

    # 每一行代表一个属性
    a = np.array([[10, 2.7, 3.6],
                  [-100, 5, -2],
                  [120, 20, 40]], dtype=np.float64)
    # 标准化之前 和 标准化之后
    print(a)
    print(preprocessing.scale(a))