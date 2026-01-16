import tkinter as tk
#Creating the main tkinter window
root = tk.Tk()
root.minsize(650, 400)

#Step 1: Create the main menu Bar
menu_bar = tk.Menu(root)
root.config(menu = menu_bar) #This displays the menu to the main tkinter window

#Step 2: Create 'File' Menu
file_menu = tk.Menu(menu_bar, tearoff = 0)#Setting tearoff to 0 removes that ugly dashed lines
menu_bar.add_cascade(label = "File", menu = file_menu)#Add the names of the menus to the menu bar

#Adding the menu items to the file menu
def new_file():
    print("New File Clicked!")

def exit_app():
    root.quit()#Exits a tkinter window

file_menu.add_command(label = "View", command = new_file)
file_menu.add_separator()
file_menu.add_command(label = "Exit", command = exit_app)

root.mainloop()