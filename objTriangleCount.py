# СЧЕТЧИК ТРЕУГОЛЬНИКОВ
def obj_triangle_count(args):
    obj_file = open(args, 'r')
    triangles = 0  # Треугольники

    # обернуть в try catch(ошибка при выдаче img как obj)
    for line in obj_file:
        split = line.split()
        if not len(split):
            continue
        if split[0] == "f":
            triangles += len(split[1:])

    return triangles
