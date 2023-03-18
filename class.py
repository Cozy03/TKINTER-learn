from tkinter import *

class ButtonGrp:
    def __init__(self,main):
        frame=Frame(main)
        frame.pack()

        self.printButton=Button(frame,text="Print Message",command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton=Button(frame,text="Quit",command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("Whatever")

root=Tk()
root.title("Class")
x=ButtonGrp(root)


root.mainloop()