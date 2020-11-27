# ПРОВЕРКА НА СПЛОШНУЮ ТЕКСТУРУ
from PIL import Image


def texture_solid_color(args):
    img = Image.open(args).convert("RGBA")  # Проверить jpg/png
    new_img = Image.new('RGB', img.size, (255, 255, 255))
    new_img.paste(img, (0, 0), img)

    temp = new_img.getpixel((0, 0))

    liar = 0
    check = True

    for k in range(new_img.size[1]):
        for i in range(new_img.size[0]):
            current = new_img.getpixel((i, k))
            if current == temp:
                liar += 1
    if liar == new_img.size[0] * new_img.size[1]:
        check = False
    return check  # False-сплошная
