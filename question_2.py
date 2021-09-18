import io_data_module as io
import renderer as render
from k_means_clustering import find_cluster_for_random_center

num_of_centers = int(input("Enter number of centers: "))
dimensions = int(input("Enter dimension: "))

dataset = io.read_multi_dim_data("datasets/K-means/data_" + str(num_of_centers) + "c_" + str(dimensions) + "d.txt")

initial_points = [(0.02, 0.82), (-0.004, 4.3), (3.8955, 2.392), (0.1, 2.1)]

final_clusters = find_cluster_for_random_center(dataset, initial_points)[0]

render.render_clusters(final_clusters)

render.run_tk_window()
