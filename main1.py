import json
import os
import zipfile
from typing import List, Dict, Any

from textureFill import texture_fill
from textureMainCheck import texture_main_check
from textureSolidColor import texture_solid_color
from utils import textures_valid, obj, get_texture_points, texture_exist


# Получить баллы за одну текстуру Unit 1
def points_texture_count(arg):
    points = 0
    if texture_solid_color(arg):
        if texture_main_check(arg):
            points += 1
            if texture_fill(arg) > 0.65:
                points += 1
    return points


def main():
    # get zip archive
    base_dir = 'zip1'
    # обернуть в try except(ошибка при выдаче левого файла как zip)
    if os.path.exists('models.zip'):
        with zipfile.ZipFile("models.zip", "r") as zip_ref:
            zip_ref.extractall(base_dir)

    with open("unit1.json", "r") as myfile:
        data: List[Dict[str, Any]] = json.load(myfile)

    score = 0
    for line in data:
        num = line["num"]
        dir_path = f'{base_dir}/{num}'
        obj_name = line["obj_name"]
        texture_quantity = line["texture_quantity"]
        triangles = line["triangles"]
        model_path = f'{dir_path}/{obj_name}.obj'
        if not os.path.exists(model_path):
            continue
        score += obj(model_path, triangles, 1.75)
        if texture_exist(base_dir, num, obj_name, texture_quantity):
            if textures_valid(dir_path, obj_name, texture_quantity):
                score += get_texture_points(base_dir, num, obj_name, texture_quantity, points_texture_count)

    # shutil.rmtree("zip")
    # Вывод Баллов (Unit 1)
    score = max(0, score)
    score = min(score, 40)
    score /= 100
    print(score)


if __name__ == '__main__':
    main()

# print(textureMainCheck('zip/1/wall_simple_tex2.png'))

# ОБРАЩЕНИЕ К ФУНКЦИИ
# objObjectsCounter('zip/1/wall_simple.obj')
# objTriangleCount('zip/1/wall_simple.obj')
# objScale('zip/1/wall_simple.obj')
# textureMainCheck('zip/1/wall_simple_tex2.png')
# textureFill('zip/1/wall_simple_tex2.png')
# textureSolidColor('zip/1/wall_simple_tex2.png')
# textureDifference('zip/1/wall_simple_tex2.png', 'zip/1/wall_simple_tex2.png')

# УДАЛИТЬ ПАПКУ
# shutil.rmtree("10")
# os.remove("models.zip")

#
# obj:_______________________________________________
# -кол-во треугольников             +objTriangleCount
# -масштаб                          +objScale
# -кол-во объектов в obj            +objObjectsCounter
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# texture:___________________________________________
# -соотн стрн,степень 2,не > 2048   +textureMainCheck
# -заполненность текстуры(процент)  +textureFill
# -проверка на сплошную картинку    +textureSolidColor
# -проверка двух текстур на отличие +textureDifference
#
