from tkinter import *
# import random module , use it to randomly select an image from list
import tkinter as tk



class Application(Frame):

    def __init__(self, users_anime,master=None):  # add  a list as parameter to store your anime
        frame = Frame.__init__(self, master,bg="gray")


        self.user_anime = users_anime
        putback = {}  # stores location of selected item in listbox_all_anime
        self.putback = putback
        self.pack()

        #self.painel = tk.Canvas(frame, width=w, height=h)
        ##self.painel.pack(side='top', fill='both', expand='yes')

        #self.painel.grid(row=0, column=0)


        #self.painel.create_image(0, 0, image=bg_images, anchor='nw')




        # ----Call all widgets----
        self.search_var = StringVar()
        self.search_var.trace("w", self.update_list)
        self.entry = Entry(self, textvariable=self.search_var, width=60)
        self.label = Label(self, text="All Anime ", )
        self.btn_remove = Button(self, text="Remove <---", command=self.Remove, padx=2, pady=2)
        self.btn_select = Button(self, text="Select --->", command=self.Select, padx=2, pady=2)
        self.btn_done = Button(self, text="Done", padx=1, command=self.quit)  # make the font larger
        self.listbox_all_anime = Listbox(self, selectmode=SINGLE, width=90, height=15)
        self.listbox_choices = Listbox(self, selectmode=SINGLE, width=59, height=15)

        # ----Position all widgets----
        self.entry.grid(row=0, column=1, padx=10, pady=3)
        self.listbox_all_anime.grid(row=1, column=0, padx=10, pady=3, columnspan=2)
        self.listbox_choices.grid(row=1, column=3, padx=10, pady=3, columnspan=2)
        self.btn_select.grid(column=2, row=1)
        self.btn_remove.grid(column=3, row=2, sticky=E)
        self.btn_done.grid(column=1, row=2)

        # Function for updating the list/doing the search.
        # It needs to be called here to populate the listbox.
        self.update_list()

    def show_anime(self):
        return self.user_anime

    def show_putback(self):
        return self.putback

    def update_list(self, *args):
        search_term = self.search_var.get()

        # Just a generic list to populate the listbox
        from pickle import load
        all_anime = load(open("anime_save_.p", "rb"))

        all_anime_list = []
        for key, value in all_anime.items():
            all_anime_list.append(key)

        self.listbox_all_anime.delete(0, END)

        for item in all_anime_list:
            if search_term.lower() in item.lower():
                self.listbox_all_anime.insert(END, item)

    def Select(self):
        selection = self.listbox_all_anime.curselection()
        for i in selection:
            entered = self.listbox_all_anime.get(i)
            self.listbox_choices.insert(END, entered + '\n')
            # self.user_anime.append(entered)
            self.listbox_all_anime.delete(selection)
            self.putback[entered] = selection

    def Remove(self):
        selection = self.listbox_choices.curselection()
        for i in selection:
            clicked = self.listbox_choices.get(i)  # the name of the clicked anime
            location = self.putback[clicked[:-1]]
            self.listbox_all_anime.insert(location, clicked)
            self.listbox_choices.delete(selection)

    def final(self):
        for i in self.listbox_choices.get(0, END):
            self.user_anime.append(i[:-1])

    def quit(self):
        self.final()
        """Quit the Tcl interpreter. All widgets will be destroyed."""
        self.tk.quit()


root = Tk()
root.title('Filter Listbox Test')
#root.geometry("1000x307")

bg_images = PhotoImage(file="C:\\Users\\Gerard\\PycharmProjects\\Web Scraping\\\images\\sao.png")
your_anime = []

w = bg_images.width()
h = bg_images.height()

#painel = tk.Canvas(root, width=w, height=h)
#painel.pack(side='top', fill='both', expand='yes')
#painel.create_image(0, 0, image=bg_images, anchor='nw')
#
app = Application(your_anime, master=root)
print('Starting mainloop()')

root.mainloop()
