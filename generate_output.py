def write_to_file(dataset, dimension):
    filename = 'output_' + str(dimension) + 'D.txt'
    f = open(filename, 'w')
    f.write(str(dataset))
    f.close()
    # for item in dataset:
    #     print("point:", str(item[:-1]))

