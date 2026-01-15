# 🧩 Mini Project: Music Preference Selector App
# (Perfectly fits what you’ve been learning 😉)

# 🎯 Project Goal
# Build a small GUI app where a user:
# Selects one music mood using Radiobuttons
# Selects multiple music genres using a Listbox
# Clicks a button to submit
# Sees their choices displayed in the app 

import tkinter as tk 

root = tk.Tk()
root.title("Music Preference Selector App")
root.minsize(500, 350)

#Fonts
font1 = ("verdana", 13, "bold")
font2 = ("calibri", 11)

#title Label
titleLab = tk.Label(root, text = "Music Preference App", font = font1, background = "lightblue")
titleLab.pack(pady=10)

#Radio Buttons Label
moodSelectLab = tk.Label(root, text = "Select your mood", font = font2)
moodSelectLab.pack(pady=10)

mood_var = tk.StringVar() #All radiobuttons that share this variable become LINKED
#Radio Buttons
for text in ["Happy", "Chill", "Energetic"]:
    tk.Radiobutton(root, text = text, value = text, variable = mood_var).pack()

#ListBox Label
lstboxLab = tk.Label(root, text = "Select your favourite genres", font = font2)
lstboxLab.pack(pady=10)

#ListBox
lstbox = tk.Listbox(root, selectmode = "multiple", height = 6)
items = ["Hip-Hop", "Afrobeats", "Pop", "R&B", "Rock"] #Items for the listbox
for item in items:
    lstbox.insert("end", item)
lstbox.pack(pady=10)

#Submit Button
SubmitBtn = tk.Button(root, text = "Submit", font = font1)
SubmitBtn.pack(pady=15)

root.mainloop()