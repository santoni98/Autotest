# СЧЕТЧИК ОБЪЕКТОВ В .obj ФАЙЛЕ

def obj_objects_counter(args):
    objFile = open(args, 'r')
    objCount = 0

    for line in objFile:
        split = line.split()
        if not len(split):
            continue
        if split[0] == "o":
            objCount += 1

    return objCount
