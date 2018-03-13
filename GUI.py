from tkinter import *


class AddAnime(Frame):

    def __init__(self, list_user_anime, master=None):  # add  a list as parameter to store your anime
        Frame.__init__(self, master, bg="gray")
        self.user_anime = list_user_anime  # all of the anime the user likes
        putback = {}             # location of chose anime in libox_anime_pics  used in select method
        self.putback = putback   # location of chose anime in libox_anime_pics  used in select method




        self.pack()

        self.search_var = StringVar()
        self.search_var.trace("w", self.update_list)
        self.entry = Entry(self, textvariable=self.search_var, width=60)
        self.label = Label(self, text="All Anime ", )
        self.btn_remove = Button(self, text="Remove <---", command=self.Remove, padx=2, pady=2)
        self.btn_select = Button(self, text="Select --->", command=self.Select, padx=2, pady=2)
        self.btn_done = Button(self, text="Done", padx=1, command=self.quit)  # make the font larger
        self.libox_all_anime = Listbox(self, selectmode=SINGLE, width=90, height=15)
        self.libox_anime_picks = Listbox(self, selectmode=SINGLE, width=59, height=15)

        self.entry.grid(row=0, column=1, padx=10, pady=3)
        self.libox_all_anime.grid(row=1, column=0, padx=10, pady=3, columnspan=2)
        self.libox_anime_picks.grid(row=1, column=3, padx=10, pady=3, columnspan=2)
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

        self.libox_all_anime.delete(0, END)

        for item in all_anime_list:
            if search_term.lower() in item.lower():
                self.libox_all_anime.insert(END, item)

    def Select(self):
        selection = self.libox_all_anime.curselection()
        for i in selection:
            entered = self.libox_all_anime.get(i)
            self.libox_anime_picks.insert(END, entered + '\n')
            self.user_anime.append(entered)  ######
            self.libox_all_anime.delete(selection)
            self.putback[entered] = selection
            #print(self.show_putback())

    def Remove(self):
        selection = self.libox_anime_picks.curselection()
        for i in selection:
            clicked = self.libox_anime_picks.get(i)  # the name of the clicked anime
            location = self.putback[clicked[:-1]]
            self.libox_all_anime.insert(location, clicked)
            self.libox_anime_picks.delete(selection)
            del self.user_anime[i]





    #def final(self):


    def close(self):
        #self.final()
        """Quit the Tcl interpreter. All widgets will be destroyed."""
        self.tk.quit()


class Youanime(Frame):
    def __init__(self, list_user_anime, master=None):  # add  a list as parameter to store your anime
        Frame.__init__(self, master, bg="green")
        self.pack()
        self.user_anime_YU = list_user_anime  # all of the anime the user likes

        self.lbl_title = Label(self, text="Your Anime !!", padx=10,)
        self.btn_remove_YU = Button(self, text="Remove", padx=2, relief=RAISED, command= self.delete)
        self.libox_ur_anime = Listbox(self, selectmode=SINGLE, width=90, height=15, bg="grey")
        self.btn_done = Button(self, text="Done", padx=7, command=self.quit)  # make the font larger ####

        self.create_ur_anime()


    def create_ur_anime(self):
        self.lbl_title.grid(row=0, column=2,sticky=W)
        self.libox_ur_anime.grid(row=1, column=0, columnspan=4)
        self.btn_remove_YU.grid(row=0, column=3, sticky=E)
        #self.btn_done.grid(column=0, row=0,sticky=W)



        for c, item in enumerate(self.user_anime_YU):
                #print(str(item))
                items ="   " + str(item)   # add some bullet points or something

                self.libox_ur_anime.insert(END, items)



    def delete(self):
        selection = self.libox_ur_anime.curselection()
        for i in selection:
            self.libox_ur_anime.delete(selection)
            del self.user_anime_YU[i]

root = Tk()
root.title('Filter Listbox Test')
root.geometry("1013x303")

your_anime = []

app1 = AddAnime(your_anime, master=root)



root.mainloop()

print(your_anime)
