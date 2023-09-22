import pandas as pd
import pickle
from pathlib import Path
import numpy as np

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


A = np.array([1, 2, 3, 4])
B = np.array([0, 1, 1, 0])

# 使用布尔索引从A中选择与B中值为1的元素对应的元素
selected_elements = A[B == 1]

print(selected_elements)

