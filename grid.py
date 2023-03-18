from tkinter import *

root=Tk()
root.title("Grid View")

name=Label(root,text="Name",bg="White",fg="red")

password=Label(root,text="Password",bg="gray",fg="red")
ni=Entry(root)
pi=Entry(root)

name.grid(row=0,sticky=W)#sticky=Sticks to {N=North, E,S,W ....}
password.grid(row=1)
ni.grid(column=1,row=0,sticky=W)
pi.grid(column=1,row=1)
# Insering a Checkbox
chk=Checkbutton(root,text="Keep me Logged in")
chk.grid(row=3,columnspan=2)
btn=Button(root,text="Login",bg="Green")
btn.grid(row=4,column=1)

root.mainloop()