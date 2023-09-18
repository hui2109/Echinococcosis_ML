import os
import pathlib
import pickle
import time

import pandas as pd
from radiomics import featureextractor


def extract_features(img, mask):
    extractor = featureextractor.RadiomicsFeatureExtractor()
    extractor.enableAllFeatures()
    extractor.enableImageTypes(
        Original={},
        Wavelet={},
        LoG={},
        Logarithm={},
        Exponential={},
        Gradient={},
    )
    return extractor.execute(img, mask)


def batch_extract():
    with open('./resources/source_data/finding_list.pkl', 'rb') as f:
        finding_list = pickle.load(f)

    df = pd.DataFrame()
    for results in finding_list:  # results是一个字典
        img = str(results['img'].resolve(strict=True))
        mask = str(results['mask'].resolve(strict=True))
        label = results['label']
        stem = results['stem']

        # 特征提取
        featureVector = extract_features(img=img, mask=mask)

        featureVector['label'] = label
        featureVector['process_index'] = i
        featureVector['stem'] = stem

        # 将提取的特征转换为DataFrame格式
        df_new = pd.DataFrame.from_dict(featureVector.values()).T
        df_new.columns = featureVector.keys()
        df = pd.concat([df, df_new])

    # 将提取的特征结果写入文件
    result_path = pathlib.Path(f'./resources/source_data/results_{int(time.time())}.xlsx')
    with pd.ExcelWriter(result_path) as writer:
        df.to_excel(writer, index=False)


if __name__ == '__main__':
    batch_extract()
