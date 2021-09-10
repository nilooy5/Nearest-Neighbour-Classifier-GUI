import io_data_module as io
import random
from renderer import render_graph
from nearest_neighbor import find_nearest_neighbor

dataSet_red = io.read_multi_dim_data("datasets/nearest-neighbor/red_2d.txt")
dataSet_blue = io.read_multi_dim_data("datasets/nearest-neighbor/blue_2d.txt")
dataset_unknown = io.read_multi_dim_data("datasets/nearest-neighbor/unknown_2d.txt")

unknown_tuple = (random.uniform(-6.0, 6.0), random.uniform(-6.0, 6.0))

nearest_dataset = find_nearest_neighbor(dataset_unknown, dataSet_red, dataSet_blue)

render_graph(dataSet_red, dataSet_blue, dataset_unknown, nearest_dataset)