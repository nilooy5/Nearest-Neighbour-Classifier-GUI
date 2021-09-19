from tkinter import *

tk = Tk()
# tk.title("Nearest Neighbor Classifier")

window = Canvas(tk, bg="white", height=700, width=1000)
radius = 3      # radius of the ovals
scale = 70      # can be compared to zoom
offset = 200    # to show the negative points
colors_set = ["grey", "magenta", "green", "orange"]     # color sets taken for drawing specific colors for a cluster


# renders graph for nearest neighbor
def render_graph(dataset_red, dataset_blue, dataset_unknown, nearest_dataset):
    render_points(dataset_red, "red")
    render_points(dataset_blue, "blue")
    for i in range(len(dataset_unknown)):
        render_line_with_nearest_neighbor(dataset_unknown[i], nearest_dataset[i][0], nearest_dataset[i][1])

    run_tk_window()


# draw a list dataset
def render_points(dataset, color):
    for item in dataset:
        draw_oval(item, color)


# takes an unknown tuple, nearest tuple and its class and then draws them
def render_line_with_nearest_neighbor(unknown_tuple, nearest_tuple, nearest_tuple_color):
    # create line between unknown & nearest tuple
    draw_line(nearest_tuple, unknown_tuple, "green")

    # create oval for unknown tuple
    draw_oval(unknown_tuple, nearest_tuple_color)

    # create label for unknown tuple
    draw_label(unknown_tuple, nearest_tuple_color)

    # create oval for nearest tuple
    draw_oval(nearest_tuple, nearest_tuple_color)

    # create label for nearest tuple
    draw_label(nearest_tuple, nearest_tuple_color)


# draws an oval for each points on the screen
def draw_oval(item, color):
    window.create_oval(float(item[0]) * scale - radius + offset,
                       float(item[1]) * scale - radius + offset,
                       float(item[0]) * scale + radius + offset,
                       float(item[1]) * scale + radius + offset,
                       outline="white", fill=color)


# writes label for a point and its class if string is passed
def draw_label(nearest_tuple, nearest_tuple_color):
    window.create_text(float(nearest_tuple[0]) * scale - radius + offset,
                       float(nearest_tuple[1]) * scale - radius + offset,
                       text=str(nearest_tuple) + nearest_tuple_color)


# draws line between two tuples and picks the color depending on the parameter
def draw_line(nearest_tuple, unknown_tuple, line_color):
    window.create_line(float(unknown_tuple[0]) * scale + offset,
                       float(unknown_tuple[1]) * scale + offset,
                       float(nearest_tuple[0]) * scale + offset,
                       float(nearest_tuple[1]) * scale + offset,
                       fill=line_color)


# renders clusters for k-means algorithm's resultant cluster set
def render_clusters(final_clusters):
    color_index = 0
    for cluster_center in final_clusters:
        for item in final_clusters[cluster_center]:
            draw_line(item, cluster_center, colors_set[color_index % 4])
        render_points(final_clusters[cluster_center], "blue")
        render_points([cluster_center], "red")
        draw_label(cluster_center, "")
        color_index += 1


def run_tk_window():
    window.pack()
    tk.mainloop()
