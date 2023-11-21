#
# extract_results_2022: pd.DataFrame = pd.read_pickle('./resources/temp_file/extract_results_2022.pkl').iloc[:, 22:-2]
# # final_extract_results: pd.DataFrame = pd.read_pickle('./resources/temp_file/final_extract_results.pkl').iloc[:, 22:]
#
# er2_index = extract_results_2022.columns
# # fer_index = final_extract_results.columns
#
# # print(len(er2_index), er2_index)
# # print(len(fer_index), fer_index)
#
# # minmax_results: pd.DataFrame = pd.read_csv(
# #     r'G:\FAE\huis_data\results\results1_合并\MinMax\MinMax_normalized_test_feature.csv').iloc[:, 2:]
# # minmax_index = minmax_results.columns
# #
# # for i in er2_index:
# #     if i not in minmax_index:
# #         print(i)
#
# exclude_columns = ['original_shape_Flatness', 'original_shape_LeastAxisLength', 'gradient_firstorder_Minimum']

# pd.read_excel('./resources/extract_data/external_test_set_2022.xlsx').to_pickle('./resources/temp_file/external_test_set_2022.pkl')

# with open(r'G:\FAE\huis_data\results\results1_合并\Mean\PCC\ANOVA_40\feature_select_info.csv', 'r', 1, encoding='utf-8') as f:
#     for i in f.readlines():
#         if i.startswith('selected_feature'):
#             m = i.strip().split(',')
#             print(len(m[1:]))


# with open(r'G:\FAE\huis_data\results\results1_合并\Mean\PCA\ANOVA_40\AB\model.pickle', 'rb') as f:
#     model: sklearn.ensemble._weight_boosting.AdaBoostClassifier = pickle.load(f)
#
# test_data = pd.read_csv(r'G:\FAE\huis_data\results\results1_合并\Mean\PCA\ANOVA_40\ANOVA_test_feature.csv')
# features = test_data.iloc[:, 2:]
# # print(test_data.shape) # (4691, 1) (4691,)
# y_pred = model.predict_proba(features)[:, 1]
# y_true = test_data.iloc[:, 1]
#
# precision, recall, thresholds = precision_recall_curve(y_true, y_pred)
# auc1 = auc(recall, precision)
#
# fpr, tpr, thresholds = roc_curve(y_true, y_pred)
# auc2 = auc(fpr, tpr)
#
# print(auc1, auc2)

# import os
# from pathlib import Path
#
#
# def my_rename(p: Path, prefix):
#     os.chdir(p)
#     for i in p.iterdir():
#         i.rename(f'{prefix}-' + i.name)
#
#
# if __name__ == '__main__':
#     jpg_CE_p = Path(r'G:\肝包虫图片\2023年9月8日包虫考核\考核用图\dataset_voc_CE\JPEGImages')
#     my_rename(jpg_CE_p, 'R')
#
#     png_CE_p = Path(r'G:\肝包虫图片\2023年9月8日包虫考核\考核用图\dataset_voc_CE\SegmentationClassPNG')
#     my_rename(png_CE_p, 'R')
#
#     jpg_AE_p = Path(r'G:\肝包虫图片\2023年9月8日包虫考核\考核用图\dataset_voc_AE\JPEGImages')
#     my_rename(jpg_AE_p, 'B')
#
#     png_AE_p = Path(r'G:\肝包虫图片\2023年9月8日包虫考核\考核用图\dataset_voc_AE\SegmentationClassPNG')
#     my_rename(png_AE_p, 'B')

# sss = '你好，,.。123-3/'
# res = pypinyin.lazy_pinyin(sss)
# print(res)

# def hanzi_to_pinyin(p: Path):
#     os.chdir(p)
#     for i in p.iterdir():
#         new_name = ''.join(pypinyin.lazy_pinyin(i.name))
#         i.rename(new_name)
#
#
# if __name__ == '__main__':
#     img = Path(r'D:\exe_code\Python\17_Echinococcosis_ML\resources\all_images\IMGs_2023')
#     hanzi_to_pinyin(img)
#
#     mask = Path(r'D:\exe_code\Python\17_Echinococcosis_ML\resources\all_images\MASKs_2023')
#     hanzi_to_pinyin(mask)

# s_2023 = pd.read_excel('./resources/extract_data/external_test_set_2023.xlsx')
# s_2023.to_pickle('./resources/temp_file/external_test_set_2023.pkl')


# import random
# import numpy as np
#
#
# def generate_random_number(min_probability, max_probability):
#     # 生成一个在指定范围内的随机概率值
#     probability = random.uniform(min_probability, max_probability)
#
#     # 生成一个0到1之间的随机浮点数
#     random_value = random.random()
#
#     # 根据概率范围判断生成的随机数范围
#     if random_value < probability:
#         # 以生成的概率生成随机数
#         result = 1  # 这里生成1到100之间的随机整数，你可以根据需要调整范围
#     else:
#         # 以(1 - probability)的概率生成其他值，或者不生成任何值，这里简单返回0
#         result = 0
#
#     return result
#
#
# # 设置生成随机数的概率范围为0.2到0.5
# min_probability = 0.2
# max_probability = 0.5
#
# # 调用函数生成随机数
# num_list = []
# for i in range(100):
#     random_number = generate_random_number(min_probability, max_probability)
#     num_list.append(random_number)
#
# num_list = np.array(num_list)
# print(np.sum(num_list == 1) / len(num_list))

from utils import get_add_AE_prediction_num
