# ОПРЕДЕЛЕНИЕ ФИЗ МАСШТАБА МОДЕЛИ

def obj_scale(args):
    obj_file = open(args, 'r')

    scale = 0  # искомый масштаб в метрах
    #
    x_min = 0
    x_max = 0
    #
    y_min = 0
    y_max = 0
    #
    z_min = 0
    z_max = 0

    for line in obj_file:
        split = line.split()
        if not len(split):
            continue
        if split[0] == "v":
            # split[1]==x
            if float(split[1]) > x_max:
                x_max = float(split[1])
            if float(split[1]) < x_min:
                x_min = float(split[1])
            # split[2]==y
            if float(split[2]) > y_max:
                y_max = float(split[2])
            if float(split[2]) < y_min:
                y_min = float(split[2])
            # split[3]==z
            if float(split[3]) > z_max:
                z_max = float(split[3])
            if float(split[3]) < z_min:
                z_min = float(split[3])
    scale = x_max - x_min
    if y_max - y_min > scale:
        scale = y_max - y_min
    if z_max - z_min > scale:
        scale = z_max - z_min

    return scale
