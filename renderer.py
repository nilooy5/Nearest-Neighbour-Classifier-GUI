from tkinter import *

tk_window = Tk()


def render_points(dataSet, unknown_tuple, nearest_tuple):
    c = Canvas(tk_window, bg="white", height=700, width=1000)
    radius = 3.5
    scale = 50
    offset = 300

    for item in dataSet:
        c.create_oval(float(item[0]) * scale - radius + offset,
                      float(item[1]) * scale - radius + offset,
                      float(item[0]) * scale + radius + offset,
                      float(item[1]) * scale + radius + offset,
                      outline="black", fill="red")

    c.create_line(float(unknown_tuple[0]) * scale + offset,
                  float(unknown_tuple[1]) * scale + offset,
                  float(nearest_tuple[0]) * scale + offset,
                  float(nearest_tuple[1]) * scale + offset,
                  fill="blue")

    c.create_oval(float(unknown_tuple[0]) * scale - radius + offset,
                  float(unknown_tuple[1]) * scale - radius + offset,
                  float(unknown_tuple[0]) * scale + radius + offset,
                  float(unknown_tuple[1]) * scale + radius + offset,
                  outline="black", fill="white")

    c.create_oval(float(nearest_tuple[0]) * scale - radius + offset,
                  float(nearest_tuple[1]) * scale - radius + offset,
                  float(nearest_tuple[0]) * scale + radius + offset,
                  float(nearest_tuple[1]) * scale + radius + offset,
                  outline="black", fill="blue")
    c.pack()
    tk_window.mainloop()
