# ПРОЦЕНТ ЗАПОЛНЕННОСТИ РАЗВЕРТКИ(ТЕКСТУРЫ)
from PIL import Image


def texture_fill(args):
    img = Image.open(args).convert("RGBA")  # Проверить jpg/png
    new_img = Image.new('RGB', img.size, (255, 255, 255))
    new_img.paste(img, (0, 0), img)

    # print(new_img.size)
    white_pixels = 0
    all_pixels = new_img.size[0] * new_img.size[1]

    for k in range(new_img.size[1]):
        current_row = [new_img.getpixel((i, k)) for i in range(new_img.size[0])]
        white_pixels += current_row.count((255, 255, 255))
        # print(current_row.count((255, 255, 255)))
    percent_whtpxls = round(1 - white_pixels / all_pixels, 2)

    return percent_whtpxls

# all_row = [[rgb_im.getpixel((i,0)) for i in range(rgb_im.size[0])] for i in range(rgb_im.size[1])]
# first_row.count((0,0,0)) # --> 628
# len(first_row) #--> 680

# print(all_row.count((255,255,255)))
# print(len(all_row))

# import cv2
# im = cv2.imread("image.png", cv2.IMREAD_UNCHANGED)

# alpha_index = img.getbands().index('A')
# print(alpha_index)

# new_img.save("test3424.jpg", quality=95)

# print(white_pixels)
