import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
from matplotlib.legend_handler import HandlerTuple
from sklearn.metrics import roc_curve, roc_auc_score

from open_tools import open_specific_prediction_file


def draw_roc_curve(ax, y_true: list, y_score: list, title):
    colors = ['#f7df87', '#eca680', '#e3716e']
    labels = ['训练集', '交叉验证集', '独立测试集']
    roc_curves = []
    scatter_dots = []
    auc_labels = []
    for i in range(len(y_true)):
        fpr, tpr, thresholds = roc_curve(y_true[i], y_score[i], pos_label=1)
        auc = roc_auc_score(y_true[i], y_score[i])

        # 绘制ROC曲线
        auc_label = labels[i] + f' (AUC = {auc:.2f})'
        auc_labels.append(auc_label)
        param_dict = {
            'color': colors[i],
            'lw': 2,
            'marker': '.',
            'label': auc_label
        }
        roc_curves.append(ax.plot(fpr, tpr, **param_dict)[0])

        # 找到最靠近左上角的点并绘制*
        font_dict = {
            'family': 'Times New Roman',
            'weight': 'bold',
            'size': 10
        }
        distance = np.sqrt(fpr ** 2 + (1 - tpr) ** 2)
        closest_point_idx = np.argmin(distance)
        if i == 0:
            scatter_dots.append(ax.scatter(fpr[closest_point_idx] + 0.02, tpr[closest_point_idx] - 0.02, marker='$*$', color=colors[i]))
        else:
            scatter_dots.append(ax.scatter(fpr[closest_point_idx] - 0.02, tpr[closest_point_idx], marker='$*$', color=colors[i]))

    # 设置spines及grid
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(which='both', linestyle='--', color='darkgrey', alpha=0.5)

    # 设置x轴和y轴范围及locator
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.xaxis.set_major_locator(plt.MultipleLocator(0.1))
    ax.yaxis.set_major_locator(plt.MultipleLocator(0.1))
    ax.xaxis.set_minor_locator(plt.MultipleLocator(0.05))
    ax.yaxis.set_minor_locator(plt.MultipleLocator(0.05))

    # 设置坐标轴数字为Times New Roman字体
    text = ax.get_yticklabels()
    for tx in text:
        tx.set_fontproperties('Times New Roman')
    text = ax.get_xticklabels()
    for tx in text:
        tx.set_fontproperties('Times New Roman')

    # 设置图形标题和坐标轴标签
    font_dict = {
        'family': 'Microsoft YaHei',
        'weight': 'bold',
        'size': 12}
    ax.set_xlabel('假阳性率', fontdict=font_dict)
    ax.set_ylabel('真阳性率', fontdict=font_dict)
    ax.set_title(title, fontsize=10, fontdict=font_dict)

    # 绘制辅助线
    param_dict = {
        'color': '#7ac7e2',
        'lw': 2,
        'linestyle': ':',
        'alpha': 0.5,
        'label': 'baseline',
    }
    baseline, = ax.plot([0, 1], [0, 1], **param_dict)

    # 设置图例
    ax.legend(
        [roc_curves[0], roc_curves[1], roc_curves[2], (scatter_dots[0], scatter_dots[1], scatter_dots[2]), baseline],
        [auc_labels[0], auc_labels[1], auc_labels[2], '当前分类器', '基线'],
        loc='lower right',
        ncols=1,
        # prop={
        #     'family': 'Times New Roman',
        #     'size': 10,
        #     'weight': 'bold'},
        fancybox=True,
        framealpha=0.8,
        numpoints=1,
        handler_map={tuple: HandlerTuple(ndivide=None)}
    )


def get_data(norm1, fdr1, fs_nums_feature1, classifier1, prediction_file1, norm2, fdr2,
             fs_nums_feature2, classifier2, prediction_file2, norm3, fdr3, fs_nums_feature3, classifier3,
             prediction_file3):
    y_true_list = []
    y_score_list = []
    y_true1, y_score1 = open_specific_prediction_file(norm1, fdr1, fs_nums_feature1, classifier1, prediction_file1)
    y_true2, y_score2 = open_specific_prediction_file(norm2, fdr2, fs_nums_feature2, classifier2, prediction_file2,
                                                      root_path=r'G:\FAE\huis_data\results\results1_合并')
    y_true3, y_score3 = open_specific_prediction_file(norm3, fdr3, fs_nums_feature3, classifier3, prediction_file3)
    y_true_list.append(y_true1)
    y_true_list.append(y_true2)
    y_true_list.append(y_true3)
    y_score_list.append(y_score1)
    y_score_list.append(y_score2)
    y_score_list.append(y_score3)

    return y_true_list, y_score_list


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
    x_min, x_max = ax.get_xlim()
    ax.text((x_min - x_max) * 0.12, (y_max - y_min) * 0.95 + y_min, **param_dict)


if __name__ == '__main__':
    # 设置公式字体
    # config = {
    #     "font.family": 'Times New Roman',
    #     "font.size": 10,
    #     "mathtext.fontset": 'stix',
    #     "font.serif": ['SimSun'],  # simsun字体中文版就是宋体
    #     "font.weight": 'bold'
    # }
    # rcParams.update(config)
    plt.rcParams['font.family'] = ['Times New Roman', 'Microsoft YaHei']  # 设置字体族，中文为SimSun，英文为Times New Roman

    fig, ax = plt.subplots(figsize=(8, 8), dpi=600)

    y_true_list, y_score_list = get_data(
        'Mean', 'PCC', 'Relief_19', 'RF', 'train_prediction.csv',
        'Mean', 'PCC', 'KW_24', 'RF', 'cv_val_prediction.csv',
        'Mean', 'PCC', 'Relief_32', 'RF', 'test_prediction.csv'
    )
    draw_roc_curve(ax, y_true_list, y_score_list, '不同数据集中最佳模型的ROC曲线')

    plt.savefig('./saved_figs/Figure 6.tiff', bbox_inches='tight')
    plt.show()
