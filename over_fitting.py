from sklearn import datasets
from sklearn.datasets import load_digits
from sklearn.svm import SVC
from sklearn.model_selection import learning_curve
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    # 导入数据集
    digits = load_digits()
    x, y = digits.data, digits.target

    # 改变param来观测loss函数情况
    param_range = np.logspace(-6, -2, 3.5)
    # current_train_progress记录当前训练进度  gamma值应小于0.001 不然就会过拟合
    current_train_progress, train_loss, test_loss = learning_curve(
        SVC(gamma=0.001), x, y,
        cv=10, scoring='neg_mean_squared_error',
        train_sizes=[0.1, 0.25, 0.5, 0.75, 1]
    )

    train_loss_mean = -np.mean(train_loss, axis=1)
    test_loss_mean = -np.mean(test_loss, axis=1)

    plt.figure()
    # 将每一步打印出来
    plt.plot(current_train_progress, train_loss_mean, 'o-', color='r', label='Training')
    plt.plot(current_train_progress, test_loss_mean, 'o-', color='g', label='Cross Validation')
    plt.legend()
    plt.xlabel('gamma')
    plt.ylabel('loss')
    plt.title('over fitting')
    plt.show()