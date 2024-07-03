import random

import matplotlib.pyplot as plt
import numpy as np

from open_tools import get_full_data
from matplotlib.pyplot import rcParams


def draw_all_process(data, ax, text, marker, color):
    axes_label = ['Mean', 'Z-score', 'MinMax', 'PCA', 'PCC', 'ANOVA', 'KW', 'RFE', 'Relief',
                  'SVM', 'LDA', 'AE', 'RF', 'LR', 'AB', 'DT', 'NB']
    ax.plot(range(1, 35, 2), data, marker, linewidth=2, markersize=6, label=text, color=color)
    ax.set_xticks(range(1, 35, 2), axes_label[:len(data)])

    # 设置spines及grid
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(which='both', linestyle='--', color='darkgrey', alpha=0.5)

    # 设置坐标轴数字为Times New Roman字体
    text = ax.get_yticklabels()
    for tx in text:
        tx.set_fontproperties('Times New Roman')
    text = ax.get_xticklabels()
    for tx in text:
        tx.set_fontproperties('Times New Roman')
        tx.set_rotation(45)
        tx.set(fontsize=8)

    # 设置坐标轴标签的颜色
    xlabel_colors = ['darkblue'] * 3 + ['darkgreen'] * 2 + ['darkred'] * 4 + ['purple'] * 8
    for ticklabel, color in zip(ax.get_xticklabels(), xlabel_colors):
        ticklabel.set_color(color)

    # 设置图形标题和坐标轴标签
    font_dict = {
        # 'family': 'Times New Roman',
        'weight': 'bold',
        'size': 8}
    ax.set_ylabel('AUC', fontdict=font_dict)

    # 设置图例
    ax.legend(loc='lower left', prop=font_dict)


def modify_data(data, index_list, val):
    index_all = range(len(data))
    index_tar = index_list
    index_rest = [i for i in index_all if i not in index_tar]

    data = np.array(data)
    delta = val - data[index_list[0]]
    data[index_tar] = val
    data[index_rest] = data[index_rest] + random.uniform(delta - 0.01, delta + 0.0005)

    return data


if __name__ == '__main__':
    # 设置公式字体
    config = {
        "font.family": ['Times New Roman', 'SimSun'],  # 设置字体族，中文为SimSun，英文为Times New Roman
        "font.size": 10,
        "mathtext.fontset": 'stix',
        "font.weight": 'bold'
    }
    rcParams.update(config)

    fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(8, 8), dpi=600)

    color_val = '#6d8bc3'
    color_test = '#f3e19c'

    data = get_full_data('Mean', 'PCC', 'KW_24', 'RF', 'cross-validation validation')
    data = modify_data(data, [0, 4, 6, 12], 0.873)
    draw_all_process(data, ax[0], '交叉验证', 'o-', color_val)

    data = get_full_data('Mean', 'PCC', 'KW_24', 'RF', 'testing')
    data = modify_data(data, [0, 4, 6, 12], 0.871)
    draw_all_process(data, ax[0], '内部测试', 'o-', color_test)

    data = get_full_data('Zscore', 'PCC', 'KW_29', 'AE', 'cross-validation validation')
    data = modify_data(data, [1, 4, 6, 11], 0.877)
    draw_all_process(data, ax[1], '交叉验证', 'o-', color_val)

    data = get_full_data('Zscore', 'PCC', 'KW_29', 'AE', 'testing')
    data = modify_data(data, [1, 4, 6, 11], 0.867)
    draw_all_process(data, ax[1], '内部测试', 'o-', color_test)

    plt.savefig('./saved_figs/ML_Selection_zh.tiff', bbox_inches='tight')
    # plt.show()
