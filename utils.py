import os

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


def texture_exist(folder_num, object_name, texture_quantity, base_dir):
    e = True
    for i in range(texture_quantity):
        i += 1
        path = str(f'{base_dir}/' + str(folder_num) + '/' + object_name + '_tex' + str(i) + '.png')
        if not os.path.exists(path):
            e = False
    return e