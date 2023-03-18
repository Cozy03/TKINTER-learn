from tkinter import *
import tkinter.messagebox as mb

root=Tk()
root.title("Message Box")

mb.showinfo("rror","you are Hacked Bro!")

answer=mb.askquestion("QST","Are you Hacked?")

if answer=='yes':
    print("Doomed")
root.mainloop()