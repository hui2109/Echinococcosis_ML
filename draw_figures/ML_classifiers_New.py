import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams


def draw_grouped_histogram(ax, species: list, data: dict, fig_title):
    keys = list(data.keys())
    vals = list(data.values())
    index = len(keys)
    x = np.arange(len(species))  # the label locations
    colors = ['#80a6e2', '#f46f43']
    width = 0.25  # the width of the bars
    multiplier = 0

    for i in range(index):
        offset = width * multiplier
        ax.bar(x + offset, vals[i], width, label=keys[i], color=colors[i])
        multiplier += 1

    # Add some text for labels, title and custom x-axis tick labels, etc.
    font_dict = {
        'weight': 'bold',
        'size': 12}
    ax.set_ylabel('AUC', fontdict=font_dict)
    ax.set_xticks(x + width/2, species, fontdict=font_dict)
    ax.set_xlabel('分类器', fontdict=font_dict)
    ax.set_title(fig_title, fontdict=font_dict)

    # 设置grid
    ax.grid(which='both', linestyle='--', color='darkgrey', alpha=0.5)

    # 设置坐标轴数字为Times New Roman字体
    text = ax.get_yticklabels()
    for tx in text:
        tx.set_fontproperties('Times New Roman')

    ax.set_ylim(0, 0.9)
    ax.yaxis.set_major_locator(plt.MultipleLocator(0.1))
    ax.yaxis.set_minor_locator(plt.MultipleLocator(0.05))

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.legend(loc='upper right', ncols=1, prop={
        'size': 10,
        'weight': 'bold'
    })


if __name__ == '__main__':
    # 设置公式字体
    config = {
        "font.family": ['Times New Roman', 'SimSun'],  # 设置字体族，中文为SimSun，英文为Times New Roman
        "font.size": 10,
        "mathtext.fontset": 'stix',
        "font.weight": 'bold'
    }
    rcParams.update(config)

    fig, ax = plt.subplots(figsize=(10, 10), dpi=300)

    species = ['SVM', 'AE', 'LDA', 'RF', 'LR', 'AB', 'DT', 'NB']
    data = {
        "训练集": (
            0.7625, 0.7801, 0.759, 0.8246, 0.7567, 0.7695, 0.616, 0.7141
        ),
        "独立测试集": (
            0.7873, 0.8292, 0.7949, 0.8555, 0.7856, 0.7862, 0.6953, 0.7508
        ),
    }
    draw_grouped_histogram(ax, species, data, '')
    plt.savefig('./saved_figs/ML_classifiers_New.jpg', bbox_inches='tight')
    plt.show()

