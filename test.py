# import pathlib
# import os
# import pickle
#
# import SimpleITK as sitk
# import numpy as np
# from PIL import Image
#
# i = r'D:\295.jpg'
# img = Image.open(i)
# grey_img = img.convert('L')
# grey_img_array = np.array(grey_img)
# # grey_img_3d_array = np.array([grey_img_array])
# img = sitk.GetImageFromArray(grey_img_array)
# sitk.WriteImage(img, './img1.nrrd')

import os
import pathlib
import pickle
import time

import pandas as pd
from radiomics import featureextractor

# extractor = featureextractor.RadiomicsFeatureExtractor(force2D=True)
# extractor.enableAllFeatures()
# extractor.enableImageTypes(
#     Original={},
#     Wavelet={},
#     LoG={},
#     Logarithm={},
#     Exponential={},
#     Gradient={},
# )
# img = r'D:\img.nrrd'
# mask = r'D:\out.nrrd'
#
# featureVector = extractor.execute(img, mask)
# result_path = pathlib.Path('./aaa.xlsx')
#
# df = pd.DataFrame()
# df_new = pd.DataFrame.from_dict(featureVector.values()).T
# df_new.columns = featureVector.keys()
# df = pd.concat([df, df_new])
#
# with pd.ExcelWriter(result_path) as writer:
#     df.to_excel(writer, index=False)

with open('resources/extract_data/finding_list_2022.pkl', 'rb') as f:
    finding_list_2022 = pickle.load(f)
    print(len(finding_list_2022))
