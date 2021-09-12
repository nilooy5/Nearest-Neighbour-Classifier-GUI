import io_data_module as io
import renderer as render


dataset_2c_2d = io.read_multi_dim_data("datasets/K-means/data_4c_4d.txt")

render.render_points(dataset_2c_2d, "blue")

render.run_tk_window()
