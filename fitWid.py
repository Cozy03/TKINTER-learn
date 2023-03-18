from tkinter import *
root=Tk()
root.title("Fit Widgets")

# Making a label in root PARAMETERS=> (Where to place,Text to display, foreground(Text) color,Background color)
one=Label(root,text="One",fg="green",bg="white")
one.pack()

two=Label(root,text="Two", fg="yellow",bg="purple")
two.pack(fill=X) #fill=___=> Fills it up if we streach the window Values= x or y

three=Label(root,text="Three", fg="yellow",bg="black")
three.pack(side=LEFT,fill=Y)

root.mainloop()