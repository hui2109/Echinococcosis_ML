from pathlib import Path

from PIL import Image, ImageChops


def cropImages(original_image_path: str, mask_image_path: str):
    # Load the original image and the mask image
    original_image_path = Path(original_image_path)
    mask_image_path = Path(mask_image_path)

    original_image = Image.open(original_image_path)
    mask_image = Image.open(mask_image_path)

    # Convert mask image to grayscale and threshold it to create a binary mask
    mask_image_gray = mask_image.convert('L')
    binary_mask = mask_image_gray.point(lambda x: 0 if x == 0 else 255, '1')

    # Crop the original image using the binary mask
    # Since the mask is green in the image, we should use the green channel as a mask
    masked_image = ImageChops.multiply(original_image.convert('RGB'), binary_mask.convert('RGB'))
    crop_image = masked_image.crop(masked_image.getbbox())

    return crop_image


if __name__ == '__main__':
    examination_2023_0 = Path('./examination_2023/0')
    examination_2023_1 = Path('./examination_2023/1')
    examination_2023_0.mkdir(parents=True, exist_ok=True)
    examination_2023_1.mkdir(parents=True, exist_ok=True)

    test_images_2023 = Path('./resources/all_images/IMGs_2023')
    test_masks_2023 = Path('./resources/all_images/Masks_2023')

    for img in test_images_2023.iterdir():
        if img.stem.startswith('B'):
            mask = test_masks_2023 / (img.stem + '.png')
            cropImages(str(img.resolve(strict=True)), str(mask.resolve(strict=True))).save(
                examination_2023_1 / (img.stem + '.gif'))
        else:
            mask = test_masks_2023 / (img.stem + '.png')
            cropImages(str(img.resolve(strict=True)), str(mask.resolve(strict=True))).save(
                examination_2023_0 / (img.stem + '.gif'))
