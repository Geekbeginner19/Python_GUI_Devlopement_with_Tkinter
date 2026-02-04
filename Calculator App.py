#Building a Calculator App Using Tkinter
import tkinter as tk 
from tkinter.font import Font
from tkinter import messagebox

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
    ".", "C", "←"
]
#Function for the clear button
def clear_display():
    displayEntry.delete(0, tk.END)

#Function for the delete button
def delete_last():
    current = displayEntry.get()
    if current: #Checks to see if there are any characters on screen
        displayEntry.delete(len(current) - 1, tk.END) 

#Button Modifications
def on_button_click(value):
    if value == "=":
        try:
            expression = displayEntry.get()
            result = eval(expression)
            displayEntry.delete(0, tk.END)
            displayEntry.insert(0, str(result))
        except:
            messagebox.showerror("Error", "Invalid Expression")
            displayEntry.delete(0, tk.END)
        return
    current = displayEntry.get() #Gets the values of whatever entered
    # If value is an operator
    if value in "+-*/":
        if current == "":
            return  # Rule 1: no operator at start
        if current[-1] in "+-*/":
            return  # Rule 2: no double operators

    # If value is a decimal point
    if value == ".":
        last_number = ""
        for char in reversed(current):
            if char in "+-*/":
                break
            last_number = char + last_number
        if "." in last_number:
            return  # Rule 3: one decimal per number
    displayEntry.delete(0, tk.END)
    displayEntry.insert(0, current + value)

row = 1
col = 0

for btn in buttons:
    if btn == "C": #Handling the clear button differently
        calcbtns = tk.Button(
            root,
            text=btn,
            font=font2,
            width=5,
            height=2,
            command=clear_display
        )
    elif (btn == "←"):
        calcbtns = tk.Button(
            root,
            text=btn,
            font=font2,
            width=5,
            height=2,
            command=delete_last
        )
    else:
        calcbtns = tk.Button(
            root,
            text=btn,
            font=font2,
            width=5,
            height=2,
            command=lambda value=btn: on_button_click(value)
        )
    calcbtns.grid(row = row, column = col, padx = 8.5, pady = 5)

    #Resetting the number of rows when the column number reaches 4
    col += 1
    if col > 3:
        col = 0 #resets column number after it exceeds 3
        row += 1

root.mainloop()