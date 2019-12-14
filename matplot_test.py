#!/usr/bin/env python
# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.axes3d import Axes3D
import matplotlib

# 折线图
def plot_test():
    x = np.arange(9)
    x = range(20)
    x = np.arange(0, 40, 2)
    y = np.sin(x)
    y = np.random.randint(1, 100, size=20)
    z = np.cos(x)
    # marker数据点样式 线宽 线型 颜色
    plt.plot(x, y, marker="*", linewidth=3, linestyle='-', color='orange')
    plt.title("热门微博的评论数量")
    plt.xlabel('x')
    plt.ylabel('y')
    # 设置图例
    plt.legend(['Y', 'Z'], loc='upper right')
    plt.grid()
    plt.show()

# 散点图
def scatter_test():
    # 正态分布的 10个小于1的数字
    x = np.random.randint(1, 100, size=100)
    y = np.random.randint(1, 100, size=100)
    plt.scatter(x, y)
    plt.show()

# 柱状图
def bar_test():
    x = np.arange(10)
    y = np.random.randint(0, 30, 10)
    plt.bar(x, y)
    plt.show()

# 饼图
def pie_test():
    x = np.random.randint(1, 10, 6)
    plt.pie(x)
    plt.show()

# 直方图
def hist_test():
    x = 0 + 1 * np.random.randn(10000)
    plt.hist(x, bins=50)
    plt.show()

# 子图
def subplot_test():
    # figsize绘图对象的宽和高 dpi绘图对象的分辨率
    plt.figure(figsize=(8, 6), dpi=100)
    a = plt.subplot(2, 2, 1)
    plt.plot([0, 1], [0, 1], color="red")

    plt.subplot(2, 2, 2)
    plt.title('B')
    plt.plot([0, 1], [0, 1], color="green")

    plt.subplot(2, 1, 2)
    plt.title('C')
    plt.plot(np.arange(10), np.random.rand(10), color="orange")

    # 选择子图
    plt.sca(a)
    plt.title('A')
    plt.show()

# 正弦曲线
def sin_test():
    x = np.arange(-np.pi, np.pi, 0.1)   #开始值 结束值 步长
    y = np.sin(x)
    # 画布大小
    plt.figure(figsize=(5, 5))
    # 设置网格线y轴 默认是xy都有
    plt.grid(axis='y', color='red')
    # 设置x轴标签的内容样式
    plt.xlabel('xxx',color='red',fontsize=20,rotation=20)
    plt.ylabel('yyy',rotation=90)
    # 设置图例 也可以在plot里 label属性设置
    plt.legend(['AAA','BBB'], loc='upper right')

    plt.plot(x, y)
    plt.show()

# 画圆
def cicle_test():
    # 绘制图形
    x = np.linspace(-1, 1, 100)
    print(x)
    y = (1 - x**2) **0.5
    plt.plot(x, y, color='red')
    plt.plot(x, -y, color='green')
    # x轴起始值 x轴结束值 y轴
    plt.axis([-2,2,-2,2])
    # 也可以单独设置x 和y的起始 结束值
    plt.xlim([-3, 3])
    plt.ylim([-2, 2])
    plt.show()

# 直方图
def i():
    data = np.random.randint(0,100,size=100)
    plt.hist(data, bins=10, density=True, color='red')
    plt.show()

# 饼图
def j():
    x = [89, 45, 32, 16]
    plt.pie(x, labels=['A', 'B', 'C', 'D'],
            labeldistance=1.2,
            autopct='%1.1f%%',  #保留一位小数的百分比
            pctdistance=0.5,
            explode=[0, 0.2, 0, 0],
            colors=['red','blue','yellow','green'],
            shadow=True,
            startangle=60
            )
    plt.title('haha华为')
    # 设置图例
    plt.legend(['A', 'B', 'C', 'D'], loc='best')
    plt.grid()
    plt.show()

# 散点图
def k():
    x = np.random.normal(loc=0, scale=1, size=1000)
    y = np.random.normal(loc=0, scale=1, size=1000)
    print(x)
    plt.scatter(x, y)
    plt.scatter(x, y, s=[30, 100], c=[(1, 0, 0), (0, 1, 0), (0, 0, 1)], marker="o", alpha=0.8)
    plt.show()

# 画3d图
def m():
    axes = plt.subplot(projection='3d')
    plt.show()

def n():
    # 设置matplotlib正常显示中文
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
    phone_average_price = [1000,2000,3000,4000]
    value = [1,2,3,4,5,6,7,8,9,10]
    key = ['a','b','c','d','e','f','g','h','i','j']
    # 画饼图
    plt.pie(value,        #要显示的列表
            labels=key,     #每个地区的标签
            labeldistance=1.2,          #标签距离圆心
            autopct='%1.1f%%',          #保留一位小数的百分比
            pctdistance=0.5,
            explode=[0, 0, 0, 0, 0, 0, 0.2, 0,0,0],
            # colors=['red','blue','yellow','green', 'orange', 'antiquewhite', 'aquamarine', 'hotpink'], #每个地区的颜色
            shadow=True,
            startangle=60               #起始角度
            )
    plt.text(1, 1, 'hhhhhhhhhhhhhhhh')
    plt.title('Average Price of Mobile Phones in Taobao')
    # 设置图例
    plt.legend(['iphoneX', 'HuaweiP30', 'OnePlus6', 'Xiaomi9'], loc='upper right')
    plt.grid()
    plt.show()

def x():
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
    phone_name_list = ['iphoneX', '华为P30', 'OnePlus6', 'Xiaomi9']
    phone_total_sells = [164,170,150,220]
    # 画柱状图
    k = [4435.23423,3942.32525,2316.325235,2489.1224]
    plt.bar(phone_name_list[0], k[0], color='r',  alpha=0.6)
    plt.bar(phone_name_list[1], k[1], color='g',  alpha=0.6)
    plt.bar(phone_name_list[2], k[2], color='b',  alpha=0.6)
    plt.bar(phone_name_list[3], k[3], color='y',  alpha=0.6)
    # 设置标题
    plt.title('淘宝4大热销手机')
    # 设置图例
    plt.text(-0.3,0,k[0])
    plt.text(0.7,1,k[1])
    plt.text(1.7,2,k[2])
    plt.text(2.7,3,k[3])
    # 显示横轴标签
    plt.xlabel("手机平均价格")
    # 显示纵轴标签
    plt.ylabel("手机型号")
    # 设置图例
    plt.legend(phone_name_list, loc='best')

    plt.show()

def q():
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
    key = ['武汉','长沙','厦门','ww','ww','武汉','武汉']
    plt.hist(key, bins=4, facecolor="yellow", edgecolor="black", alpha=0.7)
    plt.text(0.2,3.05,1000)
    plt.text(1,1.1,2000)
    plt.text(1.8,1.1,3000)
    plt.text(2.5,2.1,4000)
    # 显示横轴标签
    plt.xlabel("地区")
    # 显示纵轴标签
    plt.ylabel("分布情况")
    # 显示图标题
    plt.title("淘宝4大热销手机的地区分布")
    plt.show()

def w():
    k = [1,2,3,4,1,1,2]
    # 直方图
    plt.hist(k, bins=len(k),
             facecolor="yellow", edgecolor="black", alpha=0.7)
    plt.show()

def main():

if __name__ == '__main__':
    main()
