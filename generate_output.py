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
