import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

from open_tools import open_specific_path


def draw_grouped_histogram(ax, species: list, data: dict, fig_title):
    keys = list(data.keys())
    vals = list(data.values())
    index = len(keys)
    x = np.arange(len(species))  # the label locations
    colors = ['#e3716e', '#eca680', '#f7df87']
    width = 0.25  # the width of the bars
    multiplier = 0

    for i in range(index):
        offset = width * multiplier
        ax.bar(x + offset, vals[i], width, label=keys[i], color=colors[i])
        multiplier += 1

    # Add some text for labels, title and custom x-axis tick labels, etc.
    font_dict = {
        'family': 'Times New Roman',
        'weight': 'bold',
        'size': 12}
    ax.set_ylabel('AUC', fontdict=font_dict)
    ax.set_xticks(x + width, species, fontdict=font_dict)

    font_dict['family'] = 'Microsoft YaHei'
    ax.set_title(fig_title, fontdict=font_dict)

    # 设置坐标轴数字为Times New Roman字体
    text = ax.get_yticklabels()
    for tx in text:
        tx.set_fontproperties('Times New Roman')

    ax.set_ylim(0, 1)
    ax.yaxis.set_major_locator(plt.MultipleLocator(0.1))
    ax.yaxis.set_minor_locator(plt.MultipleLocator(0.05))

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)


def add_fig_num(ax, num: str):
    # 在指定区域插入文本框
    param_dict = {
        's': num,
        'fontdict': {
            'family': 'Times New Roman',
            'size': 12,
            'weight': 'bold',
            'horizontalalignment': 'center',
            'verticalalignment': 'center'
        }}
    ax.text(-0.6, 0.95, **param_dict)


if __name__ == '__main__':
    # 设置公式字体
    config = {
        "font.family": 'serif',
        "font.size": 10,
        "mathtext.fontset": 'stix',
        "font.serif": ['SimSun']  # simsun字体中文版就是宋体
    }
    rcParams.update(config)
    # 建立公式样本
    sample = '$^{*}$'

    fig, ax = plt.subplots(figsize=(10, 10), dpi=300)

    # 训练集、交叉验证集及独立测试集
    source_1 = open_specific_path('Mean', 'PCC', 'Relief_32', 'RF')
    source_2 = open_specific_path('Zscore', 'PCC', 'Relief_32', 'RF')
    source_3 = open_specific_path('MinMax', 'PCC', 'Relief_32', 'RF')
    data_1 = {
        '训练集': (
            source_1['train_AUC'], source_2['train_AUC'], source_3['train_AUC']),
        '交叉验证集': (
            source_1['cross-validation validation'], source_2['cross-validation validation'],
            source_3['cross-validation validation']),
        '测试集': (source_1['testing'], source_2['testing'], source_3['testing'])
    }
    species = ['Mean' + sample, 'Z-score', 'MinMax']
    draw_grouped_histogram(ax, species, data_1, '数据归一化')
    add_fig_num(ax, 'A')
    # ax.legend(loc='upper left', ncols=1, prop={
    #     'family': 'Microsoft YaHei',
    #     'size': 10,
    #     'weight': 'bold'
    # })

    plt.savefig('./saved_figs/Figure 1.tiff', bbox_inches='tight')
    plt.show()
