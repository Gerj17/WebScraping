from tkinter import *


class AddAnime(Frame):

    def __init__(self, list_user_anime, master=None):  # add  a list as parameter to store your anime
        Frame.__init__(self, master, bg="gray")
        self.user_anime = list_user_anime  # all of the anime the user likes
        putback = {}
        self.putback = putback
        self.pack()

        # -----Create widgets-----
        self.search_var = StringVar()
        self.search_var.trace("w", self.update_list)
        self.entry = Entry(self, textvariable=self.search_var, width=60)
        self.label_0 = Label(self, text="Search")
        self.label_1 = Label(self, text="All Anime ", )
        self.label_2 = Label(self, text="Your Anime ", )
        self.btn_remove = Button(self, text="Remove <---", command=self.Remove, padx=2, pady=2)
        self.btn_select = Button(self, text="ADD --->", command=self.Select, padx=2, pady=2)
        self.btn_done = Button(self, text="Done", padx=1, command=self.quit)  # make the font larger
        self.libox_all_anime = Listbox(self, selectmode=SINGLE, width=77, height=15)
        self.textbox_choices = Listbox(self, selectmode=SINGLE, width=77, height=15)
        self.scrollbar1 = Scrollbar(self)
        self.scrollbar2 = Scrollbar(self)

        # -----Place widget in frame-----
        self.entry.grid(row=0, column=1, padx=10, pady=3)
        self.label_0.grid(row=0, column=0, padx=18, pady=3, sticky=(N, S, E, W))
        self.label_1.grid(row=1, column=0, padx=18, columnspan=2, pady=3, )
        self.label_2.grid(row=1, column=3, padx=18, columnspan=2, pady=3, )
        self.libox_all_anime.grid(row=2, column=0, padx=15, pady=3, columnspan=2)
        self.textbox_choices.grid(row=2, column=3, padx=15, pady=3, columnspan=2)
        self.btn_select.grid(row=2, column=2)
        self.btn_remove.grid(row=3, column=3, sticky=E)
        self.btn_done.grid(row=3, column=1, padx=10)
        self.scrollbar1.grid(row=2, column=0, padx=15, pady=3, columnspan=2, sticky=(N, S, E))
        self.scrollbar2.grid(row=2, column=3, padx=15, pady=3, columnspan=2, sticky=(N, S, E))

        #  -----configure scrollbars-----
        self.libox_all_anime.configure(yscrollcommand=self.scrollbar1.set)
        self.textbox_choices.configure(yscrollcommand=self.scrollbar1.set)

        self.scrollbar1.configure(command=self.libox_all_anime.yview)
        self.scrollbar2.configure(command=self.textbox_choices.yview)

        # ----- Function for updating the list/doing the search.------
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
            self.textbox_choices.insert(END, entered + '\n')
            self.user_anime.append(entered)
            self.libox_all_anime.delete(selection)
            self.putback[entered] = selection

    def Remove(self):
        selection = self.textbox_choices.curselection()
        for i in selection:
            clicked = self.textbox_choices.get(i)  # the name of the clicked anime
            location = self.putback[clicked[:-1]]
            self.libox_all_anime.insert(location, clicked)
            self.textbox_choices.delete(selection)
            del self.user_anime[i]

    # def final(self):

    # def maintain  add a function that maintains the status of the listbox's

    def close(self):
        # self.final()
        """Quit the Tcl interpreter. All widgets will be destroyed."""
        # self.pack_forget()
        self.tk.quit()


class YouAnime(Frame):
    def __init__(self, list_user_anime, master=None):  # add  a list as parameter to store your anime
        Frame.__init__(self, master, bg="green")
        self.pack()
        self.user_anime_YU = list_user_anime  # all of the anime the user likes

        self.lbl_title = Label(self, text="Your Anime !!", padx=10, )
        self.btn_remove_YU = Button(self, text="Remove", padx=2, relief=RAISED, command=self.delete)
        self.libox_ur_anime = Listbox(self, selectmode=SINGLE, width=90, height=15, bg="grey")
        self.btn_done = Button(self, text="Done", padx=7, command=self.quit)  # make the font larger ####
        self.scrollbar3 = Scrollbar(self, )
        self.create_ur_anime()

        self.animedescription = AnimeDescription

        self.libox_ur_anime.bind('<Double-Button-1>', self.get_anime_name)

    def create_ur_anime(self):
        self.lbl_title.grid(row=0, column=2, sticky=W)
        self.libox_ur_anime.grid(row=1, column=0, columnspan=4)
        self.btn_remove_YU.grid(row=0, column=3, sticky=E)
        # self.btn_done.grid(column=0, row=0,sticky=W)
        self.scrollbar3.grid(row=1, column=3, sticky=(E, N, S), )

        self.libox_ur_anime.configure(yscrollcommand=self.scrollbar3.set)
        self.scrollbar3.configure(command=self.libox_ur_anime.yview)

        for c, item in enumerate(self.user_anime_YU):
            # print(str(item))
            items = "   " + str(item)  # add some bullet points or something

            self.libox_ur_anime.insert(END, items)

    def delete(self):
        selection = self.libox_ur_anime.curselection()
        for i in selection:
            self.libox_ur_anime.delete(selection)
            del self.user_anime_YU[i]

    def get_anime_name(self, event):
        selection = self.libox_ur_anime.curselection()
        for i in selection:
            anime_name = self.libox_ur_anime.get(i)
            self.animedescription.place_anime_info(AnimeDescription(), anime_name)
            #print(anime_name)
            return anime_name
            # self.pack_forget()

    def unpack(self):
        print("DID IT ")
        return self.pack_forget()



            

