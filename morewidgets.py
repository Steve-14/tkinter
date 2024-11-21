
import tkinter as tk
from tkinter import ttk

#  tk._test() tests import has worked

root = tk.Tk() # sets up the interface
root.title("Widgets App") # creates title for window

def add_to_list(event=None):# a function add text input to list box (event=None) is added to allow function to accept an argument)
    text = entry.get() # gets text from entry box and stores in variable £text£
    if text: # check if text entered prevent empty lines being added
        text_list.insert(tk.END, text) # tk.END adds to end of current list
        entry.delete(0, tk.END) # removes the text entered into the text box from start to end
        
root.columnconfigure(0, weight=1)# makes element  take up all available space when resized
root.columnconfigure(1, weight=1) # same for second column
root.rowconfigure(0, weight=1) 

frame= ttk.Frame(root) # a container in root
frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10) # to allow display, sticky to make frame sticks to window when resized

frame.columnconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)

entry = ttk.Entry(frame) # add to frame that is within root - in that frame is a text input field
entry.grid(row=0, column=0, sticky="ew") # position element so it is displayed

entry.bind("<Return>", add_to_list) # pressing enter button calls function

entry_btn = ttk.Button(frame, text="Add", command=add_to_list) # adds a command to the button to call the add_to_list function
entry_btn.grid(row=0, column=1)

text_list = tk.Listbox(frame) # adds a listbox element to the frame
text_list.grid(row=1, column=0, columnspan=2, sticky="nsew") # to display

# frames allow us to easily replicate groups of elements to quickly build forms using similar layouts

""" frame2= ttk.Frame(root) # a container in root
frame2.grid(row=0, column=2, sticky="nsew", padx=10, pady=10) # to allow display, sticky to make frame sticks to window when resized

frame2.columnconfigure(1, weight=1)
frame2.rowconfigure(1, weight=1)

entry = ttk.Entry(frame2) # add to frame that is within root - in that frame is a text input field
entry.grid(row=0, column=0, sticky="ew") # position element so it is displayed

entry.bind("<Return>", add_to_list)

entry_btn2 = ttk.Button(frame2, text="Addme", command=add_to_list) # adds a command to the button to call the add_to_list function
entry_btn2.grid(row=0, column=1)

text_list2 = tk.Listbox(frame2) # adds a listbox element to the frame
text_list2.grid(row=1, column=0, columnspan=2, sticky="nsew") # to display """

root.mainloop() # to keep on screen