from tkinter import *
import tkinter  # for the try and except in the animedescrition class

root = Tk()
root.title('Filter Listbox Test')
# root.geometry("1013x303")

# your_anime = []

your_anime = ['Terra Formars Revenge', 'Tesagure! Bukatsumono Encore ',
              'Tesagure! Bukatsumono Spin-off Purupurun Sharumu to Asobou', 'Tetsujin 28-go (Dub)',
              'Tetsuwan Birdy (Dub)', 'Tetsuwan Birdy Decode (Dub)', 'Tetsuwan Birdy Decode:02 (Dub)', 'Texhnolyze ',
              'The Cat Returns (Dub)', 'The Cat Returns', 'The Daughter of 20 Faces ', 'The Brave of Gold Goldran',
              'The Disappearance of Conan Edogawa: The Worst Two Days in History',
              'The Disappearance of Haruhi Suzumiya', 'The Epic of Zektbach OVA', 'The Galaxy Railways ',
              'The Familiar of Zero ', 'The Boy Who Saw the Wind', 'The Galaxy Railways (Dub)',
              'The Garden of Words (Dub)', 'The Girl Who Leapt Through Time', 'The Girl Who Leapt Through Time (Dub)',
              '009 Re:Cyborg (Dub)', '.hack//Sign (Dub)']

# ---------- FUNCTIONS----------


# -----AddAnime Functions -----

def create_AddAnime():
    entry.grid(row=0, column=1, padx=10, pady=3)
    label_0.grid(row=0, column=0, padx=18, pady=3, sticky=(N, S, E, W))
    label_1.grid(row=1, column=0, padx=18, columnspan=2, pady=3, )
    label_2.grid(row=1, column=3, padx=18, columnspan=2, pady=3, )
    libox_all_anime.grid(row=2, column=0, padx=15, pady=3, columnspan=2)
    textbox_choices.grid(row=2, column=3, padx=15, pady=3, columnspan=2)
    btn_select.grid(row=2, column=2)
    btn_remove.grid(row=3, column=3, sticky=E)
    btn_done.grid(row=3, column=1, padx=10)
    scrollbar1.grid(row=2, column=0, padx=15, pady=3, columnspan=2, sticky=(N, S, E))
    scrollbar2.grid(row=2, column=3, padx=15, pady=3, columnspan=2, sticky=(N, S, E))
    # -----Run necessary function------
    # ----- Function for updating the list/doing the search.------
    # It needs to be called here to populate the listbox.
    update_list()

def show_anime():
    return user_anime


def show_putback():
    return putback


def update_list(*args):
    search_term = search_var.get()

    # Just a generic list to populate the listbox
    from pickle import load
    all_anime = load(open("anime_save_.p", "rb"))

    all_anime_list = []
    for key, value in all_anime.items():
        all_anime_list.append(key)

    libox_all_anime.delete(0, END)

    for item in all_anime_list:
        if search_term.lower() in item.lower():
            libox_all_anime.insert(END, item)


def Select():
    print("running")
    selection = libox_all_anime.curselection()
    for i in selection:
        entered = libox_all_anime.get(i)
        textbox_choices.insert(END, entered + '\n')
        user_anime.append(entered)
        libox_all_anime.delete(selection)
        putback[entered] = selection


def Remove():
    selection = textbox_choices.curselection()
    for i in selection:
        clicked = textbox_choices.get(i)  # the name of the clicked anime
        location = putback[clicked[:-1]]
        libox_all_anime.insert(location, clicked)
        textbox_choices.delete(selection)
        del user_anime[i]


# def final():
# def maintain  add a function that maintains the status of the listbox's

def close():
    # final()
    """Quit the Tcl interpreter. All widgets will be destroyed."""
    # pack_forget()
    frame1.quit()


# -----YouAnime Functions -----

def create_YouAnime():
    lbl_title.grid(row=0, column=2, sticky=W)
    libox_ur_anime.grid(row=1, column=0, columnspan=4, )
    # sticky=(N, S, E, W))
    btn_remove_YU.grid(row=0, column=3, sticky=E)
    # btn_done.grid(column=0, row=0,sticky=W)
    scrollbar3.grid(row=1, column=3, sticky=(E, N, S), )

    libox_ur_anime.configure(yscrollcommand=scrollbar3.set)
    scrollbar3.configure(command=libox_ur_anime.yview)

    for c, item in enumerate(user_anime_YU):
        # print(str(item))
        items = "   " + str(item)  # add some bullet points or something

        libox_ur_anime.insert(END, items)


