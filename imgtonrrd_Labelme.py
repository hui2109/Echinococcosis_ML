import pathlib
import pickle

import SimpleITK as sitk
import numpy as np
from PIL import Image


def image_to_nrrd():
    finding_list = []
    images_path = pathlib.Path('./resources/all_images/IMGs_2023')
    masks_path = pathlib.Path('./resources/all_images/MASKs_2023')

    for i in images_path.iterdir():
        img = Image.open(i)
        grey_img = img.convert('L')
        grey_img_array = np.array(grey_img)
        grey_img_3d_array = np.array([grey_img_array])
        img = sitk.GetImageFromArray(grey_img_3d_array)

        label_path = masks_path / (i.stem + '.png')
        label = Image.open(label_path)
        grey_label = label.convert('L')
        grey_label_array = np.array(grey_label)
        grey_label_3d_array = np.array([grey_label_array])
        grey_label_3d_array[grey_label_3d_array != 0] = 1
        label = sitk.GetImageFromArray(grey_label_3d_array)

        # 将数组写入文件
        converted_imgs = pathlib.Path('./resources/converted/imgs_nrrd_2023')
        converted_masks = pathlib.Path('./resources/converted/masks_nrrd_2023')
        sitk.WriteImage(img, converted_imgs / (i.stem + '.nrrd'))
        sitk.WriteImage(label, converted_masks / (i.stem + '.nrrd'))

        # 判断病灶类型，CE设为0，AE设为1
        if i.stem.startswith('B-'):
            label = 1
        elif i.stem.startswith('R-'):
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

    finding_list_pkl = pathlib.Path('resources/extract_data/finding_list_2023.pkl')
    with open(finding_list_pkl, 'wb') as f:
        pickle.dump(finding_list, f)


if __name__ == '__main__':
    image_to_nrrd()
