import math
import time
import pickle
import sys

from typing import List

from batchextract import extract_features
import threading
import pathlib
import pandas as pd
import logging


# 控制台输出记录到文件
class Logger(object):
    def __init__(self, file_name, stream=sys.stdout):
        self.terminal = stream
        self.log = open(file_name / 'top_log.txt', "a", 1, 'utf-8')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


def log_error(name, index, error, log_path):
    with open(log_path, 'a', 1, 'utf-8') as f:
        f.write(f'{int(time.time())},{name},{index},{error}\n')


def save_data(df, path):
    # 将提取的特征结果写入文件
    with pd.ExcelWriter(path) as writer:
        df.to_excel(writer, index=False)


def start_extract(index: List[int]):
    with open('resources/extract_data/finding_list.pkl', 'rb') as f:
        finding_list = pickle.load(f)

    # 初始化存放文件夹
    name = threading.current_thread().name
    th_p = pathlib.Path(f'./resources/threads_results/threads_tmp_{name}/')
    th_p.mkdir(parents=True, exist_ok=True)

    # 初始化日志文件
    log_path = th_p / f'log_{name}.csv'
    with open(log_path, 'a', 1, 'utf-8-sig') as f:
        f.write('date,thread_name,index,error\n')

    # 初始化df、临时保存文件及保存文件
    df = pd.DataFrame()
    save_temp_path = th_p / f'results_{name}_tmp.xlsx'
    save_path = th_p / f'results_{name}.xlsx'

    # 初始化临时保存索引
    inner_i = 0
    inner_len = len(index)

    for i in index:
        inner_i += 1

        results = finding_list[i]  # results是一个字典
        img = str(results['img'].resolve(strict=True))
        mask = str(results['mask'].resolve(strict=True))
        label = results['label']
        stem = results['stem']

        # 特征提取
        try:
            featureVector = extract_features(img, mask)
            print(
                '\033[0;31;42m' + f'The {i}th image has been extracted, and ' + f'this thread {name} has {inner_len - inner_i} images left to be extracted.' + '\033[0m')
        except Exception as e:
            print(
                '\033[4;33;45m' + f'The {i}th image is in error! ' + f'This thread {name} has {inner_len - inner_i} images left to be extracted.' + '\033[0m')
            log_error(name, i, e, log_path)
            continue

        featureVector['label'] = label
        featureVector['thread_index'] = i
        featureVector['stem'] = stem

        df_new = pd.DataFrame.from_dict(featureVector.values()).T
        df_new.columns = featureVector.keys()
        df = pd.concat([df, df_new])

        # 定期保存文件
        if inner_i % 50 == 0:
            save_data(df, save_temp_path)

    # 将提取的特征结果写入文件
    save_data(df, save_path)


def get_thread_process_list(num: int, range_list: List):
    total_slice = []
    li_len = len(range_list)

    # num代表线程数，li代表总列表
    num_for_thread = li_len // num
    remain_num = li_len % num
    li_ = list(range(li_len))

    if remain_num == 0:
        for i in range(num):
            slice_ = li_[i * num_for_thread: (i + 1) * num_for_thread]
            total_slice.append(slice_)
    else:
        for i in range(num - 1):
            slice_ = li_[i * num_for_thread: (i + 1) * num_for_thread]
            total_slice.append(slice_)
        except_ = li_[(num - 1) * num_for_thread:]
        total_slice.append(except_)

    return num, total_slice


def main(num, range_list):
    num, total_slice = get_thread_process_list(num, range_list)

    obj_list = []
    for i in range(num):
        obj = threading.Thread(target=start_extract, args=(total_slice[i],))
        obj_list.append(obj)

    # 启动
    [i.start() for i in obj_list]
    # 等待子线程结束
    [i.join() for i in obj_list]


if __name__ == '__main__':
    t1 = time.time()

    # 记录正常的 print 信息 及 traceback 异常信息
    log_file_name = pathlib.Path('./resources/threads_results/')
    log_file_name.mkdir(exist_ok=True, parents=True)
    sys.stdout = Logger(log_file_name)
    sys.stderr = Logger(log_file_name)

    # set level for all radiomics classes
    logger = logging.getLogger("radiomics")
    logger.setLevel(logging.ERROR)

    with open('resources/extract_data/finding_list.pkl', 'rb') as f:
        finding_list = pickle.load(f)
        max_length = len(finding_list)
    main(101, list(range(max_length)))
    print('All images has been extracted!', 'Consuming time: ', time.time() - t1, ' s')
