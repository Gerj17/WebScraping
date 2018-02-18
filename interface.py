from tkinter import *
from tkinter import ttk

root = Tk()

root.title("Name of application")

frame = Frame(root)

Label(frame, text="Your anime").grid(row=0, sticky=W, padx=4)
Entry(frame,width=50).grid(row=0, column=1,pady=4)

Button(frame, text="Submit").grid(row=0, column=8)









frame.grid()

root.mainloop()