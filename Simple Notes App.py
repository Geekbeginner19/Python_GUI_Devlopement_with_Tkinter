# 🧩 MINI PROJECT: Simple Notes App

# 🎯 Project Goal
# Create a small app where a user can:
# Type multiple lines of text
# Scroll through the text using a vertical scrollbar
# Click a button to display or save the written notes (for now, just display them)
# This is the foundation of apps like Notepad.

import tkinter as tk 

root = tk.Tk()
root.minsize(300, 100)
root.title("Simple Notes App")

#Create Scrollbar
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side = "right", fill = "y")

#Connect the scrollbar to the text (when creating the text)
text = tk.Text(root, yscrollcommand = scrollbar.set)
text.insert("insert", "Here I am, send me, send me\nArduino pins are connection points that let the Arduino control and receive signals from electronic components. \nArduino pins are the small metal connection points on the Arduino board that allow it to communicate with other electronic components.")
text.insert("end", "\nOkayy :)")
text.pack(side = "left", fill = "both", expand = True) #Packing the text onto the window

#Telling the scrollbar to control the text (Should come after the text is created)
scrollbar.config(command = text.yview)

root.mainloop()