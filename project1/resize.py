
from PIL import Image

from resizeimage import resizeimage


with open('ntu.jpg', 'r+b') as f:
    with Image.open(f) as image:
        cover = resizeimage.resize_cover(image, [400, 400])
        cover.save('nturesize.jpeg', image.format)