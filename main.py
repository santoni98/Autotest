import os
import shutil
import zipfile
import json
from objObjectsCounter import obj_objects_counter
from objTriangleCount import obj_triangle_count
from textureFill import texture_fill
from textureMainCheck import texture_main_check


# obj Unit 1
def obj(arg1, arg2):
    temp = obj_triangle_count(arg1)
    constant_tris1 = arg2
    points = 0
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
        path = str('zip/' + str(folder_num) + '/' + object_name + '_tex' + str(i) + '.png')
        if not os.path.exists(path):
            e = False
    return e


# Получить баллы за все текстуры в папке Unit 1
def get_texture_points(folder_num, object_name, texture_quantity):
    temp = 10
    for i in range(texture_quantity):
        i += 1
        path = str('zip/' + str(folder_num) + '/' + object_name + '_tex' + str(i) + '.png')
        if temp > points_texture_count(path):
            temp = points_texture_count(path)
    temp *= texture_quantity
    return temp


# Получить баллы за одну текстуру Unit 1
def points_texture_count(arg):
    points = 0
    if texture_main_check(arg):
        points += 1
        if texture_fill(arg) > 0.65:
            points += 1
    return points


def main():
    # get zip archive
    if os.path.exists('models.zip'):
        with zipfile.ZipFile("models.zip", "r") as zip_ref:
            zip_ref.extractall("zip")

    #filename = "unit1.json"
    #myfile = open(filename)

    with open("unit1.json", "r") as myfile:
        data = json.load(myfile)


    folder_num = data[0]
    object_name = data[1]
    texture_quantity = data[2]

    score = 0  # Баллы

    # Сделать проверку содержимого архива
    if os.path.exists('zip/1/wall_simple.obj'):
        if obj_objects_counter('zip/1/wall_simple.obj') == 1:
            score += obj('zip/1/wall_simple.obj', 100)
            # Проверка текстуры
            # 1 2 3
            if texture_exist(folder_num["folder_num1"], object_name["object_name1"],
                             texture_quantity["texture_quantity1"]):
                score += get_texture_points(folder_num["folder_num1"],
                                            object_name["object_name1"],
                                            texture_quantity["texture_quantity1"])
    print(score)

    if os.path.exists('zip/2/wall_lux.obj'):
        if obj_objects_counter('zip/2/wall_lux.obj') == 1:
            score += obj('zip/2/wall_lux.obj', 150)
            # Проверка текстуры
            # 1 2
            if texture_exist(folder_num["folder_num2"], object_name["object_name2"],
                             texture_quantity["texture_quantity2"]):
                score += get_texture_points(folder_num["folder_num2"],
                                            object_name["object_name2"],
                                            texture_quantity["texture_quantity2"])
    print(score)

    if os.path.exists('zip/3/wall_simple_window.obj'):
        if obj_objects_counter('zip/3/wall_simple_window.obj') == 1:
            score += obj('zip/3/wall_simple_window.obj', 150)
            # Проверка текстуры
            # 1 2 3
            if texture_exist(folder_num["folder_num3"], object_name["object_name3"],
                             texture_quantity["texture_quantity3"]):
                score += get_texture_points(folder_num["folder_num3"],
                                            object_name["object_name3"],
                                            texture_quantity["texture_quantity3"])
    print(score)

    if os.path.exists('zip/4/wall_lux_window.obj'):
        if obj_objects_counter('zip/4/wall_lux_window.obj') == 1:
            score += obj('zip/4/wall_lux_window.obj', 300)
            # Проверка текстуры
            # 1 2
            if texture_exist(folder_num["folder_num4"], object_name["object_name4"],
                             texture_quantity["texture_quantity4"]):
                score += get_texture_points(folder_num["folder_num4"],
                                            object_name["object_name4"],
                                            texture_quantity["texture_quantity4"])
    print(score)

    if os.path.exists('zip/5/roof_simple.obj'):
        if obj_objects_counter('zip/5/roof_simple.obj') == 1:
            score += obj('zip/5/roof_simple.obj', 200)
            # Проверка текстуры
            # 1
            if texture_exist(folder_num["folder_num5"], object_name["object_name5"],
                             texture_quantity["texture_quantity5"]):
                score += get_texture_points(folder_num["folder_num5"],
                                            object_name["object_name5"],
                                            texture_quantity["texture_quantity5"])
    print(score)

    if os.path.exists('zip/6/roof_lux.obj'):
        if obj_objects_counter('zip/6/roof_lux.obj') == 1:
            score += obj('zip/6/roof_lux.obj', 300)
            # Проверка текстуры
            # 1
            if texture_exist(folder_num["folder_num6"], object_name["object_name6"],
                             texture_quantity["texture_quantity6"]):
                score += get_texture_points(folder_num["folder_num6"],
                                            object_name["object_name6"],
                                            texture_quantity["texture_quantity6"])
    print(score)

    if os.path.exists('zip/7/roof_booth.obj'):
        if obj_objects_counter('zip/7/roof_booth.obj') == 1:
            score += obj('zip/7/roof_booth.obj', 200)
            # Проверка текстуры
            # 1 2 3
            if texture_exist(folder_num["folder_num7"], object_name["object_name7"],
                             texture_quantity["texture_quantity7"]):
                score += get_texture_points(folder_num["folder_num7"],
                                            object_name["object_name7"],
                                            texture_quantity["texture_quantity7"])
    print(score)

    if os.path.exists('zip/8/window_simple.obj'):
        if obj_objects_counter('zip/8/window_simple.obj') == 1:
            score += obj('zip/8/window_simple.obj', 150)
            # Проверка текстуры
            # 1
            if texture_exist(folder_num["folder_num8"], object_name["object_name8"],
                             texture_quantity["texture_quantity8"]):
                score += get_texture_points(folder_num["folder_num8"],
                                            object_name["object_name8"],
                                            texture_quantity["texture_quantity8"])
    print(score)

    if os.path.exists('zip/9/window_mid.obj'):
        if obj_objects_counter('zip/9/window_mid.obj') == 1:
            score += obj('zip/9/window_mid.obj', 200)
            # Проверка текстуры
            # 1
            if texture_exist(folder_num["folder_num9"], object_name["object_name9"],
                             texture_quantity["texture_quantity9"]):
                score += get_texture_points(folder_num["folder_num9"],
                                            object_name["object_name9"],
                                            texture_quantity["texture_quantity9"])
    print(score)

    if os.path.exists('zip/10/window_lux.obj'):
        if obj_objects_counter('zip/10/window_lux.obj') == 1:
            score += obj('zip/10/window_lux.obj', 300)
            # Проверка текстуры
            # 1
            if texture_exist(folder_num["folder_num10"], object_name["object_name10"],
                             texture_quantity["texture_quantity10"]):
                score += get_texture_points(folder_num["folder_num10"],
                                            object_name["object_name10"],
                                            texture_quantity["texture_quantity10"])

    shutil.rmtree("zip")
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
