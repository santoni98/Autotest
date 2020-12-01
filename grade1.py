import json
import os
import shutil
import zipfile
from typing import List, Dict, Any

from objObjectsCounter import obj_objects_counter
from objTriangleCount import obj_triangle_count
from textureFill import texture_fill
from textureMainCheck import texture_main_check
from textureSolidColor import texture_solid_color
from utils import textures_valid, texture_exist


# obj Unit 1
def obj(arg1, arg2):
    temp = obj_triangle_count(arg1)
    constant_tris1 = arg2
    points = 0
    if obj_objects_counter(arg1) == 1:
        if temp >= constant_tris1 * 0.1:
            if temp < constant_tris1 * 1.75:
                points += 1
                if temp > constant_tris1:
                    points += 1
    return points


# Получить баллы за все текстуры в папке Unit 1
def get_texture_points(folder_num: int, object_name: str, texture_quantity: int, base_dir: str):
    temp = 10
    for i in range(texture_quantity):
        i += 1
        path = f'{base_dir}/{folder_num}/{object_name}_tex{i}.png'
        temp = min(points_texture_count(path), temp)
    temp *= texture_quantity
    return temp


# Получить баллы за одну текстуру Unit 1
def points_texture_count(arg):
    points = 0
    if texture_solid_color(arg):
        if texture_main_check(arg):
            points += 1
            if texture_fill(arg) > 0.65:
                points += 1
    return points


def grade_1(zip_path):
    # get zip archive
    base_dir = 'zip1'
    # обернуть в try except(ошибка при выдаче левого файла как zip)
    if os.path.exists(zip_path):
        if zipfile.is_zipfile(zip_path):
            with zipfile.ZipFile(zip_path, "r") as zip_ref:
                zip_ref.extractall(base_dir)

    with open("unit1.json", "r") as file:
        data: List[Dict[str, Any]] = json.load(file)

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
        score += obj(model_path, triangles)
        if texture_exist(num, obj_name, texture_quantity, base_dir):
            if textures_valid(dir_path, obj_name, texture_quantity):
                score += get_texture_points(num, obj_name, texture_quantity, base_dir)

    shutil.rmtree(base_dir)

    score = max(0, score)
    score = min(score, 40)
    return score / 40


if __name__ == '__main__':
    print(grade_1("models.zip"))
