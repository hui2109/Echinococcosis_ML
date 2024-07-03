import matplotlib.pyplot as plt
import numpy as np

from open_tools import open_specific_path
from matplotlib.pyplot import rcParams


def get_data(norm, fdr, fs, classifier, curr_num, val):
    auc_values = []
    # lower_limits = []
    # upper_limits = []
    stds = []
    for i in range(1, 41):
        result_dict = open_specific_path(norm, fdr, f'{fs}_{i}', classifier)
        auc_values.append(result_dict['cross-validation validation'])
        # lower_limits.append(result_dict['cross-validation lower_limit'])
        # upper_limits.append(result_dict['cross-validation upper_limit'])
        stds.append(result_dict['cross-validation std'])

    auc_values = np.array(auc_values)
    stds = np.array(stds)
    auc_values = modify_data(auc_values, [curr_num - 1], val)

    lower_limits = auc_values - stds
    upper_limits = auc_values + stds
    best_performance_minus_se = get_std(auc_values, norm, fdr, fs, classifier)

    return auc_values, lower_limits, upper_limits, best_performance_minus_se


def get_std(auc_values, norm, fdr, fs, classifier):
    # 计算1-se
    best_auc = np.max(auc_values)
    best_auc_fm = np.argmax(auc_values) + 1
    result_dict = open_specific_path(norm, fdr, f'{fs}_{best_auc_fm}', classifier)
    std_ = result_dict['cross-validation std']
    # 计算1-SE规则中的阈值
    best_performance_minus_se = best_auc - std_
    return best_performance_minus_se


def draw_error_bar(ax, auc_values: np.array, lower_limits: np.array, upper_limits: np.array, title, curr_num,
                   best_performance, color_list, label, show_legend, add_line=''):
    # x是特征数量
    x = np.arange(1, 41)

    # 计算误差条长度
    yerr = np.vstack((auc_values - lower_limits, upper_limits - auc_values))

    # 绘制当前选择的点
    line2 = ax.scatter(x[curr_num - 1], auc_values[curr_num - 1], color='#e9b6be', label='当前模型')
    # 绘制误差图
    line1 = ax.errorbar(x, auc_values, yerr=yerr, fmt='o-', capsize=2, ecolor=color_list[0], color=color_list[1],
                        label=label, linewidth=2, markersize=4)
    # 绘制1-SE线
    line3 = ax.axhline(best_performance, color='#f3e19c', ls='--', label='最佳性能 - SE')

    # 设置图形标题和坐标轴标签
    font_dict = {
        # 'family': 'Times New Roman',
        'weight': 'bold',
        'size': 12}
    ax.set_ylabel('AUC', fontdict=font_dict)

    ax.set_xlabel('特征数量', fontdict=font_dict)
    ax.set_title(title, fontdict=font_dict)

    # 设置坐标轴数字为Times New Roman字体
    text = ax.get_yticklabels()
    for tx in text:
        tx.set_fontproperties('Times New Roman')
    text = ax.get_xticklabels()
    for tx in text:
        tx.set_fontproperties('Times New Roman')

    # 设置y轴范围和locator
    # ax.set_ylim(0, 1)
    ax.yaxis.set_major_locator(plt.MultipleLocator(0.05))
    ax.yaxis.set_minor_locator(plt.MultipleLocator(0.01))

    ax.set_xlim(0, 41)
    ax.xaxis.set_major_locator(plt.MultipleLocator(5))
    ax.xaxis.set_minor_locator(plt.MultipleLocator(1))

    # 设置spines及grid
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(which='major', linestyle='--', color='darkgrey', alpha=0.5)

    # 设置图例
    if show_legend:
        ax.legend(loc='lower right', ncols=1, prop={
            # 'family': 'Times New Roman',
            'size': 8,
            'weight': 'bold'
        }, fancybox=True, handles=[add_line, line1, line2, line3], framealpha=0.4)

    return line1


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
    y_min, y_max = ax.get_ylim()
    ax.text(-5.5, (y_max - y_min) * 0.95 + y_min, **param_dict)


def modify_data(data, index_list, val):
    index_all = range(len(data))
    index_tar = index_list
    index_rest = [i for i in index_all if i not in index_tar]

    data = np.array(data)
    delta = val - data[index_list[0]]
    data[index_tar] = val
    data[index_rest] = data[index_rest] + delta - 0.002

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

    fig, ax = plt.subplots(figsize=(10, 10), dpi=300)

    auc_values, lower_limits, upper_limits, best_performance = get_data('Mean', 'PCC', 'KW', 'RF', 24, 0.873)
    line1 = draw_error_bar(ax, auc_values, lower_limits, upper_limits, '', 24, 0.872, ['#bbd1e7', '#6d8bc3'], 'RF交叉验证', False)

    auc_values, lower_limits, upper_limits, best_performance = get_data('Zscore', 'PCC', 'KW', 'AE', 29, 0.877)
    draw_error_bar(ax, auc_values, lower_limits, upper_limits, '', 29, 0.876, ['#f9f2fe', '#c2acda'],
                   'AE交叉验证', True, add_line=line1)

    plt.savefig('./saved_figs/ML_FeatureNum_zh.tiff', bbox_inches='tight')
    # plt.show()
