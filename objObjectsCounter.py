# СЧЕТЧИК ОБЪЕКТОВ В .obj ФАЙЛЕ

def obj_objects_counter(args):
    obj_file = open(args, 'r')
    obj_count = 0

    for line in obj_file:
        split = line.split()
        if not len(split):
            continue
        if split[0] == "o":
            obj_count += 1

    return obj_count
