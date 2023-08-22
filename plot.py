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
    # legend
    ax.legend()
    # plt.show()
    plt.savefig('./img/plot.png')
