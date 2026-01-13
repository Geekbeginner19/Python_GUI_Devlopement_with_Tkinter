# 🧩 Mini Project: Simple Profile Card App
# 🎯 Project Goal
# Create a small window that displays static information about a person using only Label widgets.
# Think of it like a digital ID card.

import tkinter as tk

root = tk.Tk()
root.title("My Profile Card App") #Title of window
root.geometry("500x350")#Window size

#Creating labels
label = tk.Label(root, text = "PROFILE CARD APP", font = ("verdana", 25, "bold"), padx = 20, pady = 20, bg = "lightblue")
label2 = tk.Label(root, text = "Name : Kelvin Ofori Amoafo", font = "calibri", padx = 20, pady = 20, fg = "blue")
label3 = tk.Label(root, text = "Role: Data Analyst", font = "calibri", padx = 20, pady = 20, fg = "green")
label4 = tk.Label(root, text = "Learning Tkinter", font = "calibri", padx = 20, pady = 20, fg = "brown")
label5 = tk.Label(root, text = "Built with Tkinter", font = "calibri", padx = 20, pady = 20, fg = "red")

#Displaying the labels 
label.pack()
label2.pack()
label3.pack()
label4.pack()
label5.pack()

root.mainloop()