class AnimeDescription(Frame):
    def __init__(self,  master=None):  # add  a list as parameter to store your anime
        from pickle import load
        Frame.__init__(self, master, bg="red")

        all_anime = load(open("testing_save_.p", "rb"))
        self.all_anime = all_anime

        # ------Store classes as variables/Instances-----
        self.youranime = YouAnime

        # -----Create Widgets-----
        self.label_title = Label(self, text="Title :")
        self.label_genre = Label(self, text="Genre :")
        self.label_release_date = Label(self, text="Release Date :")
        self.label_plot = Label(self, text="Plot")
        self.description = Text(self, bg="pink")
        self.description2 = Text(self, bg="pink")
        self.pack()

        #for key, value in all_anime.items():
        #print(key, "=", value)

        # -----Place widgets-----
    #def place_widgets(self):
        self.label_title.grid(column=1)
        self.label_genre.grid(row=3, column=1)
        self.label_release_date.grid(row=4, column=1)
        self.label_plot.grid(row=5, column=1, sticky=W)
        #self.description2.grid(row=6, column=1)


        #self.description.insert(END, self.all_anime['009 Re:Cyborg'][0])  # string formatting


    def place_anime_info(self, name):

        self.youranime.unpack(YouAnime(list_user_anime=your_anime))

        self.description.grid(row=6, column=1)

        print('\n', name, '\n')
        the_name = name.strip()
        self.description.insert(END, self.all_anime[the_name][0])  # ---Plot--- string formatting

        #print("its here now ")
        #self.description.insert(END, self.all_anime[name][1])  # ---Genre---string formatting
        #self.description.insert(END, self.all_anime[name][2])  # --- Release Date ---string formatting





class YourParent:  # contoll AnimeDescription and YouAnime
    def __init__(self):

        # ------Store classes as variables/Instances-----
        self.youranime = YouAnime
        self.animedescription = AnimeDescription

        self.youranime(list_user_anime=your_anime)
        #self.animedescription()
        # self.animedescription.place_widgets(AnimeDescription())

        # self.nm_anime = self.youranime.get_anime_name(YouAnime(list_user_anime=your_anime))
        #  call method from Youanime




        # self.youranime.double_click(YouAnime(list_user_anime=your_anime), self.fill_description)


   # def fill_description(self, event):
    #    self.animedescription.place_anime_info(AnimeDescription(), self.nm_anime)  # call method from AnimeDescription
     #   #return 'break'





root = Tk()
root.title('Filter Listbox Test')
# root.geometry("1013x303")

your_anime = ['Terra Formars Revenge', 'Tesagure! Bukatsumono Encore ',
              'Tesagure! Bukatsumono Spin-off Purupurun Sharumu to Asobou', 'Tetsujin 28-go (Dub)',
              'Tetsuwan Birdy (Dub)', 'Tetsuwan Birdy Decode (Dub)', 'Tetsuwan Birdy Decode:02 (Dub)', 'Texhnolyze ',
              'The Cat Returns (Dub)', 'The Cat Returns', 'The Daughter of 20 Faces ', 'The Brave of Gold Goldran',
              'The Disappearance of Conan Edogawa: The Worst Two Days in History',
              'The Disappearance of Haruhi Suzumiya', 'The Epic of Zektbach OVA', 'The Galaxy Railways ',
              'The Familiar of Zero ', 'The Boy Who Saw the Wind', 'The Galaxy Railways (Dub)',
              'The Garden of Words (Dub)', 'The Girl Who Leapt Through Time', 'The Girl Who Leapt Through Time (Dub)',
              '009 Re:Cyborg (Dub)', '.hack//Sign (Dub)']
# your_anime = []
# app1 = AddAnime(your_anime, master=root)
# app1test = AddAnime(your_anime, root)
# app2 = YouAnime(your_anime, root)
# app3 = AnimeDescription(root)

app4 = YourParent()

root.mainloop()

print(your_anime)
