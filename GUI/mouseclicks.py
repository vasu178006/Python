from tkinter import *

def m1(event):
    root.config(background="red")
def m2(event):
    btn.config(background="blue")
def m3(event):
    btn.config(background="green")
root = Tk()
root.geometry("1000x1000")
root.resizable(1, 1)
btn = Button(root, text="Click Me", font=("Arial", 15))
btn.bind("<Button-1>", m1) 
btn.bind("<Button-2>", m2)
btn.bind("<Button-3>", m3)
btn.pack()
root.mainloop()
