import io_data_module as io
from tkinter import *

dataSet = io.read_multi_dim_data("iris.data")

tk_window = Tk()

c = Canvas(tk_window, bg="white", height=500, width=500)
radius = 1.5
spread = 50

for item in dataSet:
    c.create_oval(float(item[0]) * spread - radius,
                  float(item[1]) * spread - radius,
                  float(item[0]) * spread + radius,
                  float(item[1]) * spread + radius,
                  outline="red", fill="red")

c.pack()
tk_window.mainloop()