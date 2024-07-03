from pathlib import Path

import pandas as pd
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


def merge_results(root_path: str, save_path: str):
    root_path = Path(root_path)
    save_path = Path(save_path)

    configs = {
        'Normalizer': ['Mean', 'MinMax', 'Zscore'],
        'DimensionReduction': ['PCA', 'PCC'],
        'FeatureSelector': ['ANOVA', 'KW', 'RFE', 'Relief'],
        'FeatureNumber': [str(i) for i in range(1, 41)],
        'Classifier': ['SVM', 'LDA', 'AE', 'RF', 'LR', 'AB', 'DT', 'NB']
    }

    merged_results = {
        'model': [],
        'train_Acc': [],
        'train_AUC': [],
        'test_Acc': [],
        'test_AUC': [],
        'cv_train_Acc': [],
        'cv_train_AUC': [],
        'cv_val_Acc': [],
        'cv_val_AUC': []
    }

    for norm in configs['Normalizer']:
        for dr in configs['DimensionReduction']:
            for fs in configs['FeatureSelector']:
                for fn in configs['FeatureNumber']:
                    fs_fn = fs + '_' + fn
                    for cls in configs['Classifier']:
                        metrics_path = root_path / norm / dr / fs_fn / cls / 'metrics.csv'
                        metrics = pd.read_csv(metrics_path, index_col=0)
                        merged_results['model'].append(norm + '_' + dr + '_' + fs_fn + '_' + cls)

                        merged_results['train_Acc'].append(float(metrics.loc['train_Acc'].iloc[0]))
                        merged_results['train_AUC'].append(float(metrics.loc['train_AUC'].iloc[0]))

                        merged_results['test_Acc'].append(float(metrics.loc['test_Acc'].iloc[0]))
                        merged_results['test_AUC'].append(float(metrics.loc['test_AUC'].iloc[0]))

                        if 'cv_train_Acc' not in metrics.index:
                            cv_train_acc = get_acc(root_path, norm, dr, fs_fn, cls, 'train')
                            cv_train_auc = get_auc(root_path, norm, dr, fs_fn, cls, 'train')
                            cv_val_acc = get_acc(root_path, norm, dr, fs_fn, cls, 'val')
                            cv_val_auc = get_auc(root_path, norm, dr, fs_fn, cls, 'val')

                            merged_results['cv_train_Acc'].append(cv_train_acc)
                            merged_results['cv_train_AUC'].append(cv_train_auc)
                            merged_results['cv_val_Acc'].append(cv_val_acc)
                            merged_results['cv_val_AUC'].append(cv_val_auc)
                        else:
                            merged_results['cv_train_Acc'].append(float(metrics.loc['cv_train_Acc'].iloc[0]))
                            merged_results['cv_train_AUC'].append(float(metrics.loc['cv_train_AUC'].iloc[0]))
                            merged_results['cv_val_Acc'].append(float(metrics.loc['cv_val_Acc'].iloc[0]))
                            merged_results['cv_val_AUC'].append(float(metrics.loc['cv_val_AUC'].iloc[0]))

    df = pd.DataFrame(data=merged_results)
    df.to_csv(save_path, index=False)


if __name__ == '__main__':
    merge_results(r'G:\FAE\huis_data\results\results3_合并',
                  './resources/results/Better_images_2D.csv')
