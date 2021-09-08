import io_data_module as io
from tkinter import *

dataSet = io.read_multi_dim_data("iris.data")

tk_window = Tk()

c = Canvas(tk_window, bg="white", height=500, width=500)
radius = 1.5
spread = 50

for x, y, z, w, flower_class in dataSet:
    c.create_oval(x * spread - radius, y * spread - radius, x * spread + radius, y * spread + radius, outline="red", fill="red")

c.create_oval(100 - radius, 200 - radius, 100 + radius, 200 + radius, outline="blue", fill="blue")
c.pack()
tk_window.mainloop()