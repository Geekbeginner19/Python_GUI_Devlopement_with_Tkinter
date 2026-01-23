# 🧩 MINI PROJECT: Student Registration Form

# 🎯 Goal
# Build a small GUI app where a user:
# Enters student info inside LabelFrames
# Selects an age using a Spinbox
# Submits the form
# Gets feedback using Messageboxes
# This mirrors how forms work in real software.

import tkinter as tk 
from tkinter import messagebox 

root = tk.Tk()
root.title("Student Registration Form")
root.minsize(450, 200)

#Fonts
font1 = ("verdana", 17, "bold")
font2 = ("calibri", 11)

#Title Label to Show Heading
titleLabel = tk.Label(root, text = "Student Registration Form", font=font1)
titleLabel.pack()

#Creating the label frame
stuLabelFrame = tk.LabelFrame(root, text = "Student info", height = 300, width = 150, font=font2)
stuLabelFrame.pack()
#Putting other labels and entries on the Label Frame Created above
nameLabel = tk.Label(stuLabelFrame, text = "Name: ")
ageLabel = tk.Label(stuLabelFrame, text = "Age: ")
ageSpin = tk.Spinbox(stuLabelFrame, from_=1, to=100)
emailLabel = tk.Label(stuLabelFrame, text = "Email: ")
nameEntry = tk.Entry(stuLabelFrame)
emailEntry = tk.Entry(stuLabelFrame)
#Arranging the Labels and Entries on the Label Frame created
nameLabel.grid(column = 0, row = 0)
nameEntry.grid(column = 1, row = 0)
emailLabel.grid(column = 0, row = 1)
emailEntry.grid(column = 1, row = 1)
ageLabel.grid(column = 0, row = 2)
ageSpin.grid(column = 1, row = 2)

#Creating a Function to display a message using tkinter messagebox
def info():
    messagebox.showinfo("Success", "Your Information has been collected successfully!")
    messagebox.showinfo("Info", emailEntry.get())#to call and display the information entered in the entry widget

#Creating the Submit Button
submitBtn = tk.Button(root, text = "Submit", font=font2, command = info)
submitBtn.pack(pady = 15)

root.mainloop()