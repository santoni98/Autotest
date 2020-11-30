import os
import shutil
import zipfile
import json
from objObjectsCounter import obj_objects_counter
from objTriangleCount import obj_triangle_count
from textureDifference import texture_difference
from textureFill import texture_fill
from textureMainCheck import texture_main_check
from textureSolidColor import texture_solid_color


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


# Проверка наличия всех текстур в папке. Unit 1
def texture_exist(folder_num, object_name, texture_quantity):
    e = True
    for i in range(texture_quantity):
        i += 1
        path = str('zip1/' + str(folder_num) + '/' + object_name + '_tex' + str(i) + '.png')
        if not os.path.exists(path):
            e = False
    return e


# Проверка на схожесть текстур в папке
def textures_valid(dir_path, object_name, texture_quantity):
    path1 = str(dir_path + '/' + object_name + '_tex1.png')
    path2 = str(dir_path + '/' + object_name + '_tex2.png')
    path3 = str(dir_path + '/' + object_name + '_tex3.png')

    check = True
    if texture_quantity == 2:
        check = texture_difference(path1, path2)
    if texture_quantity == 3:
        check = texture_difference(path1, path3) and texture_difference(path2, path3)
    return check


# Получить баллы за все текстуры в папке Unit 1
def get_texture_points(folder_num, object_name, texture_quantity):
    temp = 10
    for i in range(texture_quantity):
        i += 1
        path = str('zip1/' + str(folder_num) + '/' + object_name + '_tex' + str(i) + '.png')
        if temp > points_texture_count(path):
            temp = points_texture_count(path)
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


def main():
    # get zip archive
    # обернуть в try except(ошибка при выдаче левого файла как zip)
    if os.path.exists('models.zip'):
        with zipfile.ZipFile("models.zip", "r") as zip_ref:
            zip_ref.extractall("zip1")

    with open("unit1.json", "r") as myfile:
        data = json.load(myfile)

    score = 0
    for line in data:
        num = line["num"]
        dir_path = f'zip1/{line["num"]}'
        obj_name = line["obj_name"]
        texture_quantity = line["texture_quantity"]
        triangles = line["triangles"]
        model_path = f'{dir_path}/{obj_name}.obj'
        if not os.path.exists(model_path):
            continue
        score += obj(model_path, triangles)
        if texture_exist(num, obj_name, texture_quantity):
            if textures_valid(dir_path, obj_name, texture_quantity):
                score += get_texture_points(num, obj_name, texture_quantity)

    shutil.rmtree("zip1")
    # Вывод Баллов (Unit 1)
    if score < 0:
        score = 0
    if score > 40:
        score = 40
    score /= 100
    print(score)


if __name__ == '__main__':
    main()
