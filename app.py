import numpy as np
import scipy
import scipy.linalg as la
from tkinter import *
 
# create root window
root = Tk()
 
# root window title and dimension
root.title("ANF")
# Set geometry (widthxheight)
root.geometry('3500x2000')
 
lbl = Label(root)
lbl.grid()

# button is clicked
# adding Entry Field
txt = Entry(root, width=10)
txt.grid(column =1, row =1)
 
 
# function to display user text when
# button is clicked
def clicked():
 
    res = "You wrote" + txt.get()
    lbl.configure(text = res)
 
# button widget with red color text inside
btn = Button(root, text = "Click me" ,
             fg = "red", command=clicked)
# all widgets will be here
# Execute Tkinter

root.mainloop()