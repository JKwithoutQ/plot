import matplotlib.pyplot as plt

ROWS = 2
COLS = 3

if __name__ == '__main__':

    fig, ax = plt.subplots(nrows=ROWS, ncols=COLS, subplot_kw=dict(projection="polar"))
    ((ax1, ax2, ax3), (ax4, ax5, ax6)) = ax
    for row in range(ROWS):
        for col in range(COLS):
            ax[row][col].set_title(f'{row * col}')
    plt.show()
