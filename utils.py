import os

from textureDifference import texture_difference


def textures_valid(dir_path: str, object_name: str, texture_quantity: int):
    path1 = f'{dir_path}/{object_name}_tex1.png'
    path2 = f'{dir_path}/{object_name}_tex2.png'
    path3 = f'{dir_path}/{object_name}_tex3.png'

    check = True
    if texture_quantity == 2:
        check = texture_difference(path1, path2)
    if texture_quantity == 3:
        check = texture_difference(path1, path3) and texture_difference(path2, path3)
    return check


def texture_exist(folder_num, object_name, texture_quantity, base_dir):
    e = True
    for i in range(texture_quantity):
        i += 1
        path = f'{base_dir}/{folder_num}/{object_name}_tex{i}.png'
        if not os.path.exists(path):
            e = False
    return e