import tkinter as tk

#  tk._test() tests import has worked

root = tk.Tk() # sets up the interface
root.title("Simple App") # creates title for window

def on_click():
    lbl.config(text="Button Clicked!!") # when called the function changes the text on the label to "Button Clicked"


lbl = tk.Label(root, text="Label 1") # ads a label for button 1
lbl.grid(row=0, column=0) # again must use this line for button to be displayed

print(lbl.config().keys()) # prints a list of the keys usable for label config in the terminal

btn = tk.Button(root, text="Button 1", command=on_click) # create a button. Passing in root as this will be the parent window where the button is to placed. calls function on_click()
btn.grid(row=0, column=1) # MUST specify grid layout for button to show






root.mainloop() # allows window to remain on screen


