# 🧩 Mini Project: Simple Registration Form App

# This is a real-world beginner GUI project that uses ALL of the following:
# ✅ Label
# ✅ Entry
# ✅ Button
# ✅ Checkbutton

# 🎯 Project Goal
# Create a small GUI app where a user can:
# Enter their Name
# Enter their Email
# Choose whether they agree to terms
# Click a button to submit
# See the submitted info displayed in the app 

import tkinter as tk 

root = tk.Tk()
root.title("Simple Registration Form App")
root.minsize(600, 450) #setting default window size for this program

#fonts
font1 = ("verdana", 16, "bold")
font2 = ("serif", 11)

#Registration Label, Name and Entry for name
regLab = tk.Label(root, text = "REGISTRATION FORM", font = font1)
nameLab = tk.Label(root, text = "Name:", font=font2)
nameEntry = tk.Entry(root)
regLab.pack()
nameLab.pack()
nameEntry.pack()


#Email label and it entry
emailLab = tk.Label(root, text = "Email:", font=font2)
emailEntry = tk.Entry(root)
emailLab.pack()
emailEntry.pack()

#Checkbutton label and it entry
chkbtnLab = tk.Label(root, text = "I agree to the terms", font=font2)
chkbtn = tk.Checkbutton(root)
chkbtnLab.pack()
chkbtn.pack()

#Submit button
submitbtn = tk.Button(root, text = "SUBMIT", font=font2)
submitbtn.pack()

root.mainloop()
