import tkinter as tk
#Creating the main tkinter window
root = tk.Tk()
root.minsize(650, 400)

#Step 1: Create the main menu Bar
menu_bar = tk.Menu(root)
root.config(menu = menu_bar) #This displays the menu to the main tkinter window

#Step 2: Create 'File' Menu
file_menu = tk.Menu(menu_bar, tearoff = 0)#Setting tearoff to 0 removes that ugly dashed lines
menu_bar.add_cascade(label = "File", menu = file_menu)#Displays the names of the menus to the menu bar

#Adding the menu items to the file menu
def new_file():
    print("New File Clicked!")

def exit_app():
    root.quit()#Exits a tkinter window

#Creating a Dropdown inside the main menu
openrecent = tk.Menu(menu_bar, tearoff = 0)
fileNames = ["File 1", "File 2", "File 3", "File 4"]
for label in fileNames:
    openrecent.add_command(label = label) #Adding the menu items on the open recent option
file_menu.add_cascade(label = "Open Recent", menu = openrecent)#Adding the open recent to the file menu
openrecent.add_separator()
openrecent.add_command(label = "Exit", command = exit_app)#Adding a command to the openrecent menu

#Adding Commands to the file menu
file_menu.add_command(label = "New", command = new_file)
file_menu.add_separator()
file_menu.add_command(label = "Exit", command = exit_app)


#Making Menu Buttons
#Step 1: Create a menu button
menu_btn = tk.Menubutton(root, text = "Options", relief = "raised")
menu_btn.pack(pady = 20)

#Step 2: Create a Menu for the button
btnForMenu = tk.Menu(menu_btn, tearoff = 0)
menu_btn.config(menu = btnForMenu)

#Step 3: Add items to the menu
def option1():
    print("Option 1 selected")

def option2():
    print("Option 2 selected")

btnForMenu.add_command(label="Option 1", command=option1)
btnForMenu.add_command(label="Option 2", command=option2)

root.mainloop()