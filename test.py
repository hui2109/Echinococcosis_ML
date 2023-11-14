import pandas as pd
import pickle
from pathlib import Path
import numpy as np
from sklearn.model_selection import train_test_split

# 17676
# with open('./resources/source_data/finding_list.pkl', 'rb') as f:
#     finding_list = pickle.load(f)
# print(finding_list[17676]['img'].resolve(strict=True))
# print(finding_list[17676]['mask'].resolve(strict=True))

# df = pd.DataFrame()
# excel1 = pd.read_excel('./resources/source_data/final_extract_results.xlsx')
# excel2 = pd.read_excel('./resources/source_data/results_1694776386.xlsx')
# df = pd.concat([df, excel1])
# df = pd.concat([df, excel2])
# final_result = Path('./resources/source_data/final_extract_results2.xlsx')
# with pd.ExcelWriter(final_result) as writer:
#     df.to_excel(writer, index=False)

# with open('./resources/source_data/finding_list.pkl', 'rb') as f:
#     pl = pickle.load(f)
# print(pl[:5])


# A = np.array([1, 2, 3, 4])
# B = np.array([0, 1, 1, 0])
#
# # 使用布尔索引从A中选择与B中值为1的元素对应的元素
# selected_elements = A[B == 1]
#
# print(selected_elements)


df = pd.read_pickle('./resources/temp_file/final_extract_results.pkl')

X = df.iloc[:, 800:-4]
X['patient_ID'] = df.iloc[:, -1]
y = df.iloc[:, -4]

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.009, random_state=44)
print(X_train.shape, np.sum(y_train == 0) / len(y_train))

X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, train_size=0.7, random_state=42)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape, np.sum(y_train == 0) / len(y_train), np.sum(y_test == 0) / len(y_test))

X_train.to_csv('./resources/X_train.csv', index=False, encoding='utf-8-sig')
X_test.to_csv('./resources/X_test.csv', index=False, encoding='utf-8-sig')
y_train.to_csv('./resources/y_train.csv', index=False, encoding='utf-8-sig')
y_test.to_csv('./resources/y_test.csv', index=False, encoding='utf-8-sig')
