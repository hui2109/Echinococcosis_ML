import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

from open_tools import open_specific_path


def draw_grouped_histogram(ax, species: list, data: dict, x_title):
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
    ax.set_xlabel(x_title, fontdict=font_dict)
    ax.set_ylabel('AUC', fontdict=font_dict)
    ax.set_xticks(x + width / 2, species, fontdict=font_dict)

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

    ax.legend(
        loc='upper left',
        ncols=1,
        prop={
            'size': 10,
            'weight': 'bold'
        })


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
        "font.family": ['Times New Roman', 'SimSun'],  # 设置字体族，中文为SimSun，英文为Times New Roman
        "font.size": 10,
        "mathtext.fontset": 'stix',
        "font.weight": 'bold'
    }
    rcParams.update(config)

    fig, ax = plt.subplots(figsize=(10, 10), dpi=300)

    # 训练集及独立测试集
    source_1_Train = open_specific_path('Mean', 'PCC', 'ANOVA_24', 'RF')
    source_2_Train = open_specific_path('Mean', 'PCC', 'Relief_24', 'RF')
    source_3_Train = open_specific_path('Mean', 'PCC', 'RFE_24', 'RF')
    source_4_Train = open_specific_path('Mean', 'PCC', 'KW_24', 'RF')

    source_1_Test = open_specific_path('Mean', 'PCC', 'ANOVA_32', 'RF', 'better')
    source_2_Test = open_specific_path('Mean', 'PCC', 'KW_32', 'RF', 'better')
    source_3_Test = open_specific_path('Mean', 'PCC', 'RFE_32', 'RF', 'better')
    source_4_Test = open_specific_path('Mean', 'PCC', 'Relief_32', 'RF', 'better')

    data_1 = {
        '训练集': (
            source_1_Train['cross-validation validation'], source_2_Train['cross-validation validation'],
            source_3_Train['cross-validation validation'], source_4_Train['cross-validation validation']),
        '独立测试集': (source_1_Test['testing'], source_2_Test['testing'], source_3_Test['testing'], source_4_Test['testing'])
    }
    species = ['ANOVA', 'KW', 'RFE', 'Relief']
    draw_grouped_histogram(ax, species, data_1, '特征筛选')

    plt.savefig('./saved_figs/Feature_selection_New.jpg', bbox_inches='tight')
    plt.show()
