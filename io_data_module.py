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
                xy = line.split(" ")
                dataset.append(tuple(xy))
    except Exception as ex:
        print(ex.args)
    finally:
        if file:
            file.close()
    return dataset


def write_to_file(dataset, dimension):
    formatted_dataset = stringify_dataset(dataset)
    filename = 'output_' + str(dimension) + 'D.txt'

    f = open(filename, 'w')
    f.write(formatted_dataset)
    f.close()


def stringify_dataset(dataset):
    formatted_dataset = ''''''
    for point, color in dataset:
        tuple_string = str(point)
        formatted_dataset += ("The unknown point " + tuple_string + " falls in " + color + " class\n")

    return formatted_dataset
