import io_data_module as io
import renderer as render
from k_means_clustering import find_cluster_for_random_center

dataset = io.read_multi_dim_data("datasets/K-means/data_2c_2d.txt")

final_clusters = find_cluster_for_random_center(dataset, [(5.0, 6.0), (7.0, -1.0)])[0]

for cluster in final_clusters:
    for item in final_clusters[cluster]:
        render.draw_line(item, cluster)
    render.render_points(final_clusters[cluster], "blue")
    render.render_points([cluster], "red")

render.run_tk_window()
