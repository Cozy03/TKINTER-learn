#Adding Frames and Widgets inside it........

from tkinter import *
root=Tk()
root.title("Adding Frames and Widgets")

#Building a Frame
frameTop=Frame(root)
frameTop.pack()

# Adding a bottom frame in ____ well Buttom!(side=BOTTOM)
frameButt=Frame(root)
frameButt.pack(side=BOTTOM)

# Adding a Button to top frame

button1=Button(frameTop,text="Button 1", fg="green")#inputs(Frame,Name(text=" "),Color of Text(fg=""))
button1.pack(side=LEFT)

button1=Button(frameTop,text="Button 3", fg="purple")#inputs(Frame,Name(text=" "),Color of Text(fg=""))
button1.pack(side=LEFT)


# Adding a Button to down frame

button2=Button(frameButt,text="Button 2", fg="red")#inputs(Frame,Name(text=" "),Color of Text(fg=""))
button2.pack(side=RIGHT)




root.mainloop()