from tkinter import *


class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master, bg="red")

        self.pack()
        self.create_widgets()

    # Create main GUI window
    def create_widgets(self):

        self.search_var = StringVar()
        self.search_var.trace("w", self.update_list)
        self.entry = Entry(self, textvariable=self.search_var, width=60)
        self.lable = Label(self, text="All Anime ", )
        self.btn_select = Button(self, text="Select", command=self.Select, padx=2, pady=2)
        self.btn_done = Button(self, text="Done", padx=1, )  # make the font larger
        self.libox_all_anime = Listbox(self, selectmode=SINGLE, width=90, height=15)
        self.textbox_choices = Text(self, width=59, height=15)

        self.entry.grid(row=0, column=1, padx=10, pady=3)
        self.lable.grid(row=0, column=0, padx=10, pady=3, )
        self.libox_all_anime.grid(row=1, column=0, padx=10, pady=3, columnspan=2)
        self.textbox_choices.grid(row=1, column=3, padx=10, pady=3, columnspan=2)
        self.btn_done.grid(column=1, row=2)
        self.btn_select.grid(column=2, row=1)

        # Function for updating the list/doing the search.
        # It needs to be called here to populate the listbox.
        self.update_list()

    def update_list(self, *args):
        search_term = self.search_var.get()

        # Just a generic list to populate the listbox
        from pickle import load
        all_anime = load(open("anime_save_.p", "rb"))

        all_anime_list = []
        for key, value in all_anime.items():
            all_anime_list.append(key)

        self.libox_all_anime.delete(0, END)

        for item in all_anime_list:
            if search_term.lower() in item.lower():
                self.libox_all_anime.insert(END, item)

    def Select(self):

        reslist = []
        selecion = self.libox_all_anime.curselection()

        for i in selecion:
            entered = self.libox_all_anime.get(i)
            self.textbox_choices.insert(END, entered + '\n')

        print(reslist)
        # print(entered)


root = Tk()
root.title('Filter Listbox Test')
# root.geometry("560x450")
app = Application(master=root)
print('Starting mainloop()')
app.mainloop()
