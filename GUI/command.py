from tkinter import *
root=Tk()
root.geometry("500x500")
root.resizable(1,1)
def myfun():
    print("Vasu")
btn=Button(root,text="click me",font=("Arial",15),command=myfun)
btn.pack()
root.mainloop()
