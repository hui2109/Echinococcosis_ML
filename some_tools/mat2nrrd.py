import pathlib
import pickle
from pathlib import Path

import SimpleITK as sitk
import numpy as np
from PIL import Image
from scipy.io import loadmat


def mat_to_nrrd(mat_path: str):
    mat_path_p = Path(mat_path)
    stem = mat_path_p.stem

    mat_data = loadmat(mat_path)
    mat_roi = mat_data['roi'][0][0][0]
    mat_roi_3d_array = np.array([mat_roi])
    label = sitk.GetImageFromArray(mat_roi_3d_array)

    img_dir = Path(r'D:\exe_code\Python\17_Echinococcosis_ML\resources\all_images\IMGs_2022')
    img_name = Path(mat_data['roi'][0][0][3][0])
    img_path = img_dir / img_name.name
    img = Image.open(img_path)
    grey_img = img.convert('L')
    grey_img_array = np.array(grey_img)
    grey_img_3d_array = np.array([grey_img_array])
    img = sitk.GetImageFromArray(grey_img_3d_array)

    # 将数组写入文件
    converted_imgs = pathlib.Path('./resources/converted/imgs_nrrd_2022')
    converted_masks = pathlib.Path('./resources/converted/masks_nrrd_2022')
    sitk.WriteImage(img, converted_imgs / (stem + '.nrrd'))
    sitk.WriteImage(label, converted_masks / (stem + '.nrrd'))

    # 判断病灶类型，CE设为0，AE设为1
    if stem.startswith('B-'):
        label = 1
    elif stem.startswith('C-'):
        label = 1
    elif stem.startswith('R-'):
        label = 0
    elif stem.startswith('M-'):
        label = 0
    else:
        label = -1
        print(stem, '出错了')

    # 制作成组表,方便查找
    group_dict = {
        'img': converted_imgs / (stem + '.nrrd'),
        'mask': converted_masks / (stem + '.nrrd'),
        'label': label,
        'stem': stem
    }

    return group_dict


if __name__ == '__main__':
    masks_path = Path('./resources/all_images/MASKs_2022')
    finding_list = []

    for i in masks_path.iterdir():
        group_dict = mat_to_nrrd(str(i.absolute()))
        finding_list.append(group_dict)

    finding_list_pkl = pathlib.Path('resources/extract_data/finding_list_2022.pkl')
    with open(finding_list_pkl, 'wb') as f:
        pickle.dump(finding_list, f)
