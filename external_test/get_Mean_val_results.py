import pandas as pd

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

    'outline_SVM_p1': './resources/results/outlines/SVM/val/p1.csv',
    'outline_SVM_p2': './resources/results/outlines/SVM/val/p2.csv',
    'outline_SVM_p3': './resources/results/outlines/SVM/val/p3.csv',
    'outline_SVM_p4': './resources/results/outlines/SVM/val/p4.csv',
    'outline_SVM_p5': './resources/results/outlines/SVM/val/p5.csv',
    'outline_SVM_p6': './resources/results/outlines/SVM/val/p6.csv',

    'outline_ResNet_p1': './resources/results/outlines/ResNet/val/p1.csv',
    'outline_ResNet_p2': './resources/results/outlines/ResNet/val/p2.csv',
    'outline_ResNet_p3': './resources/results/outlines/ResNet/val/p3.csv',
    'outline_ResNet_p4': './resources/results/outlines/ResNet/val/p4.csv',
    'outline_ResNet_p5': './resources/results/outlines/ResNet/val/p5.csv',
    'outline_ResNet_p6': './resources/results/outlines/ResNet/val/p6.csv',
}

All_E = pd.concat([pd.read_csv(results_path_all['External_senior_E']),
                   pd.read_csv(results_path_all['External_middle_E']),
                   pd.read_csv(results_path_all['External_junior_E']),
                   ], ignore_index=True)
All_NE = pd.concat([pd.read_csv(results_path_all['External_senior_NE']),
                    pd.read_csv(results_path_all['External_middle_NE']),
                    pd.read_csv(results_path_all['External_junior_NE'])
                    ], ignore_index=True)

All_E.to_csv('./resources/results/External/Mean_E/mk_2022_inves.csv')
All_NE.to_csv('./resources/results/External/Mean_NE/mk_2022_inves.csv')
