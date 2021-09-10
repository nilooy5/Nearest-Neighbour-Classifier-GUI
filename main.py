import io_data_module as io
from renderer import render_graph
from nearest_neighbor import find_nearest_neighbor

dataSet_red = io.read_multi_dim_data("datasets/nearest-neighbor/red_4d.txt")
dataSet_blue = io.read_multi_dim_data("datasets/nearest-neighbor/blue_4d.txt")
dataset_unknown = io.read_multi_dim_data("datasets/nearest-neighbor/unknown_4d.txt")

nearest_dataset = find_nearest_neighbor(dataset_unknown, dataSet_red, dataSet_blue)

render_graph(dataSet_red, dataSet_blue, dataset_unknown, nearest_dataset)