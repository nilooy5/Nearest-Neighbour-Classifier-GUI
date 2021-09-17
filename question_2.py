import io_data_module as io
import renderer as render
from k_means_clustering import find_cluster_for_random_center

dataset = io.read_multi_dim_data("datasets/K-means/data_4c_2d.txt")

final_clusters = find_cluster_for_random_center(dataset, [(0.02, 0.82), (-0.004, 4.3), (3.8955, 2.392), (0.1, 2.1)])[0]

for cluster in final_clusters:
    for item in final_clusters[cluster]:
        render.draw_line(item, cluster)
    render.render_points(final_clusters[cluster], "blue")
    render.render_points([cluster], "red")
    render.draw_label(cluster, "")

render.run_tk_window()
