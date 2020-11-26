# ПРОЦЕНТ ЗАПОЛНЕННОСТИ РАЗВЕРТКИ(ТЕКСТУРЫ)
from PIL import Image


def texture_fill(args):
    img = Image.open(args).convert("RGBA")  # Проверить jpg/png
    new_img = Image.new('RGB', img.size, (255, 255, 255))
    new_img.paste(img, (0, 0), img)

    white_pixels = 0
    all_pixels = new_img.size[0] * new_img.size[1]

    for k in range(new_img.size[1]):
        current_row = [new_img.getpixel((i, k)) for i in range(new_img.size[0])]
        white_pixels += current_row.count((255, 255, 255))
    if white_pixels < all_pixels*0.03:
        white_pixels = all_pixels
    percent_whtpxls = round(1 - white_pixels / all_pixels, 2)

    return percent_whtpxls
