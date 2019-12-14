from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # 导入数据集
    loaded_data = datasets.load_boston()
    # 输入特征 和 对应label
    data_x = loaded_data.data     #506 * 13
    data_y = loaded_data.target   #506

    # 线性回归模型
    model = LinearRegression()
    # 拟合
    model.fit(data_x, data_y)

    # 推理 预测值
    print(model.predict(data_x[:4, :]))
    print(data_y[:4])

    # 随机生成一个数据集
    # n_samples样本数目  n_features特征数目  n_targets真实值数目 noise噪音
    x, y = datasets.make_regression(n_samples=100, n_features=1, n_targets=1, noise=10)
    # 滑散点图
    plt.scatter(x, y)
    plt.show()

    # 参数  如果y=0.1x + 0.3(w*x + b)
    print('w: ', model.coef_)  #这行是0.1
    print('b: ', model.intercept_)  #这行是0.3
    print('模型参数: ', model.get_params())  #模型定义时定义的参数 没有定义返回默认值
    print('score: ', model.score(data_x, data_y))  #给训练模型打分
