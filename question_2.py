import io_data_module as io
import renderer as render
from k_means_clustering import find_closest_cluster_center

dataset = io.read_multi_dim_data("datasets/K-means/data_2c_2d.txt")

new_dataset = find_closest_cluster_center(dataset,[(5.0, 6.0), (7.0, -1.0)])

render.render_points(dataset, "blue")

render.run_tk_window()
