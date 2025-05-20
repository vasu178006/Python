from tkinter import *
root=Tk()
root.geometry("500x500")
root.resizable(1,1)
def myfun():
    print("Vasu")
btn=Button(root,text="click me",font=("Arial",15))
btn.bind("<Button-1>",myfun)
btn.bind("<Button-1>",lambda e:root.configure(background="red"))
root.mainloop()
