import json
import math
import os
import shutil
import zipfile

from objObjectsCounter import obj_objects_counter
from objScale import obj_scale
from objTriangleCount import obj_triangle_count
from textureFill import texture_fill
from textureMainCheck import texture_main_check
from textureSolidColor import texture_solid_color
from utils import textures_valid, texture_exist


# Баллы за идентичную длину дорог в 1,2,3 папках
def length_roads_equally2_1(base_dir):
    points = 0
    # обернуть в try exception
    if obj_scale(f"{base_dir}/1/road1.obj") == obj_scale(f"{base_dir}/2/road2.obj"):
        if obj_scale(f"{base_dir}/1/road1.obj") == obj_scale(f"{base_dir}/3/road3.obj"):
            points += 3
    return points


# Сравнение треугольников в 1,2,3 папках
def obj2_1(name, triangles):
    points = 0
    if obj_objects_counter(name) == 1:
        if obj_triangle_count(name) > triangles:
            if obj_triangle_count(name) < triangles * 3:
                points += 1
    return points


# Определение длины модельки в 1,2,3 папках
def separate_scale2_1(name):
    points = 0
    if obj_objects_counter(name) == 1:
        if obj_scale(name) >= 4.9:
            if obj_scale(name) >= 5.1:
                points += 1
    return points


# Получить баллы за все текстуры в папке Unit 2_1
def get_texture_points2_1(folder_num, object_name, texture_quantity, base_dir):
    temp = 10
    for i in range(texture_quantity):
        i += 1
        path = str(f'{base_dir}/' + str(folder_num) + '/' + object_name + '_tex' + str(i) + '.png')
        if temp > points_texture_count2_1(path):
            temp = points_texture_count2_1(path)
    return temp


# Получить баллы за одну текстуру Unit 2_1
def points_texture_count2_1(arg):
    points = 0
    if texture_solid_color(arg):
        if texture_main_check(arg):
            if texture_fill(arg) > 0.65:
                points += 1
    return points


# obj Unit 2
def obj2(arg1, arg2):
    temp = obj_triangle_count(arg1)
    constant_tris1 = arg2
    points = 0
    if obj_objects_counter(arg1) == 1:
        if temp >= constant_tris1 * 0.1:
            if temp < constant_tris1 * 2.5:
                points += 1
                if temp > constant_tris1:
                    points += 1
    return points


# Получить баллы за все текстуры в папке Unit 2
def get_texture_points2(folder_num, object_name, texture_quantity, base_dir):
    temp = 10
    for i in range(texture_quantity):
        i += 1
        path = f'{base_dir}/{folder_num}/{object_name}_tex{i}.png'
        if temp > points_texture_count2(path):
            temp = points_texture_count2(path)
    temp *= texture_quantity
    return temp


# Получить баллы за одну текстуру Unit 2
def points_texture_count2(arg):
    points = 0
    if os.path.exists(arg):
        if texture_solid_color(arg):
            if texture_main_check(arg):
                points += 1
                if texture_fill(arg) > 0.65:
                    points += 1
    return points


def grade_2(zip_path):
    # get zip archive
    base_dir = 'zip2'
    # обернуть в try except(ошибка при выдаче левого файла как zip)
    if os.path.exists(zip_path):
        if zipfile.is_zipfile(zip_path):
            with zipfile.ZipFile(zip_path, "r") as zip_ref:
                zip_ref.extractall(base_dir)

    with open("unit2.json", "r") as myfile:
        data = json.load(myfile)

    score = 0
    helper_for_lengths = 0
    for line in data:
        num = line["num"]
        dir_path = f'{base_dir}/{num}'
        obj_name = line["obj_name"]
        texture_quantity = line["texture_quantity"]
        triangles = line["triangles"]
        model_path = f'{dir_path}/{obj_name}.obj'
        if not os.path.exists(model_path):
            continue

        # Получение баллов за первые 3 папки
        if 1 <= num <= 3:
            helper_for_lengths += 3
            score += obj2_1(model_path, triangles)
            if texture_exist(num, obj_name, texture_quantity, base_dir):
                if textures_valid(dir_path, obj_name, texture_quantity):
                    score += get_texture_points2_1(num, obj_name, texture_quantity)
        if helper_for_lengths == 3:
            score += length_roads_equally2_1(base_dir)

        if num > 3:
            score += obj2(model_path, triangles)
            if texture_exist(num, obj_name, texture_quantity, base_dir):
                if textures_valid(dir_path, obj_name, texture_quantity):
                    score += get_texture_points2(num, obj_name, texture_quantity, base_dir)

    shutil.rmtree(base_dir)
    # Вывод Баллов (Unit 2)
    score = max(0, score)
    score = min(score, 44)
    return score / 44


if __name__ == '__main__':
    print(grade_2("roads.zip"))
