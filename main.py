import io_data_module as io
import random
from renderer import render_points
from nearest_neighbor import find_nearest_neighbor

dataSet_red = io.read_multi_dim_data("datasets/nearest-neighbor/red_2d.txt")
dataSet_blue = io.read_multi_dim_data("datasets/nearest-neighbor/blue_2d.txt")

unknown_tuple = (random.uniform(-6.0, 6.0), random.uniform(-6.0, 6.0))
print(unknown_tuple)

nearest_tuple = find_nearest_neighbor(unknown_tuple, dataSet_red, dataSet_blue)

render_points(dataSet_red, dataSet_blue, unknown_tuple, nearest_tuple[0], nearest_tuple[1])