def delete():
    selection = libox_ur_anime.curselection()
    for i in selection:
        libox_ur_anime.delete(selection)
        del user_anime_YU[i]


def get_and_set_anime_name(event):
    selection = libox_ur_anime.curselection()
    for i in selection:
        anime_name = libox_ur_anime.get(i)
        create_AnimeDescription()
        place_anime_info(anime_name)
        # print(anime_name)
        return anime_name
        # pack_forget()


def unpack():
    print("DID IT ")
    # pack_forget()
    # return pack_forget()

# -----AnimeDescription Functions-----
def create_AnimeDescription():
    label_title.grid(column=1)
    label_genre.grid(row=3, column=1)
    label_release_date.grid(row=4, column=1)
    label_plot.grid(row=5, column=1, sticky=W)
    # description2.grid(row=6, column=1)

    # description.insert(END, all_anime['009 Re:Cyborg'][0])  # string formatting


def place_anime_info(name):
    # youranime.unpack(YouAnime(list_user_anime=your_anime))

    if len(description.get("1.0", "end-1c")) == 0:
        # pack_forget()
        try:
            description.delete(0, END)
            print("the widget is empty")
        except:
            print("ran into error")
            print(description)
            print()

        # pack()
    else:
        print("it not ")
        description.delete(0, END)

    description.grid(row=6, column=1)

    print('\n', name, '\n')
    the_name = name.strip()
    description.insert(END, all_anime[the_name][0])  # ---Plot--- string formatting
    # youranime.unpack(YouAnime(list_user_anime=your_anime))

    # print("its here now ")
    # description.insert(END, all_anime[name][1])  # ---Genre---string formatting
    # description.insert(END, all_anime[name][2])  # --- Release Date ---string formatting

# --------CONTENT----------

# -----AddAnime content-----

frame1 = Frame(root, bg="gray")
user_anime = your_anime  # all of the anime the user likes
putback = {}
putback = putback
frame1.pack()

# -----Create widgets-----
search_var = StringVar()
search_var.trace("w", update_list)
entry = Entry(frame1, textvariable=search_var, width=60)
label_0 = Label(frame1, text="Search")
label_1 = Label(frame1, text="All Anime ", )
label_2 = Label(frame1, text="Your Anime ", )
btn_remove = Button(frame1, text="Remove <---", command=Remove, padx=2, pady=2)
btn_select = Button(frame1, text="ADD --->", command=Select, padx=2, pady=2)
btn_done = Button(frame1, text="Done", padx=1, command=quit)  # make the font larger
libox_all_anime = Listbox(frame1, selectmode=SINGLE, width=77, height=15)
textbox_choices = Listbox(frame1, selectmode=SINGLE, width=77, height=15)
scrollbar1 = Scrollbar(frame1)
scrollbar2 = Scrollbar(frame1)

# -----configure scrollbars-----
libox_all_anime.configure(yscrollcommand=scrollbar1.set)
textbox_choices.configure(yscrollcommand=scrollbar1.set)

scrollbar1.configure(command=libox_all_anime.yview)
scrollbar2.configure(command=textbox_choices.yview)

# -----Run necessary function------
# ----- Function for updating the list/doing the search.------
# It needs to be called here to populate the listbox.
#update_list()

# -----Youanime Content -----

frame2 = Frame(root, bg="green")
frame2.pack()
user_anime_YU = your_anime  # all of the anime the user likes

lbl_title = Label(frame2, text="Your Anime !!", padx=10, )
btn_remove_YU = Button(frame2, text="Remove", padx=2, relief=RAISED, command=delete)
libox_ur_anime = Listbox(frame2, selectmode=SINGLE, width=106, height=15, bg="grey")
btn_done = Button(frame2, text="Done", padx=7, command=quit)  # make the font larger ####
scrollbar3 = Scrollbar(frame2, )

libox_ur_anime.bind('<Double-Button-1>', get_and_set_anime_name)


# -----AnimeDescription content-----
from pickle import load

frame3 = Frame(root, bg="red")

all_anime = load(open("testing_save_.p", "rb"))  # TESTING PURPOSES
all_anime = all_anime

label_title = Label(frame3, text="Title :")
label_genre = Label(frame3, text="Genre :")
label_release_date = Label(frame3, text="Release Date :")
label_plot = Label(frame3, text="Plot")
description = Text(frame3, bg="pink")
description2 = Text(frame3, bg="green")
frame3.pack()



#create_AddAnime()
create_YouAnime()
root.mainloop()

print(your_anime)
