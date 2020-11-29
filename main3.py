import json
import os
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


def main3():
    # get zip archive
    # обернуть в try except(ошибка при выдаче левого файла как zip)
    if os.path.exists('models.zip'):
        with zipfile.ZipFile("builds.zip", "r") as zip_ref:
            zip_ref.extractall("zip3")

    with open("unit3.json", "r") as myfile:
        data = json.load(myfile)

    score = 0
    for line in data:
        num = line["num"]
        dir_path = f'zip3/{line["num"]}'
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
        if num < 3:
            score += big_triangle_count(model_path, tris_checkpoint1, tris_checkpoint2, tris_checkpoint3, tris_checkpoint4)
            score += big_objects_counter(model_path, obj_checkpoint1, obj_checkpoint2, obj_checkpoint3, obj_checkpoint4)
        if num == 4:
            unique_triangle_count(model_path, tris_checkpoint2, tris_checkpoint3)

    # shutil.rmtree("zip")
    # Вывод Баллов (Unit 1)
    if score < 0:
        score = 0
    if score > 40:
        score = 40
    score /= 100
    print(score)


if __name__ == '__main__':
    main3()
