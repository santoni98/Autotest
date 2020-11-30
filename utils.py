import os

from objObjectsCounter import obj_objects_counter
from objTriangleCount import obj_triangle_count
from textureDifference import texture_difference


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


def obj(model_path: str, triangles, k: float):
    temp = obj_triangle_count(model_path)
    constant_tris1 = triangles
    points = 0
    if obj_objects_counter(model_path) == 1:
        if temp >= constant_tris1 * 0.1:
            if temp < constant_tris1 * k:
                points += 1
                if temp > constant_tris1:
                    points += 1
    return points


def get_texture_points(base_dir, folder_num, object_name, texture_quantity, grader):
    temp = 10
    for i in range(texture_quantity):
        i += 1
        path = str(f'{base_dir}/{folder_num}/{object_name}_tex{i}.png')
        grader_res = grader(path)
        temp = min(temp, grader_res)
    temp *= texture_quantity
    return temp


def texture_exist(base_folder, folder_num, object_name, texture_quantity):
    e = True
    for i in range(texture_quantity):
        i += 1
        path = f'{base_folder}/{folder_num}/{object_name}_tex{i}.png'
        if not os.path.exists(path):
            e = False
    return e