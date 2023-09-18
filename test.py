import pandas as pd
import pickle
from pathlib import Path

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

df_train = pd.read_csv('./resources/all_images/Groups/train_ids.csv')
df_val = pd.read_csv('./resources/all_images/Groups/validation_ids.csv')
df_test = pd.read_csv('./resources/all_images/Groups/test_ids.csv')
df_total = pd.read_csv('./resources/trim_data/add_ID.csv')

df = pd.concat([df_train, df_val, df_test])
df_set = set(df['ids'])
# print(len(df_set))

new_id_set = set(df_total['患者新ID'])
# print(len(new_id_set))

inters = new_id_set.intersection(df_set)
# print(len(inters))

diff = new_id_set.difference(df_set)
with open('./resources/source_data/excluded_ids.csv', 'w', 1, 'utf-8') as f:
    f.write('ids' + '\n')
    for i in sorted(diff):
        f.write(i + '\n')
