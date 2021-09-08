import io_data_module as io
from tkinter import *
from nearest_neighbor import find_nearest_neighbor

dataSet = io.read_multi_dim_data("other_datasets/ellipse1.txt")

tk_window = Tk()

unknown_tuple = (300.0, 300.0)

nearest_tuple = find_nearest_neighbor(unknown_tuple, dataSet)

c = Canvas(tk_window, bg="white", height=700, width=1000)
radius = 1.5
scale = 50

for item in dataSet:
    c.create_oval(float(item[0]) * scale - radius,
                  float(item[1]) * scale - radius,
                  float(item[0]) * scale + radius,
                  float(item[1]) * scale + radius,
                  outline="red", fill="red")
c.create_line(unknown_tuple[0], unknown_tuple[1], nearest_tuple[0], nearest_tuple[1], fill="blue")
c.create_oval(float(unknown_tuple[0]) * scale - radius,
                  float(unknown_tuple[1]) * scale - radius,
                  float(unknown_tuple[0]) * scale + radius,
                  float(unknown_tuple[1]) * scale + radius,
                  outline="blue", fill="blue")
c.pack()
tk_window.mainloop()