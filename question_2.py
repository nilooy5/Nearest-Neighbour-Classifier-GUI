#########################################
# Assignment 1 (Question 2)             #
# name:   Fazal Mahmud Niloy            #
# ID:     3228358                       #
# email:  u3228358@uni.canberra.edu.au  #
# Unit:   Programming for Data Science  #
# Course: Master of Data Science        #
# See README.MD for detailed instruction#
#########################################

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

render.render_clusters(final_clusters)

render.run_tk_window()
