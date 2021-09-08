from tkinter import *

tk_window = Tk()


def render_points(dataSet_red, dataSet_blue, unknown_tuple, nearest_tuple, nearest_tuple_color):
    c = Canvas(tk_window, bg="white", height=700, width=1000)
    radius = 3.5
    scale = 50
    offset = 300

    for item in dataSet_red:
        c.create_oval(float(item[0]) * scale - radius + offset,
                      float(item[1]) * scale - radius + offset,
                      float(item[0]) * scale + radius + offset,
                      float(item[1]) * scale + radius + offset,
                      outline="black", fill="red")

    for item in dataSet_blue:
        c.create_oval(float(item[0]) * scale - radius + offset,
                      float(item[1]) * scale - radius + offset,
                      float(item[0]) * scale + radius + offset,
                      float(item[1]) * scale + radius + offset,
                      outline="black", fill="blue")

    c.create_line(float(unknown_tuple[0]) * scale + offset,
                  float(unknown_tuple[1]) * scale + offset,
                  float(nearest_tuple[0]) * scale + offset,
                  float(nearest_tuple[1]) * scale + offset,
                  fill="black")

    c.create_oval(float(unknown_tuple[0]) * scale - radius + offset,
                  float(unknown_tuple[1]) * scale - radius + offset,
                  float(unknown_tuple[0]) * scale + radius + offset,
                  float(unknown_tuple[1]) * scale + radius + offset,
                  outline="black", fill=nearest_tuple_color)

    c.create_oval(float(nearest_tuple[0]) * scale - radius + offset,
                  float(nearest_tuple[1]) * scale - radius + offset,
                  float(nearest_tuple[0]) * scale + radius + offset,
                  float(nearest_tuple[1]) * scale + radius + offset,
                  outline="black", fill=nearest_tuple_color)
    c.pack()
    tk_window.mainloop()
