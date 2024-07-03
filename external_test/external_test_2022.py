import pickle
from pathlib import Path

import numpy as np
import pandas as pd
import sklearn
from sklearn.metrics import auc, roc_curve


def norm_training(norm_method: str):
    norm_results = external_test_set_2022.copy()

    norm_training: pd.DataFrame = pd.read_csv(
        root_results_path / norm_method / f'{norm_method}_normalization_training.csv', index_col=0)
    for row in norm_training.itertuples(index=False):
        feature_name = row[0]
        slop = row[1]
        interception = row[2]

        target_data = np.array(norm_results[feature_name])
        target_data = target_data - interception
        target_data = target_data / slop

        norm_results[feature_name] = target_data

    return norm_results


def dr_training(norm_method: str, dr_method: str, norm_results):
    if dr_method == 'PCA':
        with open(root_results_path / norm_method / dr_method / 'PCA.pickle', 'rb') as f:
            pca_model: sklearn.decomposition._pca.PCA = pickle.load(f)
        pca_results = pca_model.transform(norm_results.iloc[:, 1:])
        pca_results = pd.DataFrame(pca_results)

        columns = []
        for i in range(1, len(pca_results.columns) + 1):
            columns.append(f'PCA_feature_{i}')
        pca_results.columns = columns
        pca_results = pd.concat([norm_results.iloc[:, 0], pca_results], axis=1)

        return pca_results

    if dr_method == 'PCC':
        PCC_sort = pd.read_csv(root_results_path / norm_method / dr_method / 'PCC_sort.csv', index_col=0)
        pcc_results = norm_results[PCC_sort['0']]
        pcc_results = pd.concat([norm_results.iloc[:, 0], pcc_results], axis=1)

        return pcc_results


def fs_fn_training(norm_method: str, dr_method: str, fs_fn_method: str, dr_results):
    with open(root_results_path / norm_method / dr_method / fs_fn_method / 'feature_select_info.csv') as f:
        for line in f.readlines():
            if line.startswith('selected_feature'):
                fs_info_list = line.strip().split(',')[1:]

    fs_results = dr_results[fs_info_list]
    fs_results = pd.concat([dr_results.iloc[:, 0], fs_results], axis=1)

    return fs_results


def cls_training(norm_method: str, dr_method: str, fs_fn_method: str, cls_method: str, fs_results):
    with open(root_results_path / norm_method / dr_method / fs_fn_method / cls_method / 'model.pickle', 'rb') as f:
        model = pickle.load(f)

    features = fs_results.iloc[:, 1:]
    y_pred = model.predict_proba(features)[:, 1]
    y_true = fs_results.iloc[:, 0]
    fpr, tpr, thresholds = roc_curve(y_true, y_pred)
    ets_auc = auc(fpr, tpr)

    save_results(norm_method, dr_method, fs_fn_method, cls_method, ets_auc, fs_results)


def save_results(norm_method: str, dr_method: str, fs_fn_method: str, cls_method: str, ets_auc, fs_results):
    file_name = norm_method + '_' + dr_method + '_' + fs_fn_method + '_' + cls_method
    fs_results.to_csv(save_path / (file_name + '.csv'), index=False)
    external_test_set_2022_results['reg_external_test_set_2022'].append(file_name)
    external_test_set_2022_results['AUC'].append(ets_auc)


if __name__ == '__main__':
    configs = {
        'Normalizer': ['Mean', 'MinMax', 'Zscore'],
        'DimensionReduction': ['PCA', 'PCC'],
        'FeatureSelector': ['ANOVA', 'KW', 'RFE'],
        'FeatureNumber': [str(i) for i in range(1, 41)],
        'Classifier': ['SVM', 'LDA', 'AE', 'RF', 'LR', 'AB', 'DT', 'NB']
    }
    root_results_path = Path(r'G:\FAE\huis_data\results\results1_合并')
    external_test_set_2022: pd.DataFrame = pd.read_pickle('./resources/temp_file/external_test_set_2022.pkl')

    external_test_set_2022_results = {
        'reg_external_test_set_2022': [],
        "AUC": []
    }
    save_path = Path('./resources/external_test/2022/reg_external_test_set_2022')

    for norm in configs['Normalizer']:
        norm_results = norm_training(norm)
        for dr in configs['DimensionReduction']:
            dr_results = dr_training(norm, dr, norm_results)
            for fs in configs['FeatureSelector']:
                for fn in configs['FeatureNumber']:
                    fs_fn = fs + '_' + fn
                    fs_results = fs_fn_training(norm, dr, fs_fn, dr_results)
                    for cls in configs['Classifier']:
                        cls_training(norm, dr, fs_fn, cls, fs_results)

    save_df = pd.DataFrame(external_test_set_2022_results)
    save_df.to_csv(save_path.parent / 'external_test_set_2022_results.csv', index=False)
