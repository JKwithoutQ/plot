import matplotlib.pyplot as plt
import numpy as np

# 中文乱码的处理
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 设置微软雅黑字体
plt.rcParams['axes.unicode_minus'] = False  # 避免坐标轴不能正常的显示负号

if __name__ == '__main__':
    x = np.random.randint(0, 10, 10)
    print(x)
    setting = {'fontsize': 18}
    fig, ax = plt.subplots()
    # figuresize=()
    # dpi=255
    # facecolor
    # edgecolor
    ax.plot(x, x, label='x')
    #
    ax.set_aspect('equal')
    # title
    ax.set_title('figure', **setting)
    # label
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    # grid
    ax.grid()
    # legend
    ax.legend()
    # ticks
    ax.set_xticks([0, 10], minor=True)
    ax.set_yticks([0, 5, 10], minor=True)
    # tick labels
    # ax.set_xticklabels(['1', '2', '3'])
    # ax.set_yticklabels(['1', '2', '3'])
    # x limit
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    # plot
    plt.show()
    # 图表动态刷新：plt.ion()和plt.ioff()
