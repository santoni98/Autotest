# ОСНОВНАЯ ПРОВЕРКА ТЕКСТУРЫ
from PIL import Image


def texture_main_check(args):
    image = Image.open(args)  # Открываем изображение
    (width, height) = image.size  # Определяем ширину и высоту

    check = False
    actual_resolution = 16

    while actual_resolution <= 2048:
        if width == actual_resolution and height == actual_resolution:
            check = True
            actual_resolution = 4097
        actual_resolution *= 2

    return check
