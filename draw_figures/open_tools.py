from pathlib import Path

import pandas


def open_specific_path(norm, fdr, fs_nums_feature, classifier):
    root_path = Path(r'G:\FAE\huis_data\results\results1_合并')
    path = root_path / norm / fdr / fs_nums_feature / classifier / 'metrics.csv'
    with open(path, 'r', 1, 'utf-8') as f:
        for line in f.readlines():
            if line.startswith('cv_train_AUC'):
                cv_train_AUC = line.strip().split(',')[-1]
            elif line.startswith('test_AUC'):
                test_AUC = line.strip().split(',')[-1]
            elif line.startswith('cv_val_AUC'):
                cv_val_AUC = line.strip().split(',')[-1]
            elif line.startswith('cv_val_95%'):
                cv_val_AUC_low, cv_val_AUC_high = line.strip().split('[')[-1][:-1].split('-')
            elif line.startswith('cv_val_Std'):
                cv_val_std = line.strip().split(',')[-1]
            elif line.startswith('train_AUC'):
                train_AUC = line.strip().split(',')[-1]
    return {
        'cross-validation training': float(cv_train_AUC),
        'cross-validation validation': float(cv_val_AUC),
        'testing': float(test_AUC),
        'cross-validation lower_limit': float(cv_val_AUC_low),
        'cross-validation upper_limit': float(cv_val_AUC_high),
        'cross-validation std': float(cv_val_std),
        'train_AUC': float(train_AUC)
    }


def open_specific_prediction_file(norm, fdr, fs_nums_feature, classifier, prediction_file,
                                  root_path: str = r'G:\FAE\huis_data\results\results2_合并'):
    root_path = Path(root_path)
    path = root_path / norm / fdr / fs_nums_feature / classifier / prediction_file

    df = pandas.read_csv(path)
    y_true = df['Label']
    y_score = df['Pred']
    return y_true, y_score


if __name__ == '__main__':
    r1 = open_specific_path('Zscore', 'PCC', 'Relief_36', 'RF')
    print(r1)

    r2 = open_specific_prediction_file('Zscore', 'PCC', 'Relief_36', 'RF', 'train_prediction.csv')
    print(r2)
