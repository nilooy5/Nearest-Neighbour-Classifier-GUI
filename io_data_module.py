def read_multi_dim_data(filename):
    file = None
    dataset = []

    try:
        file = open(filename, "r")

        while True:
            line = file.readline()
            if len(line) == 0 or line == "\n":
                break
            else:
                line = line.removesuffix("\n")
                xy = line.split(",")
                dataset.append(tuple(xy))
            # dataset.append((float(xy[0]), float(xy[1]), float(xy[2]), float(xy[3]), xy[4]))
    except Exception as ex:
        print(ex.args)
    finally:
        if file:
            file.close()
    return dataset
