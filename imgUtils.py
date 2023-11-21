from PIL import Image


def compress_image(input_image_path, output_image_path):
    fileType = input_image_path.split(".")[-1]
    with Image.open(input_image_path) as image:
        image.save(output_image_path, fileType.upper(), optimize=True, quality=1)


keyToFunc = {
    'compress_image': compress_image
}