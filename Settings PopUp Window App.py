# 🧩 MINI PROJECT: Settings Pop-Up Window App
# (This is how real apps use Toplevel)

# 🎯 Project Goal
# Practice creating and controlling a secondary window using tk.Toplevel.
# You will build:
# A main window
# A settings pop-up that opens in a new window
# The pop-up should not close the main app

import tkinter as tk

root = tk.Tk()
root.minsize(400, 200)
root.title("Settings Pop-Up Window App")

#Fonts
font1 = ("fine hand", 18, "bold")
font2 = ("consolas", 12)

#Creating a none-type variable for the Top Level Application
toplev = None
#Function for settings
def settings():
    global toplev
    toplev = tk.Toplevel(root)
    toplev.title("Settings")
    toplev.minsize(400, 200)

    #Label for displaying 'Settings'
    setLabel = tk.Label(toplev, text = "Settings", font = font1)
    setLabel.pack()

    #Label to display 'Choose Preference'
    toplevLabel = tk.Label(toplev, text = "Choose Preferences", font = font2)
    toplevLabel.pack(pady=5)

    #Radio Button to enable features
    radBtn = tk.Radiobutton(toplev, text = "Enable Features", value = 1, command = enableFeat)
    radBtn.pack(pady = 5)

    #Close Top Level Window Button
    closetoplevBtn = tk.Button(toplev, text = "Close Settings", font = font2, command = toplev.destroy)
    closetoplevBtn.pack(pady = 5)


#Function for When Enable Feature Button is clicked
def enableFeat():
    #Output for when Enable Features Button is clicked
    displayFeatLab = tk.Label(toplev, text = "Features Enabled!", font = font2)
    displayFeatLab.pack(pady=10)


#Main Window Info
mainLab = tk.Label(root, text = "Main Application", font = font1)
mainLab.pack()

#Settings Button for main window
openSettingsBtn = tk.Button(root, command = settings, text = "Settings", font = font2)
openSettingsBtn.pack(pady=10)

#Button to quit the main window
quitmain = tk.Button(root, text = "Quit", font = font2, command = root.quit)
quitmain.pack()

root.mainloop()