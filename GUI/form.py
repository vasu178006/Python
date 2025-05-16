from tkinter import *

root = Tk()
root.resizable(0, 0)
root.geometry("800x800")

lbl = Label(root, text="click me", font=("Arial", 25), bg="black", fg="white")
lbl.grid(row=0, column=0, pady=25, sticky='w')  

eName = Entry(root, font=("Arial", 20), bg="black", fg="white")
eName.grid(row=0, column=1, pady=25, sticky='ew')  
root.grid_columnconfigure(1, weight=1)
root.mainloop() 
