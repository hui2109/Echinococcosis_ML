import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.legend_handler import HandlerTuple
from matplotlib.patches import Rectangle
from matplotlib.pyplot import rcParams
from sklearn.metrics import roc_curve, roc_auc_score


def draw_roc_curve(ax, y_true: list, y_score: list, title, legend=True):
    colors = ['#3b63e4', '#74aed4', '#bc02bb']
    labels = ['验证集', '内部测试集', '前瞻性测试集']
    roc_curves = []
    scatter_dots = []
    auc_labels = []

    if legend:
        delta = 0.01
    else:
        delta = 0.005

    for i in range(len(y_true)):
        fpr, tpr, thresholds = roc_curve(y_true[i], y_score[i], pos_label=1)
        auc = roc_auc_score(y_true[i], y_score[i])

        # 绘制ROC曲线
        auc_label = labels[i] + f' (AUC = {auc:.3f})'
        auc_labels.append(auc_label)
        param_dict = {
            'color': colors[i],
            'lw': 2,
            'label': auc_label
        }
        roc_curves.append(ax.plot(fpr, tpr, zorder=2, **param_dict)[0])

        # 找到最靠近左上角的点并绘制 *
        font_dict = {
            'family': 'Times New Roman',
            'weight': 'bold',
            'size': 10
        }
        distance = np.sqrt(fpr ** 2 + (1 - tpr) ** 2)
        closest_point_idx = np.argmin(distance)

        scatter_dots.append(
            ax.scatter(fpr[closest_point_idx] - delta, tpr[closest_point_idx], marker='$*$', color=colors[i], zorder=3))

    # 设置spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # 设置坐标轴数字为Times New Roman字体
    text = ax.get_yticklabels()
    for tx in text:
        tx.set_fontproperties('Times New Roman')
    text = ax.get_xticklabels()
    for tx in text:
        tx.set_fontproperties('Times New Roman')

    # 设置图例
    if legend:
        # 设置x轴和y轴范围及locator
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.xaxis.set_major_locator(plt.MultipleLocator(0.1))
        ax.xaxis.set_minor_locator(plt.MultipleLocator(0.05))
        ax.yaxis.set_major_locator(plt.MultipleLocator(0.1))
        ax.yaxis.set_minor_locator(plt.MultipleLocator(0.05))

        # 设置grid
        ax.grid(which='both', linestyle='--', color='darkgrey', alpha=0.5)

        # 设置图形标题和坐标轴标签
        font_dict = {
            # 'family': 'Times New Roman',
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

        ax.legend(
            [roc_curves[0], roc_curves[1], roc_curves[2],
             (scatter_dots[0], scatter_dots[1], scatter_dots[2]),
             baseline],
            [auc_labels[0], auc_labels[1], auc_labels[2], '当前分类器', '基准线'],
            loc='upper left',
            bbox_to_anchor=(-0.01, 1.1),
            ncols=2,
            prop={
                # 'family': 'Times New Roman',
                'size': 10,
                'weight': 'bold'},
            fancybox=True,
            frameon=False,
            framealpha=0.8,
            numpoints=1,
            handler_map={tuple: HandlerTuple(ndivide=None)}
        )


def my_read_csv(path):
    if type(path) == str:
        df = pd.read_csv(res_path)
        return df
    else:
        return path


def get_data(path1, path2, path3, path4='', path5='', path6='', path7='', path8='', path9=''):
    y_true_list = []
    y_score_list = []

    df1 = my_read_csv(path1)
    df2 = my_read_csv(path2)
    df3 = my_read_csv(path3)
    # df4 = my_read_csv(path4)
    # df5 = my_read_csv(path5)
    # df6 = my_read_csv(path6)
    # df7 = my_read_csv(path7)
    # df8 = my_read_csv(path8)
    # df9 = my_read_csv(path9)

    y_true_list.append(df1['Label'])
    y_true_list.append(df2['Label'])
    y_true_list.append(df3['Label'])
    # y_true_list.append(df4['Label'])
    # y_true_list.append(df5['Label'])
    # y_true_list.append(df6['Label'])
    # y_true_list.append(df7['Label'])
    # y_true_list.append(df8['Label'])
    # y_true_list.append(df9['Label'])

    y_score_list.append(df1['Score'])
    y_score_list.append(df2['Score'])
    y_score_list.append(df3['Score'])
    # y_score_list.append(df4['Score'])
    # y_score_list.append(df5['Score'])
    # y_score_list.append(df6['Score'])
    # y_score_list.append(df7['Score'])
    # y_score_list.append(df8['Score'])
    # y_score_list.append(df9['Score'])

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


def add_zoom_axes(ax, xy1, xy2):
    width, height = xy2[0] - xy1[0], xy2[1] - xy1[1]
    color = '#ee3023'
    box_width = 0.6
    box_height = 0.55

    rectangle_patch = Rectangle(xy1, width, height, fill=False, linestyle=':', color=color, zorder=6, lw=2)
    ax.add_patch(rectangle_patch)

    rectangle_patch_ins = Rectangle(
        (rectangle_patch.get_x() + rectangle_patch.get_width(), rectangle_patch.get_y() - box_height),
        box_width,
        box_height,
        fill=False, linestyle=':', color=color, zorder=6, lw=2)
    ax.add_patch(rectangle_patch_ins)

    # 添加局部放大的轴
    axins = ax.inset_axes(
        [rectangle_patch_ins.get_x() + 0.07,
         rectangle_patch_ins.get_y() + 0.05,
         rectangle_patch_ins.get_width() - 0.1,
         rectangle_patch_ins.get_height() - 0.08
         ],
        zorder=6, transform=ax.transData)

    # 设置x轴和y轴范围及locator
    axins.set_xlim(xy1[0], xy1[0] + width)
    axins.set_ylim(xy1[1], xy1[1] + height)
    axins.xaxis.set_major_locator(plt.MultipleLocator(0.05))
    axins.yaxis.set_major_locator(plt.MultipleLocator(0.05))

    # axins.set_facecolor("none")

    draw_roc_curve(axins, y_true_list, y_score_list, '', False)


if __name__ == '__main__':
    # 设置公式字体
    config = {
        "font.family": ['Times New Roman', 'SimSun'],  # 设置字体族，中文为SimSun，英文为Times New Roman
        "font.size": 10,
        "mathtext.fontset": 'stix',
        "font.weight": 'bold'
    }
    rcParams.update(config)

    fig, ax = plt.subplots(figsize=(10, 10), dpi=600)

    indices = ['ML_AE_val', 'ML_AE_test', 'ML_AE_inves']
    results_path_all = {
        'DL_inves': './resources/results/DL/inves_2022_mk.csv',
        'DL_test': './resources/results/DL/test.csv',
        'DL_val': './resources/results/DL/validation.csv',

        'ML_RF_inves': './resources/results/ML/Mean_PCC_KW_24_RF/inves_2023_mk.csv',
        'ML_RF_test': './resources/results/ML/Mean_PCC_KW_24_RF/random_test_results_mk.csv',
        'ML_RF_val': './resources/results/ML/Mean_PCC_KW_24_RF/random_val_results_mk.csv',

        'ML_AE_inves': './resources/results/ML/Zscore_PCC_KW_29_AE/inves_2023_mk.csv',
        'ML_AE_test': './resources/results/ML/Zscore_PCC_KW_29_AE/random_test_results_mk.csv',
        'ML_AE_val': './resources/results/ML/Zscore_PCC_KW_29_AE/random_val_results_mk.csv',

        'External_junior_E': './resources/results/External/junior_E/mk_2022_inves.csv',
        'External_junior_NE': './resources/results/External/junior_NE/mk_2022_inves.csv',

        'External_middle_E': './resources/results/External/middle_E/mk_2022_inves.csv',
        'External_middle_NE': './resources/results/External/middle_NE/mk_2022_inves.csv',

        'External_senior_E': './resources/results/External/senior_E/mk_2022_inves.csv',
        'External_senior_NE': './resources/results/External/senior_NE/mk_2022_inves.csv',
    }
    df_path1 = pd.read_csv('.' + results_path_all[indices[0]])
    df_path2 = pd.read_csv('.' + results_path_all[indices[1]])
    df_path3 = pd.read_csv('.' + results_path_all[indices[2]])

    y_true_list, y_score_list = get_data(df_path1, df_path2, df_path3)

    draw_roc_curve(ax, y_true_list, y_score_list, '')
    add_zoom_axes(ax, (0.1, 0.72), (0.25, 0.95))

    plt.savefig('./saved_figs/ML_AE_Zoom_zh.tiff', bbox_inches='tight')
    # plt.show()
