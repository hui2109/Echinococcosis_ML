import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.legend_handler import HandlerTuple
from matplotlib.pyplot import rcParams
from sklearn.metrics import roc_curve, roc_auc_score


def draw_roc_curve(ax, y_true: list, y_score: list, title, legend=True):
    colors = ['#80a6e2', '#f46f43']
    labels = ['训练集', '独立测试集']
    roc_curves = []
    scatter_dots = []
    auc_labels = []

    for i in range(len(y_true)):
        fpr, tpr, thresholds = roc_curve(y_true[i], y_score[i], pos_label=1)
        auc = roc_auc_score(y_true[i], y_score[i])

        # 绘制ROC曲线
        auc_label = labels[i] + f'（AUC = {auc:.2f}）'
        auc_labels.append(auc_label)
        param_dict = {
            'color': colors[i],
            'lw': 2,
            'label': auc_label
        }
        roc_curves.append(ax.plot(fpr, tpr, zorder=2, **param_dict)[0])

        # 找到最靠近左上角的点并绘制 *
        distance = np.sqrt(fpr ** 2 + (1 - tpr) ** 2)
        closest_point_idx = np.argmin(distance)

        scatter_dots.append(
            ax.scatter(fpr[closest_point_idx] - 0.014, tpr[closest_point_idx], marker='$*$', color=colors[i], zorder=3))

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
            'weight': 'bold',
            'size': 12}
        ax.set_xlabel('假阳性率', fontdict=font_dict)
        ax.set_ylabel('真阳性率', fontdict=font_dict)
        ax.set_title(title, fontdict=font_dict)

        # 绘制辅助线
        param_dict = {
            'color': '#bbd1e7',
            'lw': 2,
            'linestyle': ':',
            'alpha': 0.5,
            'label': 'baseline',
        }
        baseline, = ax.plot([0, 1], [0, 1], **param_dict)

        ax.legend(
            [roc_curves[0], roc_curves[1],
             (scatter_dots[0], scatter_dots[1]),
             baseline],
            [auc_labels[0], auc_labels[1], '当前分类器', '基准线'],
            loc='lower right',
            prop={
                'size': 10,
                'weight': 'bold'},
            handler_map={tuple: HandlerTuple(ndivide=None)}
        )


def get_data(df1, df2):
    y_true_list = []
    y_score_list = []

    y_true_list.append(df1['Label'])
    y_true_list.append(df2['Label'])

    y_score_list.append(df1['Pred'])
    y_score_list.append(df2['Pred'])

    return y_true_list, y_score_list


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

    df_path1 = pd.read_csv(r'F:\数据\FAE\huis_data\results\results1_合并\Mean\PCC\KW_24\RF\cv_val_prediction.csv')
    df_path2 = pd.read_csv(r'F:\数据\FAE\huis_data\results\results2_合并\Mean\PCC\Relief_32\RF\test_prediction.csv')

    y_true_list, y_score_list = get_data(df_path1, df_path2)

    draw_roc_curve(ax, y_true_list, y_score_list, '')

    plt.savefig('./saved_figs/ROC_Curves_ML_RF_New.jpg', bbox_inches='tight')
    plt.show()
