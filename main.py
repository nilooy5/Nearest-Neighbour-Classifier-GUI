import io_data_module as io
from tkinter import *
from nearest_neighbor import find_nearest_neighbor

dataSet = io.read_multi_dim_data("other_datasets/ellipse1.txt")

tk_window = Tk()

unknown_tuple = (5.0, 7.0)

nearest_tuple = find_nearest_neighbor(unknown_tuple, dataSet)

c = Canvas(tk_window, bg="white", height=700, width=1000)
radius = 1.5
scale = 50
offset = 300

for item in dataSet:
    c.create_oval(float(item[0]) * scale - radius + offset,
                  float(item[1]) * scale - radius + offset,
                  float(item[0]) * scale + radius + offset,
                  float(item[1]) * scale + radius + offset,
                  outline="red", fill="red")
c.create_line(float(unknown_tuple[0]) * scale - radius + offset,
              float(unknown_tuple[1]) * scale - radius + offset,
              float(nearest_tuple[0]) * scale - radius + offset,
              float(nearest_tuple[1]) * scale - radius + offset,
              fill="blue")
c.create_oval(float(unknown_tuple[0]) * scale - radius + offset,
                  float(unknown_tuple[1]) * scale - radius + offset,
                  float(unknown_tuple[0]) * scale + radius + offset,
                  float(unknown_tuple[1]) * scale + radius + offset,
                  outline="blue", fill="white")
c.create_oval(float(nearest_tuple[0]) * scale - radius + offset,
                  float(nearest_tuple[1]) * scale - radius + offset,
                  float(nearest_tuple[0]) * scale + radius + offset,
                  float(nearest_tuple[1]) * scale + radius + offset,
                  outline="blue", fill="blue")
c.pack()
tk_window.mainloop()