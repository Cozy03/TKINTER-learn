from tkinter import *

root=Tk()
root.title("Function Binding")

# ----Meathod 1----

# Function 1
def print_name1():
    print("Debrup")

#Button using
btn1=Button(root,text="Button 1",command=print_name1)
btn1.pack()

# ----Meathod 2----

# Function 2
def print_name2(event):
    print("Debrup")

def print_name3(event):
    print("Hu Hu Hu!!!")
# Button uusing
btn2=Button(root,text="Button2")
btn2.bind("<Button-2>",print_name2)#<Button-2> => Right Click
btn2.bind("<Button-1>",print_name3)#<Button-1> => Left Click
btn2.pack()


root.mainloop()