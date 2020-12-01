import json
import os
import shutil
import math
import zipfile
from objObjectsCounter import obj_objects_counter
from objTriangleCount import obj_triangle_count


def unique_triangle_count(name, num2, num3):
    temp = obj_triangle_count(name)
    points = 0
    if num2 < temp < num3:
        points += 4
    return points


def big_triangle_count(name, num1, num2, num3, num4):
    temp = obj_triangle_count(name)
    points = 0
    if num1 < temp < num4:
        points += 1
        if num2 < temp < num3:
            points += 1
    return points


def big_objects_counter(name, num1, num2, num3, num4):
    temp = obj_objects_counter(name)
    points = 0
    if num1 < temp < num4:
        points += 1
        if num2 < temp < num3:
            points += 1
    return points


def grade_3(zip_path):
    # get zip archive
    base_dir = 'zip3'
    # обернуть в try except(ошибка при выдаче левого файла как zip)
    if os.path.exists(zip_path):
        if zipfile.is_zipfile(zip_path):
            with zipfile.ZipFile(zip_path, "r") as zip_ref:
                zip_ref.extractall(base_dir)

    with open("unit3.json", "r") as myfile:
        data = json.load(myfile)

    score = 0
    for line in data:
        num = line["num"]
        dir_path = f'{base_dir}/{num}'
        obj_name = line["obj_name"]
        tris_checkpoint1 = line["tris_checkpoint1"]
        tris_checkpoint2 = line["tris_checkpoint2"]
        tris_checkpoint3 = line["tris_checkpoint3"]
        tris_checkpoint4 = line["tris_checkpoint4"]
        obj_checkpoint1 = line["obj_checkpoint1"]
        obj_checkpoint2 = line["obj_checkpoint2"]
        obj_checkpoint3 = line["obj_checkpoint3"]
        obj_checkpoint4 = line["obj_checkpoint4"]
        model_path = f'{dir_path}/{obj_name}.obj'
        if not os.path.exists(model_path):
            continue
        if num < 4:
            score += big_triangle_count(model_path, tris_checkpoint1, tris_checkpoint2, tris_checkpoint3,
                                        tris_checkpoint4)
            score += big_objects_counter(model_path, obj_checkpoint1, obj_checkpoint2, obj_checkpoint3, obj_checkpoint4)
        if num == 4:
            score += unique_triangle_count(model_path, tris_checkpoint2, tris_checkpoint3)

    shutil.rmtree(base_dir)
    # Вывод Баллов (Unit 1)
    score = max(0, score)
    score = min(score, 16)
    score = math.floor(score / 16 * 100)  # колибровка баллов
    score /= 100
    print(score)


if __name__ == '__main__':
    grade_3("builds.zip")
