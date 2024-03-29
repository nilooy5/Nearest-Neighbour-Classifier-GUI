import io_data_module as io
import renderer as render
from k_means_clustering import find_cluster_for_random_center


# change the file name to test other files like data_2c_2d.txt data_2c_4d.txt data_4c_4d.txt
dataset = io.read_multi_dim_data("datasets/K-means/data_4c_2d.txt")

# change initial points according to the file name
# points for 4C 2d
initial_points = [(0.02, 0.82), (-0.004, 4.3), (3.8955, 2.392), (0.1, 2.1)]

# points for 2C 2D
# initial_points = [(0.02, 0.82), (-0.004, 4.3)]

final_clusters = find_cluster_for_random_center(dataset, initial_points)[0]

# change the show_labels to "False" to turn off the coordinates of the centroids on XY plane
render.render_clusters(final_clusters, show_labels=True)

render.run_tk_window()
