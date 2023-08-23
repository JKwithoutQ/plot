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
    """
    ax.scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, 
    vmax=None, alpha=None, linewidths=None, verts=None, edgecolors=None, hold=None, data=None, **kwargs)
    """
    ax.scatter(x, y, label='x')
    # plt.scatter(x, y, s, c, marker, cmap, norm, alpha, linewidths, edgecolorsl)
    # 参数说明：
    # x: x轴数据
    # y: y轴数据
    # s: 散点大小
    # c: 散点颜色
    # marker: 散点图形状
    # cmap: 指定某个colormap值, 该参数一般不用，用默认值
    # alpha: 散点的透明度
    # linewidths: 散点边界线的宽度
    # edgecolors: 设置散点边界线的颜色

    # legend
    ax.legend()
    plt.show()
