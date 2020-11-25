# ПРОВЕРКА НА ОТЛИЧИЕ ТЕКСТУР

from PIL import Image


def texture_difference(arg1, arg2):
    # 1
    img1 = Image.open("choker.png")  # Проверить jpg/png

    # 2
    img2 = Image.open("choker.png")  # Проверить jpg/png

    check = True
    if img1 == img2:
        check = False
        # print("Fuck its fake")
    return check  # False - изобр одинаковы
