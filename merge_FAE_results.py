from pathlib import Path

import pandas as pd


def merge_results(root_path: str, save_path: str):
    root_path = Path(root_path)
    save_path = Path(save_path)

    configs = {
        'Normalizer': ['Mean', 'MinMax', 'Zscore'],
        'DimensionReduction': ['PCA', 'PCC'],
        'FeatureSelector': ['ANOVA', 'KW', 'RFE'],
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

                        merged_results['cv_train_Acc'].append(float(metrics.loc['cv_train_Acc'].iloc[0]))
                        merged_results['cv_train_AUC'].append(float(metrics.loc['cv_train_AUC'].iloc[0]))

                        merged_results['cv_val_Acc'].append(float(metrics.loc['cv_val_Acc'].iloc[0]))
                        merged_results['cv_val_AUC'].append(float(metrics.loc['cv_val_AUC'].iloc[0]))

    df = pd.DataFrame(data=merged_results)
    df.to_csv(save_path, index=False)


if __name__ == '__main__':
    merge_results(r'G:\FAE\huis_data\results\results1_合并',
                  './resources/results/results1_merged.csv')
