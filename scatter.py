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
    # legend
    ax.legend()
    plt.show()
