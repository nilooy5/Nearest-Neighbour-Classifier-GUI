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
    except Exception as ex:
        print(ex.args)
    finally:
        if file:
            file.close()
    return dataset
