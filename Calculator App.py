#Building a Calculator App Using Tkinter
import tkinter as tk 
from tkinter.font import Font

#Window
root = tk.Tk()
root.title("Tkinter Calculator")
root.geometry("300x400")
root.resizable(False, False) #Fixed Window size

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

#Display Area
displayEntry = tk.Entry(
    root,
    font = font2,
    justify = "right"
)
displayEntry.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 20)

#Buttons
buttons = [
    "1", "2", "3", "4", "5",
    "6", "7", "8", "9", "0",
    "+", "-", "*", "/", "=",
    "."
]

row = 1
col = 0

for btn in buttons:
    calcbtns = tk.Button(
        root, 
        text = btn, 
        font = font2, 
        width = 5, 
        height = 2
    )
    calcbtns.grid(row = row, column = col, padx = 8.5, pady = 5)

    #Resetting the number of rows when the column number reaches 4
    col += 1
    if col > 3:
        col = 0 #resets column number after it exceeds 3
        row += 1

root.mainloop()