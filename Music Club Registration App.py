# 🎯 PROJECT GOAL

# Build a Music Club Registration App where a user:

# Enters personal details
# Selects age using Spinbox
# Chooses music mood (RadioButtons)
# Chooses favorite genres (Listbox + Scrollbar)
# Accepts terms (Checkbutton)
# Submits registration
# Sees results in a Text widget
# Can open:
# About window (Toplevel)
# Help/About menu (Menu bar)
# Gets feedback via Messageboxes

import tkinter as tk 
from tkinter.font import Font 

root = tk.Tk()
root.minsize(400, 250)
root.title("Music Club Registration App")

#Fonts
font1 = Font(
    family = "Brushstroke",
    size = 16,
    weight = "bold",
    slant = "roman",
    underline = 0,
    overstrike = 0
)

font2 = Font(
    family = "Segoe UI",
    size = 12,
    weight = "normal",
    slant = "roman",
    underline = 0,
    overstrike = 0
)

#Creating a Top level Application for the 'About' menu button
toplev = None
def about():
    global toplev
    toplev = tk.Toplevel(root)
    toplev.title("About")
    toplev.minsize(300, 150)

    AbtLabel = tk.Label(toplev, text = "Nothing to really see here :)", font = font2)
    AbtLabel.pack()


#Title Label
titleLabel = tk.Label(root, text = "Music Club Registration App", font = font1)
titleLabel.pack()


#Building the menu bar
menubar = tk.Menu(root)
root.config(menu = menubar)

#Creating the File Menu
filemenu = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu = filemenu)

#Creating the content of the file menu
filemenu.add_command(label = "Exit", command = root.quit)

#Creating Help Menu
helpmenu = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Help", menu = helpmenu)

#Creating the content of the Help menu
helpmenu.add_command(label = "About", command = about)


#Creating the contents of the main window
#LabelFrame1 : Personal Info
LabelFrame1 = tk.LabelFrame(root, text = "Personal Info", font = font2)
LabelFrame1.pack(pady = 5)

#Personal Info Labels and Entries
nameLabel = tk.Label(LabelFrame1, text = "Name")
nameEntry = tk.Entry(LabelFrame1)

emailLabel = tk.Label(LabelFrame1, text = "Email")
emailEntry = tk.Entry(LabelFrame1)

ageLabel = tk.Label(LabelFrame1, text = "Age")
ageSpin = tk.Spinbox(LabelFrame1, from_= 14, to = 40)

nameLabel.grid(column = 0, row = 0)
nameEntry.grid(column = 1, row = 0)
emailLabel.grid(column = 0, row = 1)
emailEntry.grid(column = 1, row = 1)
ageLabel.grid(column = 0, row = 2)
ageSpin.grid(column = 1, row = 2)


#LabelFrame2 : Music Preferences
LabelFrame2 = tk.LabelFrame(root, text = "Music Preference", font = font2)
LabelFrame2.pack(pady = 5)

#The Genre
genres = ["Hip-Hop", "Pop", "Rock", "Country", "Afrobeat", "R&B", "Rap", "Hip-Life", "High-Life"]
mood_var = tk.StringVar()

#Music Preferences
moodLabel = tk.Label(LabelFrame2, text = "Mood", font = font2)
moodLabel.pack()

for genre in genres:
    tk.Radiobutton(LabelFrame2, text = genre, variable = mood_var, value = genre).pack()





root.mainloop()