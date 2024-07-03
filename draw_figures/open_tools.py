from pathlib import Path

import numpy as np
import pandas as pd
import scipy
from sklearn.metrics import accuracy_score, roc_auc_score


def get_acc(root_path: Path, norm: str, dr: str, fs_fn: str, cls: str, sset: str):
    acc_csv_path = root_path / norm / dr / fs_fn / cls / f'cv_{sset}_prediction.csv'
    acc_csv = pd.read_csv(acc_csv_path, index_col=0)
    y_score = acc_csv['Pred']
    y_true = acc_csv['Label']
    y_pred = [1 if round(i, 1) >= 0.5 else 0 for i in y_score]
    return accuracy_score(y_true, y_pred)


def get_auc(root_path: Path, norm: str, dr: str, fs_fn: str, cls: str, sset: str):
    acc_csv_path = root_path / norm / dr / fs_fn / cls / f'cv_{sset}_prediction.csv'
    acc_csv = pd.read_csv(acc_csv_path, index_col=0)
    y_score = acc_csv['Pred']
    y_true = acc_csv['Label']
    return roc_auc_score(y_true, y_score)


def open_specific_path(norm, fdr, fs_nums_feature, classifier, path='all'):
    if path == 'all':
        root_path = Path(r'F:\数据\FAE\huis_data\results\results1_合并')
    else:
        root_path = Path(r'F:\数据\FAE\huis_data\results\results2_合并')

    path = root_path / norm / fdr / fs_nums_feature / classifier / 'metrics.csv'
    df = pd.read_csv(path, index_col=0)
    train_AUC = df.loc['train_AUC'].iloc[0]
    test_AUC = df.loc['test_AUC'].iloc[0]

    if 'cv_train_Acc' not in df.index:
        cv_val_prediction_path = root_path / norm / fdr / fs_nums_feature / classifier / 'cv_val_prediction.csv'
        cv_val_prediction = pd.read_csv(cv_val_prediction_path, index_col=0)
        label = cv_val_prediction['Label']
        prediction = cv_val_prediction['Pred']
        cv_val_AUC, cv_val_Std, ci = CalculateAUC(label, prediction)
        cv_val_AUC_low = ci[0]
        cv_val_AUC_high = ci[1]
    else:
        cv_val_AUC = df.loc['cv_val_AUC'].iloc[0]
        cv_val_Std = df.loc['cv_val_Std'].iloc[0]
        _cv_val_95_CI = df.loc['cv_val_95% CIs'].iloc[0]  # [0.6313-0.6457]
        cv_val_AUC_low = _cv_val_95_CI.strip().split('-')[0][1:]
        cv_val_AUC_high = _cv_val_95_CI.strip().split('-')[-1][:-1]

    return {
        'testing': float(test_AUC),
        'train_AUC': float(train_AUC),
        'cross-validation validation': float(cv_val_AUC),
        'cross-validation lower_limit': float(cv_val_AUC_low),
        'cross-validation upper_limit': float(cv_val_AUC_high),
        'cross-validation std': float(cv_val_Std)
    }


def open_specific_prediction_file(norm, fdr, fs_nums_feature, classifier, prediction_file,
                                  root_path: str = r'G:\FAE\huis_data\results\results2_合并'):
    root_path = Path(root_path)
    path = root_path / norm / fdr / fs_nums_feature / classifier / prediction_file

    df = pandas.read_csv(path)
    y_true = df['Label']
    y_score = df['Pred']
    return y_true, y_score


def CalculateAUC(label, prediction, alpha=.95):
    auc, var = delong_roc_variance(label, prediction)
    std = np.sqrt(var)
    lower_upper_q = np.abs(np.array([0, 1]) - (1 - alpha) / 2)

    if std < 1e-6:
        ci = [auc, auc]
    else:
        ci = scipy.stats.norm.ppf(lower_upper_q, loc=auc, scale=std)
        ci[ci > 1] = 1
    return auc, std, ci


def delong_roc_variance(ground_truth, predictions):
    """
    Computes ROC AUC variance for a single set of predictions
    Args:
       ground_truth: np.array of 0 and 1
       predictions: np.array of floats of the probability of being class 1
    """
    order, label_1_count = compute_ground_truth_statistics(ground_truth)
    # predictions_sorted_transposed = predictions[np.newaxis, order]
    predictions = np.array(predictions)
    predictions_sorted_transposed = predictions[order][np.newaxis, ...]
    aucs, delongcov = fastDeLong(predictions_sorted_transposed, label_1_count)
    assert len(aucs) == 1, "There is a bug in the code, please forward this to the developers"
    return aucs[0], delongcov


def compute_ground_truth_statistics(ground_truth):
    assert np.array_equal(np.unique(ground_truth), [0, 1])
    order = (-ground_truth).argsort()
    label_1_count = int(ground_truth.sum())
    return order, label_1_count


def compute_midrank(x):
    """Computes midranks.
    Args:
       x - a 1D numpy array
    Returns:
       array of midranks
    """
    J = np.argsort(x)
    Z = x[J]
    N = len(x)
    T = np.zeros(N, dtype=float)
    i = 0
    while i < N:
        j = i
        while j < N and Z[j] == Z[i]:
            j += 1
        T[i:j] = 0.5 * (i + j - 1)
        i = j
    T2 = np.empty(N, dtype=float)
    # Note(kazeevn) +1 is due to Python using 0-based indexing
    # instead of 1-based in the AUC formula in the paper
    T2[J] = T + 1
    return T2


