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
root.minsize(400, 150)
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
ageSpin.delete(0, tk.END)#Not recommended but works

nameLabel.grid(column = 0, row = 0)
nameEntry.grid(column = 1, row = 0)
emailLabel.grid(column = 0, row = 1)
emailEntry.grid(column = 1, row = 1)
ageLabel.grid(column = 0, row = 2)
ageSpin.grid(column = 1, row = 2)


#LabelFrame2 : Music Preferences
LabelFrame2 = tk.LabelFrame(root, text = "Music Preference", font = font2)
LabelFrame2.pack(pady = 5)

#The Mood
mood = ["Happy", "Chill", "Energetic"]
mood_var = tk.StringVar()#Variable for the radiobuttons
#Mood Label
moodLabel = tk.Label(LabelFrame2, text = "Select Mood", font = font2, fg = "blue")
moodLabel.pack(pady = 5)

#Creating the radio buttons
for moodinstance in mood:
    moodRadioBtn = tk.Radiobutton(LabelFrame2, text = moodinstance, value = moodinstance, variable = mood_var).pack(anchor = "nw")

#The Genre
genres = ["Hip-Hop", "Pop", "Rock", "Country", "Afrobeat", "R&B", "Rap", "Hip-Life", "High-Life"]

#Genre Label
moodLabel = tk.Label(LabelFrame2, text = "Select Genre", font = font2, fg = "blue")
moodLabel.pack(pady = 10)

#Creating a scrollbar to handle the listbox
lstboxscrollbar = tk.Scrollbar(LabelFrame2)
lstboxscrollbar.pack(side = "right", fill = "y")

#Listboxes for the genre whiles connectting the scrollbar to the listbox (when creating the listbox)
genreLstBox = tk.Listbox(LabelFrame2, width = 10, height = 7,selectmode = tk.MULTIPLE, yscrollcommand = lstboxscrollbar.set)

#Adding the items in the ListBox
for genre in genres:
    genreLstBox.insert("end", genre)
genreLstBox.pack(anchor = "nw", padx = 3)

#Telling the scrollbar to control the listbox (Should come after the listbox is created)
lstboxscrollbar.config(command = genreLstBox.yview)


#LabelFrame3: Terms
LabelFrame3 = tk.LabelFrame(root, text = "Terms & Conditions", font = font2)
LabelFrame3.pack(pady = 5)

#Checkbuttons for the terms and conditions
termsVar = tk.BooleanVar()#Assigning the value of the terms and conditions to termsVar
termsCheckButton = tk.Checkbutton(LabelFrame3, text = "I Agree to the Club Rules", font = font2, variable = termsVar)
termsCheckButton.pack()

def submit():
    #Text Widget
    spinVal = ageSpin.get()
    nameVal = nameEntry.get().strip()
    emailVal = emailEntry.get().strip()
    if nameVal and emailVal and termsVar.get() and spinVal:
        output = tk.Text(root, width = 90)
        output.insert("insert", f"Name: {nameVal}")
        output.insert("insert", f"\nEmail: {emailVal}")
        output.insert("insert", f"\nAge: {spinVal}")
        output.pack(pady = 5)
    else:
        print("Enter all info & Check the terms and conditions")

#Submit Button
submitBtn = tk.Button(root, text = "Submit", font = font2, command = submit)
submitBtn.pack(pady = 5)

root.mainloop()