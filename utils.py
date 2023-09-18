import pandas as pd
import pickle


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
