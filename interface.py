from tkinter import *

root = Tk()
root.title("Name of application")
root.geometry("360x300")

frame1 = Frame(root)
frame1.pack()
frame2 = Frame(root)
frame2.pack()


label = Label(frame1, text="Name of Anime ", )
enter_names = Entry(frame1)
submit_button = Button(frame1, text="Submit")
done_button = Button(frame2, text="Done")


label.pack()
enter_names.pack(side=LEFT)
submit_button.pack(side=RIGHT)
done_button.pack()

root.mainloop()
