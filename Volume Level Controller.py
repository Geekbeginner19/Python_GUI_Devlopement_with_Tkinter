# 📌 Topic: tk.Scale

# 📝 Project Name
# Volume Level Controller

# 🎯 Goal
# Use a Scale widget to select a numeric value and display it.

# 🖥️ App Description
# A label: “Select volume”
# A horizontal scale from 0 to 100
# A label that updates to show the current value

import tkinter as tk 

root = tk.Tk()
root.minsize(400, 200)

#Building a Label
ScaleLab = tk.Label(root, text = "Select Volume")
ScaleLab.pack()

#Building a Scale
volscale = tk.Scale(root, length = 300, from_= 0, to = 150, tickinterval = 15, orient = "horizontal")
volscale.pack()

root.mainloop()