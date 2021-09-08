import io_data_module as io
from renderer import render_points
from nearest_neighbor import find_nearest_neighbor

dataSet = io.read_multi_dim_data("other_datasets/ellipse1.txt")

unknown_tuple = (5.0, 7.0)

nearest_tuple = find_nearest_neighbor(unknown_tuple, dataSet)

render_points(dataSet, unknown_tuple, nearest_tuple)