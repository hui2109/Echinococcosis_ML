import pathlib
import os
import pickle

import SimpleITK as sitk
import numpy as np
from PIL import Image


def image_to_nrrd():
    finding_list = []
    images_path = pathlib.Path('./resources/all_images/IMGs')
    for i in images_path.iterdir():
        img = Image.open(i)
        grey_img = img.convert('L')
        grey_img_array = np.array(grey_img)
        img = sitk.GetImageFromArray(grey_img_array)

        temp = list(i.with_suffix('.gif').parts)
        temp[2] = 'MASKs'
        label = Image.open(pathlib.Path(*temp))
        grey_label_array = np.array(label)
        label = sitk.GetImageFromArray(grey_label_array)

        # 将数组写入文件
        converted_imgs = pathlib.Path('./resources/converted/imgs_nrrd_2D')
        converted_imgs.mkdir(parents=True, exist_ok=True)
        converted_masks = pathlib.Path('./resources/converted/masks_nrrd_2D')
        converted_masks.mkdir(parents=True, exist_ok=True)
        sitk.WriteImage(img, converted_imgs / (i.stem + '.nrrd'))
        sitk.WriteImage(label, converted_masks / (i.stem + '.nrrd'))

        # 判断病灶类型，CE设为0，AE设为1
        if i.stem.startswith('B-'):
            label = 1
        elif i.stem.startswith('C-'):
            label = 1
        elif i.stem.startswith('R-'):
            label = 0
        elif i.stem.startswith('M-'):
            label = 0
        else:
            label = -1
            print(i.stem, '出错了')

        # 制作成组表,方便查找
        group_dict = {
            'img': converted_imgs / (i.stem + '.nrrd'),
            'mask': converted_masks / (i.stem + '.nrrd'),
            'label': label,
            'stem': i.stem
        }
        finding_list.append(group_dict)

    finding_list_pkl = pathlib.Path('resources/extract_data/finding_list_2D.pkl')
    with open(finding_list_pkl, 'wb') as f:
        pickle.dump(finding_list, f)


if __name__ == '__main__':
    image_to_nrrd()