def fastDeLong(predictions_sorted_transposed, label_1_count):
    """
    The fast version of DeLong's method for computing the covariance of
    unadjusted AUC.
    Args:
       predictions_sorted_transposed: a 2D numpy.array[n_classifiers, n_examples]
          sorted such as the examples with label "1" are first
    Returns:
       (AUC value, DeLong covariance)
    Reference:
     @article{sun2014fast,
       title={Fast Implementation of DeLong's Algorithm for
              Comparing the Areas Under Correlated Receiver Operating Characteristic Curves},
       author={Xu Sun and Weichao Xu},
       journal={IEEE Signal Processing Letters},
       volume={21},
       number={11},
       pages={1389--1393},
       year={2014},
       publisher={IEEE}
     }
    """
    # Short variables are named as they are in the paper
    m = label_1_count
    n = predictions_sorted_transposed.shape[1] - m
    positive_examples = predictions_sorted_transposed[:, :m]
    negative_examples = predictions_sorted_transposed[:, m:]
    k = predictions_sorted_transposed.shape[0]

    tx = np.empty([k, m], dtype=float)
    ty = np.empty([k, n], dtype=float)
    tz = np.empty([k, m + n], dtype=float)
    for r in range(k):
        tx[r, :] = compute_midrank(positive_examples[r, :])
        ty[r, :] = compute_midrank(negative_examples[r, :])
        tz[r, :] = compute_midrank(predictions_sorted_transposed[r, :])
    aucs = tz[:, :m].sum(axis=1) / m / n - float(m + 1.0) / 2.0 / n
    v01 = (tz[:, :m] - tx[:, :]) / n
    v10 = 1.0 - (tz[:, m:] - ty[:, :]) / m
    sx = np.cov(v01)
    sy = np.cov(v10)
    delongcov = sx / m + sy / n
    return aucs, delongcov


def get_full_data(norm, fdr, fs_nums_feature, classifier, set_name):
    root_path = Path(r'G:\FAE\huis_data\results\results1_合并')

    s1_norm_Mean = open_specific_path('Mean', fdr, fs_nums_feature, classifier)
    s1_norm_Zscore = open_specific_path('Zscore', fdr, fs_nums_feature, classifier)
    s1_norm_MinMax = open_specific_path('MinMax', fdr, fs_nums_feature, classifier)
    data_Norm = [s1_norm_Mean[set_name], s1_norm_Zscore[set_name],
                 s1_norm_MinMax[set_name]]

    s1_fdd_PCA = open_specific_path(norm, 'PCA', fs_nums_feature, classifier)
    s1_fdd_PCC = open_specific_path(norm, 'PCC', fs_nums_feature, classifier)
    data_FDD = [s1_fdd_PCA[set_name], s1_fdd_PCC[set_name]]

    nums_feature = fs_nums_feature.split('_')[-1]
    s1_fs_ANOVA = open_specific_path(norm, fdr, f'ANOVA_{nums_feature}', classifier)
    s1_fs_KW = open_specific_path(norm, fdr, f'KW_{nums_feature}', classifier)
    s1_fs_RFE = open_specific_path(norm, fdr, f'RFE_{nums_feature}', classifier)
    s1_fs_Relief = open_specific_path(norm, fdr, f'Relief_{nums_feature}', classifier)
    data_FS = [s1_fs_ANOVA[set_name], s1_fs_KW[set_name],
               s1_fs_RFE[set_name], s1_fs_Relief[set_name]]

    s1_clf_SVM = open_specific_path(norm, fdr, fs_nums_feature, 'SVM')
    s1_clf_LDA = open_specific_path(norm, fdr, fs_nums_feature, 'LDA')
    s1_clf_AE = open_specific_path(norm, fdr, fs_nums_feature, 'AE')
    s1_clf_RF = open_specific_path(norm, fdr, fs_nums_feature, 'RF')
    s1_clf_LR = open_specific_path(norm, fdr, fs_nums_feature, 'LR')
    s1_clf_AB = open_specific_path(norm, fdr, fs_nums_feature, 'AB')
    s1_clf_DT = open_specific_path(norm, fdr, fs_nums_feature, 'DT')
    s1_clf_NB = open_specific_path(norm, fdr, fs_nums_feature, 'NB')
    data_CLF = [s1_clf_SVM[set_name], s1_clf_LDA[set_name],
                s1_clf_AE[set_name], s1_clf_RF[set_name],
                s1_clf_LR[set_name], s1_clf_AB[set_name],
                s1_clf_DT[set_name], s1_clf_NB[set_name]]

    data = data_Norm + data_FDD + data_FS + data_CLF
    return data


if __name__ == '__main__':
    r1 = open_specific_path(norm, 'PCC', 'Relief_36', 'DT')
    print(r1)

    # r2 = open_specific_prediction_file('Zscore', 'PCC', 'Relief_36', 'RF', 'train_prediction.csv')
    # print(r2)

    # df = pd.read_csv(r'G:\FAE\huis_data\results\results1_合并\Mean\PCC\KW_27\LR\cv_val_prediction.csv', index_col=0)
    # label = df['Label']
    # prediction = df['Pred']
    # data = CalculateAUC(label, prediction)
    # print(data)
