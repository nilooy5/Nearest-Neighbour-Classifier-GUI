from tkinter import *

tk = Tk()
tk.title("Nearest Neighbor Classifier")

window = Canvas(tk, bg="white", height=700, width=1000)
radius = 3.5    # radius of the ovals
scale = 50      # can be compared to zoom
offset = 300    # to show the negative points


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


def render_line_with_nearest_neighbor(unknown_tuple, nearest_tuple, nearest_tuple_color):
    # create line between unknown & nearest tuple
    draw_line(nearest_tuple, unknown_tuple)

    # create oval for unknown tuple
    draw_oval(unknown_tuple, nearest_tuple_color)

    # create label for unknown tuple
    draw_label(unknown_tuple, nearest_tuple_color)

    # create oval for nearest tuple
    draw_oval(nearest_tuple, nearest_tuple_color)

    # create label for nearest tuple
    draw_label(nearest_tuple, nearest_tuple_color)


def draw_oval(item, color):
    window.create_oval(float(item[0]) * scale - radius + offset,
                       float(item[1]) * scale - radius + offset,
                       float(item[0]) * scale + radius + offset,
                       float(item[1]) * scale + radius + offset,
                       outline="black", fill=color)


def draw_label(nearest_tuple, nearest_tuple_color):
    window.create_text(float(nearest_tuple[0]) * scale - radius + offset,
                       float(nearest_tuple[1]) * scale - radius + offset,
                       text=str(nearest_tuple) + nearest_tuple_color)


def draw_line(nearest_tuple, unknown_tuple):
    window.create_line(float(unknown_tuple[0]) * scale + offset,
                       float(unknown_tuple[1]) * scale + offset,
                       float(nearest_tuple[0]) * scale + offset,
                       float(nearest_tuple[1]) * scale + offset,
                       fill="green")


def run_tk_window():
    window.pack()
    tk.mainloop()
