import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    x = np.random.randint(0, 10, 10)
    y = x
    fig, ax = plt.subplots()
    # title
    ax.set_title('plot')
    # label
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    # grid
    ax.grid()
    # plot
    ax.plot(x, y, color='g', linewidth=12.0, linestyle='-.', marker='*', label='x', alpha=0.2)
    # plt.plot(x, y, linestyle, linewidth, color, marker, markersize, markeredgecolor, markerfactcolor, label, alpha)
    # x：指定折线图的x轴数据；
    # y：指定折线图的y轴数据；
    # linestyle：指定折线的类型，可以是实线、虚线、点虚线、点点线等，默认文实线；
    # linewidth：指定折线的宽度
    # marker：可以为折线图添加点，该参数是设置点的形状；
    # markersize：设置点的大小；
    # markeredgecolor：设置点的边框色；
    # markerfactcolor：设置点的填充色；
    # label：为折线图添加标签，类似于图例的作用；
    # legend
    ax.legend()
    # plt.show()
    plt.savefig('./img/plot.png')
