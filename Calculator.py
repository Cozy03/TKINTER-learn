from tkinter import *
def click(event):
    global scrval
    clicked=event.widget.cget("text")
    # print(clicked)
    if clicked=="=":
        if scrval.get().isdigit():
            clicked=int(scrval.get())
        else:
            clicked=eval(scrval.get())
        scrval.set(clicked)
        scr.update()
    elif clicked=="C":
        scrval.set("")
        scr.update()
    else:
        scrval.set(scrval.get()+clicked)
        scr.update()

    
root=Tk()
root.geometry("650x900")
root.title("Calculator")
root.wm_iconbitmap('Calculator_icon.svg.png')
root.configure(background="white")

scrval=StringVar()
scrval.set("")

scr=Entry(root,textvar=scrval,font="arial 40 bold",background="grey")
scr.pack(fill=X,ipadx=8,padx=10,pady=10)




# Row 1
f=Frame(root, bg="white")
b=Button(f,text="9",font="lucida 35 bold",padx=28,pady=22)
b.pack(side=LEFT,padx=12,pady=18)
b.bind("<Button-1>",click)
b=Button(f,text="8",font="lucida 35 bold",padx=28,pady=22)
b.pack(side=LEFT,padx=12,pady=18)
b.bind("<Button-1>",click)
b=Button(f,text="7",font="lucida 35 bold",padx=28,pady=22)
b.pack(side=LEFT,padx=12,pady=18)
b.bind("<Button-1>",click)
f.pack()

# Row 2
f=Frame(root, bg="white")
b=Button(f,text="6",font="lucida 35 bold",padx=28,pady=22)
b.pack(side=LEFT,padx=12,pady=18)
b.bind("<Button-1>",click)
b=Button(f,text="5",font="lucida 35 bold",padx=28,pady=22)
b.pack(side=LEFT,padx=12,pady=18)
b.bind("<Button-1>",click)
b=Button(f,text="4",font="lucida 35 bold",padx=28,pady=22)
b.pack(side=LEFT,padx=12,pady=18)
b.bind("<Button-1>",click)
f.pack()

# Row 3
f=Frame(root, bg="white")
b=Button(f,text="3",font="lucida 35 bold",padx=28,pady=22)
b.pack(side=LEFT,padx=12,pady=18)
b.bind("<Button-1>",click)
b=Button(f,text="2",font="lucida 35 bold",padx=28,pady=22)
b.pack(side=LEFT,padx=12,pady=18)
b.bind("<Button-1>",click)
b=Button(f,text="1",font="lucida 35 bold",padx=28,pady=22)
b.pack(side=LEFT,padx=12,pady=18)
b.bind("<Button-1>",click)
f.pack()

# Row 4
f=Frame(root, bg="white")
b=Button(f,text="+",font="lucida 35 bold",padx=28,pady=22)
b.pack(side=LEFT,padx=12,pady=18)
b.bind("<Button-1>",click)
b=Button(f,text="0",font="lucida 35 bold",padx=28,pady=22)
b.pack(side=LEFT,padx=12,pady=18)
b.bind("<Button-1>",click)
b=Button(f,text="-",font="lucida 35 bold",padx=28,pady=22)
b.pack(side=LEFT,padx=12,pady=18)
b.bind("<Button-1>",click)
f.pack()

# Row 5
f=Frame(root, bg="white")
b=Button(f,text="*",font="lucida 35 bold",padx=28,pady=22)
b.pack(side=LEFT,padx=12,pady=18)
b.bind("<Button-1>",click)
b=Button(f,text="/",font="lucida 35 bold",padx=28,pady=22)
b.pack(side=LEFT,padx=12,pady=18)
b.bind("<Button-1>",click)
b=Button(f,text="C",font="lucida 35 bold",padx=28,pady=22)
b.pack(side=LEFT,padx=12,pady=18)
b.bind("<Button-1>",click)
f.pack()

# Row 6
f=Frame(root, bg="white")
b=Button(f,text="(",font="lucida 35 bold",padx=28,pady=22)
b.pack(side=LEFT,padx=12,pady=18)
b.bind("<Button-1>",click)
b=Button(f,text=")",font="lucida 35 bold",padx=28,pady=22)
b.pack(side=LEFT,padx=12,pady=18)
b.bind("<Button-1>",click)
b=Button(f,text="=",font="lucida 35 bold",padx=28,pady=22)
b.pack(side=LEFT,padx=12,pady=18)
b.bind("<Button-1>",click)
f.pack()


root.mainloop()