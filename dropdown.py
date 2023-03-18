from tkinter import *

def doNothing():
    print("Nothing is Happing!")


root=Tk()
root.title("Dropdown Menus")

# ----Dropdown Menu----
menu=Menu(root)
root.config(menu=menu)

subMenu=Menu(menu)
menu.add_cascade(label="View",menu=subMenu)
subMenu.add_command(label="Print",command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit",command=root.quit)

cpMenu=Menu(menu)
menu.add_cascade(label="Edit",menu=cpMenu)
cpMenu.add_command(label="Copy",activebackground="Blue",command=doNothing)

# ----Toolbar----
toolbar=Frame(root,bg="pink")
insertButt=Button(toolbar,text="ClickMe",command=doNothing)
insertButt.pack(side=LEFT,padx=2,pady=2)
insButt=Button(toolbar,text="Exit",command=root.quit)
insButt.pack(side=LEFT,padx=2,pady=2)

toolbar.pack(side=TOP,fill=X)

#----Status Bar----
status=Label(root,text='Status Bar',bd=1,relief=SUNKEN,anchor=W )
status.pack(side=BOTTOM,fill=X,)

root.mainloop()