# СЧЕТЧИК ТРЕУГОЛЬНИКОВ
def objTriangleCount(args):
    objFile = open(args, 'r')
    triangles = 0  # Треугольники

    for line in objFile:
        split = line.split()
        if not len(split):
            continue
        if split[0] == "f":
            triangles += len(split[1:])

    return triangles
