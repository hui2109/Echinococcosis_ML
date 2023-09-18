# a = 1
# b = f'{a:010}'
# print(repr(b))

import pandas as pd

df = pd.read_csv('./resources/trim_data/add_year.csv')
for i, ID in enumerate(df['患者ID']):
    if str(ID) == 'nan':
        df.iloc[i, 9] = str(df.iloc[i, 3])[7:]

# print(len(set(df['患者ID'])))  # 4976

previous_ID_set = set(df['患者ID'])
none_list = [None] * len(previous_ID_set)
ID_dict = dict(zip(previous_ID_set, none_list))

# print(len(ID_dict))  # 4976

index = 1
new_patient_ID_list = []
for i in df['患者ID']:
    if ID_dict[i] is None:
        new_ID = f'{index:05}' + 'E'
        new_patient_ID_list.append(new_ID)
        ID_dict[i] = new_ID
        index += 1
    else:
        new_patient_ID_list.append(ID_dict[i])
# print(new_patient_ID_list[:5], len(new_patient_ID_list), len(set(new_patient_ID_list)))  # 4976

series = pd.Series(new_patient_ID_list)
df.insert(len(df.columns), '患者新ID', series)
df.to_csv('./resources/trim_data/add_ID.csv', index=False, encoding='utf-8-sig')

print(len(set(df['患者新ID'])))  # 4976
