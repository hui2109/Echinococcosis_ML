from pathlib import Path

import numpy as np
import pandas as pd
import scipy.stats as stats
from sklearn.metrics import confusion_matrix, f1_score

from draw_figures.open_tools import CalculateAUC


def clopper_pearson(successes, trials):
    alpha = 0.05
    lower = stats.beta.ppf(alpha / 2, successes, trials - successes + 1)
    upper = stats.beta.ppf(1 - alpha / 2, successes + 1, trials - successes)
    return lower, upper


def normal_approximation(successes, trials):
    z = 1.96
    p = successes / trials if trials != 0 else 0
    interval = z * np.sqrt(p * (1 - p) / trials) if trials != 0 else 0
    return max(0, p - interval), min(1, p + interval)


def compute_CI(tn, fp, fn, tp, method='clopper_pearson'):
    if method == 'clopper_pearson':
        sensitivity_CI = clopper_pearson(tp, tp + fn)
        specificity_CI = clopper_pearson(tn, tn + fp)
        accuracy_CI = clopper_pearson(tp + tn, tp + tn + fp + fn)
        ppv_CI = clopper_pearson(tp, tp + fp)
        npv_CI = clopper_pearson(tn, tn + fn)
    else:
        sensitivity_CI = normal_approximation(tp, tp + fn)
        specificity_CI = normal_approximation(tn, tn + fp)
        accuracy_CI = normal_approximation(tp + tn, tp + tn + fp + fn)
        ppv_CI = normal_approximation(tp, tp + fp)
        npv_CI = normal_approximation(tn, tn + fn)
    return sensitivity_CI, specificity_CI, accuracy_CI, ppv_CI, npv_CI


def get_diagnosis_performance(res_path, method='clopper_pearson'):
    if isinstance(res_path, pd.DataFrame):
        df = res_path
    else:
        df = pd.read_csv(res_path)
    y_true = df['Label']
    y_score = df['Pred']
    y_pred = np.where(y_score >= 0.5, 1, 0)

    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

    # 计算指标
    sensitivity = tp / (tp + fn)
    specificity = tn / (tn + fp)
    accuracy = (tp + tn) / (tp + tn + fp + fn)
    ppv = tp / (tp + fp)
    npv = tn / (tn + fn)
    sensitivity_CI, specificity_CI, accuracy_CI, ppv_CI, npv_CI = compute_CI(tn, fp, fn, tp, method)
    f1Score = f1_score(y_true, y_pred)

    auc, std_, auc_ci = CalculateAUC(y_true, y_score)

    return sensitivity, specificity, accuracy, ppv, npv, sensitivity_CI, specificity_CI, accuracy_CI, ppv_CI, npv_CI, f1Score, auc, auc_ci


def get_printed_results(value, low=None, high=None):
    if low is not None:
        return f'{value:.2f}（{low:.2f}~{high:.2f}）'
    else:
        return f'{value:.2f}'


if __name__ == '__main__':
    results_all = {
        'Sen_(95% CI)': [],
        'Spe_(95% CI)': [],
        'Acc_(95% CI)': [],
        'PPV_(95% CI)': [],
        'NPV_(95% CI)': [],
        'F1_score': [],
        'AUC_(95% CI)': [],
    }

    root_path = Path(r'F:\数据\FAE\huis_data\results\results2_合并')
    cv_val_name = 'cv_val_prediction.csv'
    test_name = 'test_prediction.csv'
    data_path = {
        'SVMTrain': root_path / 'MinMax' / 'PCA' / 'RFE_37' / 'SVM' / cv_val_name,
        'SVMTest': root_path / 'MinMax' / 'PCA' / 'RFE_37' / 'SVM' / test_name,
        'AETrain': root_path / 'Zscore' / 'PCC' / 'RFE_27' / 'AE' / cv_val_name,
        'AETest': root_path / 'Zscore' / 'PCC' / 'RFE_27' / 'AE' / test_name,
        'LDATrain': root_path / 'Mean' / 'PCA' / 'RFE_39' / 'LDA' / cv_val_name,
        'LDATest': root_path / 'Mean' / 'PCA' / 'RFE_39' / 'LDA' / test_name,
        'RFTrain': Path(r'F:\数据\FAE\huis_data\results\results1_合并') / 'Mean' / 'PCC' / 'KW_24' / 'RF' / cv_val_name,
        'RFTest': root_path / 'Mean' / 'PCC' / 'Relief_32' / 'RF' / test_name,
        'LRTrain': root_path / 'MinMax' / 'PCA' / 'RFE_32' / 'LR' / cv_val_name,
        'LRTest': root_path / 'MinMax' / 'PCA' / 'RFE_32' / 'LR' / test_name,
        'ABTrain': root_path / 'Mean' / 'PCC' / 'RFE_33' / 'AB' / cv_val_name,
        'ABTest': root_path / 'Mean' / 'PCC' / 'RFE_33' / 'AB' / test_name,
        'DTTrain': root_path / 'MinMax' / 'PCC' / 'RFE_30' / 'DT' / cv_val_name,
        'DTTest': root_path / 'MinMax' / 'PCC' / 'RFE_30' / 'DT' / test_name,
        'NBTrain': root_path / 'MinMax' / 'PCA' / 'RFE_31' / 'NB' / cv_val_name,
        'NBTest': root_path / 'MinMax' / 'PCA' / 'RFE_31' / 'NB' / test_name,
    }

    index = ['RFTrain', 'SVMTrain', 'AETrain', 'LDATrain', 'LRTrain', 'ABTrain', 'DTTrain', 'NBTrain', 'RFTest',
             'SVMTest', 'AETest', 'LDATest', 'LRTest', 'ABTest', 'DTTest', 'NBTest']
    for i in index:
        sensitivity, specificity, accuracy, ppv, npv, sensitivity_CI, specificity_CI, accuracy_CI, ppv_CI, npv_CI, f1Score, auc, auc_ci = get_diagnosis_performance(
            data_path[i], method='normal')
        results_all['Sen_(95% CI)'].append(get_printed_results(sensitivity, sensitivity_CI[0], sensitivity_CI[1]))
        results_all['Spe_(95% CI)'].append(get_printed_results(specificity, specificity_CI[0], specificity_CI[1]))
        results_all['Acc_(95% CI)'].append(get_printed_results(accuracy, accuracy_CI[0], accuracy_CI[1]))
        results_all['PPV_(95% CI)'].append(get_printed_results(ppv, ppv_CI[0], ppv_CI[1]))
        results_all['NPV_(95% CI)'].append(get_printed_results(npv, npv_CI[0], npv_CI[1]))
        results_all['F1_score'].append(get_printed_results(f1Score))
        results_all['AUC_(95% CI)'].append(get_printed_results(auc, auc_ci[0], auc_ci[1]))

    results_all_df = pd.DataFrame(results_all, index=index)
    results_all_df.to_excel('./resources/results/ML/Results_all_for_CUltra.xlsx')
