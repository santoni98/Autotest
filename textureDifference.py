# ПРОВЕРКА НА ОТЛИЧИЕ ТЕКСТУР
from PIL import Image


def texture_difference(arg1, arg2):
    # 1
    img1 = Image.open(arg1)

    # 2
    img2 = Image.open(arg2)

    check = True
    if img1 == img2:
        check = False
    return check  # False - изобр одинаковы
