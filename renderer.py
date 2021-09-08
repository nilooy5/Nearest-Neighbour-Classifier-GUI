from tkinter import *

tk = Tk()
tk.title("Nearest Neighbor Classifier")

window = Canvas(tk, bg="white", height=700, width=1000)
radius = 3.5
scale = 50
offset = 300


def render_graph(dataset_red, dataset_blue, unknown_tuple, nearest_tuple, nearest_tuple_color):
    render_points(dataset_red, dataset_blue)
    render_line_with_nearest_neighbor(unknown_tuple, nearest_tuple, nearest_tuple_color)


def render_points(dataset_red, dataset_blue):
    # draw red dataset
    for item in dataset_red:
        window.create_oval(float(item[0]) * scale - radius + offset,
                           float(item[1]) * scale - radius + offset,
                           float(item[0]) * scale + radius + offset,
                           float(item[1]) * scale + radius + offset,
                           outline="black", fill="red")

    # draw blue dataset
    for item in dataset_blue:
        window.create_oval(float(item[0]) * scale - radius + offset,
                           float(item[1]) * scale - radius + offset,
                           float(item[0]) * scale + radius + offset,
                           float(item[1]) * scale + radius + offset,
                           outline="black", fill="blue")


def render_line_with_nearest_neighbor(unknown_tuple, nearest_tuple, nearest_tuple_color):
    # create line between unknown & nearest tuple
    window.create_line(float(unknown_tuple[0]) * scale + offset,
                       float(unknown_tuple[1]) * scale + offset,
                       float(nearest_tuple[0]) * scale + offset,
                       float(nearest_tuple[1]) * scale + offset,
                       fill="black")

    # create oval for unknown tuple
    window.create_oval(float(unknown_tuple[0]) * scale - radius + offset,
                       float(unknown_tuple[1]) * scale - radius + offset,
                       float(unknown_tuple[0]) * scale + radius + offset,
                       float(unknown_tuple[1]) * scale + radius + offset,
                       outline="black", fill=nearest_tuple_color)
    # create label for unknown tuple
    window.create_text(float(unknown_tuple[0]) * scale - radius + offset,
                       float(unknown_tuple[1]) * scale - radius + offset,
                       text=str(unknown_tuple) + nearest_tuple_color)

    # create oval for nearest tuple
    window.create_oval(float(nearest_tuple[0]) * scale - radius + offset,
                       float(nearest_tuple[1]) * scale - radius + offset,
                       float(nearest_tuple[0]) * scale + radius + offset,
                       float(nearest_tuple[1]) * scale + radius + offset,
                       outline="black", fill=nearest_tuple_color)
    # create label for nearest tuple
    window.create_text(float(nearest_tuple[0]) * scale - radius + offset,
                       float(nearest_tuple[1]) * scale - radius + offset,
                       text=str(nearest_tuple) + nearest_tuple_color)
    window.pack()
    tk.mainloop()
