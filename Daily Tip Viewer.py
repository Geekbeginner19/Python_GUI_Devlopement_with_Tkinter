# 📌 Topic: Showing Multiple Lines of Text (tk.Message)
# 📝 Project Name
# Daily Tip Viewer

# 🎯 Goal
# Display a multi-line motivational or study tip inside a window using the Message widget.

# 🖥️ App Description
# A title label at the top
# A Message widget showing 3–5 lines of text
# The text should automatically wrap inside the window

import tkinter as tk 

root = tk.Tk()
root.minsize(400, 200)

#Building a Message (Unless the text function, message displays multiple lines of text in a window)
msg = tk.Message(root, text = "Tip of the Day: \nSometimes I'm really Sad. \nSometimes I'm really Happy. \nSometimes I just Exist.", width = 150)
msg.pack()

root.mainloop()