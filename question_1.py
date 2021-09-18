import io_data_module as io
from renderer import render_graph
from nearest_neighbor import generate_nearest_neighborhood_dataset, generate_neighborhood_dataset

dimension = input("enter dimension of data (2/4/8): ")

dataSet_red = io.read_multi_dim_data("datasets/nearest-neighbor/red_" + str(dimension) + "d.txt")
dataSet_blue = io.read_multi_dim_data("datasets/nearest-neighbor/blue_" + str(dimension) + "d.txt")
dataset_unknown = io.read_multi_dim_data("datasets/nearest-neighbor/unknown_" + str(dimension) + "d.txt")

nearest_dataset = generate_nearest_neighborhood_dataset(dataset_unknown, dataSet_red, dataSet_blue)

neighborhood_dataset = generate_neighborhood_dataset(dataset_unknown, nearest_dataset)

io.write_to_file(neighborhood_dataset, dimension)

# render_graph(dataSet_red, dataSet_blue, dataset_unknown, nearest_dataset)
