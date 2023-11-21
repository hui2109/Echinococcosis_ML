import pickle

import pandas as pd
import random
import numpy as np


def get_target_group(group_label, total_data):
    df = pd.DataFrame()
    for label in group_label:
        df_tmp = total_data[total_data['patient_ID'] == label]
        df = pd.concat([df, df_tmp])
    return df


def save_to_pickle(file_name, data):
    with open(file_name, 'wb') as f:
        pickle.dump(data, f)


def load_pickle(file_name):
    with open(file_name, 'rb') as f:
        data = pickle.load(f)
        return data


def _generate_random_number(min_probability, max_probability):
    # 生成一个在指定范围内的随机概率值
    probability = random.uniform(min_probability, max_probability)

    # 生成一个0到1之间的随机浮点数
    random_value = random.random()

    # 根据概率范围判断生成的随机数范围
    if random_value < probability:
        # 以生成的概率生成随机数
        result = 1  # 这里生成1到100之间的随机整数，你可以根据需要调整范围
    else:
        # 以(1 - probability)的概率生成其他值，或者不生成任何值，这里简单返回0
        result = 0

    return result


def get_add_AE_prediction_num(probability: float, add_num: int):
    min_probability = probability - 0.5
    max_probability = probability + 0.5

    if min_probability < 0.1:
        min_probability = 0.1
    elif max_probability > 0.9:
        max_probability = 0.9

    num_list = []
    for i in range(add_num):
        random_number = _generate_random_number(min_probability, max_probability)
        num_list.append(random_number)

    num_list = np.array(num_list)
    return np.sum(num_list == 1)
