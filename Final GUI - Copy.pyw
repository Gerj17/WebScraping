from tkinter import *
from pickle import load, dump

import tkinter  # for the try and except in the animedescrition class

root = Tk()

root.title('Filter Listbox Test')

# root.geometry("1013x303")

your_anime = []  # record all users anime

# print("your anime list ", your_anime)
# ---------- FUNCTIONS----------


# -----AddAnime Functions -----

# refer to " Youanime Functions for the second done function"

def create_AddAnime():
    entry.grid(row=0, column=1, padx=10, pady=3)
    label_0.grid(row=0, column=0, padx=18, pady=3, sticky=(N, S, E, W))
    label_1.grid(row=1, column=0, padx=18, columnspan=2, pady=3, )
    label_2.grid(row=1, column=3, padx=18, columnspan=2, pady=3, )
    libox_all_anime.grid(row=2, column=0, padx=15, pady=3, columnspan=2)
    libox_choices.grid(row=2, column=3, padx=15, pady=3, columnspan=2)
    btn_select.grid(row=2, column=2)
    btn_remove.grid(row=3, column=3, sticky=E)
    btn_done.grid(row=3, column=1, padx=10)
    scrollbar1.grid(row=2, column=0, padx=15, pady=3, columnspan=2, sticky=(N, S, E))
    scrollbar2.grid(row=2, column=3, padx=15, pady=3, columnspan=2, sticky=(N, S, E))
    # -----Run necessary functions------
    # ----- Function for updating the list/doing the search.------
    # It needs to be called here to populate the listbox.
    update_list()
    # # print('\n all the listbox content',libox_all_anime.get(0,END),"\n")
    update_libox_choices()
    update_libox_all_anime()



def update_list(*args):
    """ maintain the listbox containing all anime """

    search_term = search_var.get()
    all_anime = load(open("anime_save.p", "rb"))

    all_anime_list = []
    for key, value in all_anime.items():
        all_anime_list.append(key)

    libox_all_anime.delete(0, END)

    for item in all_anime_list:
        if search_term.lower() in item.lower():
            libox_all_anime.insert(END, item)


def Select():
    # print("running")
    selection = libox_all_anime.curselection()
    for i in selection:
        entered = libox_all_anime.get(i)
        libox_choices.insert(END, entered + '\n')
        your_anime.append(entered)
        libox_all_anime.delete(selection)
        putback[entered] = selection


def Remove():
    selection = libox_choices.curselection()
    for i in selection:
        clicked = libox_choices.get(i)  # the name of the clicked anime
        # print(clicked)
        try:
            location = putback[clicked[:-1]]
        except KeyError:
            # print("ran into KeyError in line 'def Remove'")
            location = putback[clicked]
        if clicked not in libox_all_anime.get(0, END):
            libox_all_anime.insert(location, clicked)
            libox_choices.delete(selection)
        else:
            libox_choices.delete(selection)
        del your_anime[i]


# def final():
# def maintain  add a function that maintains the status of the listbox's

def update_libox_choices():
    libox_choices.delete(0, END)
    for x in updated_your_anime():
        libox_choices.insert(END, x)


def update_libox_all_anime():
    """ function that ensures that the anime in user choosen listbox isn't in all anime listbox """
    ## print("update_libox_all_anime is runnig")
    a = libox_all_anime.get(0, END)
    ## print("the contents or a :", a)
    b = []
    for x in a:
        ## print("this is x: ", x)
        b.append(x)
        ## print(x)
    for x in updated_your_anime():
        if x in b:
            b.remove(x)
    c = sorted(b)
    ## print(b)
    libox_all_anime.delete(0, END)
    for x in c:
        libox_all_anime.insert(END, x)


def close():
    # final()
    """Quit the Tcl interpreter. All widgets will be destroyed."""
    # pack_forget(p
    dump(your_anime, open("users_anime_save.p", "wb"))  # store user anime in file
    dump(putback, open("putback_save.p", "wb"))  # store putback in file
    frame1.quit()


# -----YouAnime Functions -----

def create_YouAnime():
    lbl_title.grid(row=0, column=2, sticky=W)
    libox_ur_anime.grid(row=1, column=0, columnspan=4, )
    # sticky=(N, S, E, W))
    btn_remove_YU.grid(row=0, column=3, sticky=E)
    btn_add_anime1.grid(row=0, column=0, sticky=W)
    # btn_done.grid(column=0, row=0,sticky=W)
    scrollbar3.grid(row=1, column=3, sticky=(E, N, S), )

    libox_ur_anime.configure(yscrollcommand=scrollbar3.set)
    scrollbar3.configure(command=libox_ur_anime.yview)
    populate_YouAnime()


def populate_YouAnime():
    for c, item in enumerate(updated_your_anime()):
        # # print(str(item))
        items = "   " + str(item)  # add some bullet points or something
        # libox_ur_anime.delete(0, END)
        libox_ur_anime.insert(END, items)
    for x in updated_your_anime():
        if x not in your_anime:
            your_anime.append(x)


def delete():
    selection = libox_ur_anime.curselection()
    # print(selection)
    for i in selection:
        libox_ur_anime.delete(selection)
        try:
            del your_anime[i]
            dump(your_anime, open("users_anime_save.p", "wb"))  # store user anime in file
        except:
            pass


def get_and_set_anime_name(event):
    selection = libox_ur_anime.curselection()
    for i in selection:
        anime_name = libox_ur_anime.get(i)
        create_AnimeDescription()
        # print("makes frame3")
        youanime_description()  # unpacks frame2
        place_anime_info(anime_name)
        # # print(anime_name)
        return anime_name
        # pack_forget()


def add_you_anime1():  # add an anime to the users personal list
    # print("\nupdated anime list \n", updated_your_anime(), "\n")
    frame2.pack_forget()
    create_AddAnime()
    frame1.pack()
    btn_done.grid_forget()
    btn_done3 = Button(frame1, text="Done", padx=1, command=done3)  # make the font larger
    btn_done3.grid(row=3, column=1, padx=10)


def done3():  # done button for adding anime from youanime
    frame1.pack_forget()
    dump(your_anime, open("users_anime_save.p", "wb"))  # store user anime in file
    dump(putback, open("putback_save.p", "wb"))  # store putback in file
    # ensure YouAnime listbox is updated
    libox_ur_anime.delete(0, END)
    populate_YouAnime()
    frame2.pack()
    # print("\nupdated anime list \n", updated_your_anime(), "\n")
    # print("\nsaved putback \n", putback)


# -----AnimeDescription Functions-----

def create_AnimeDescription():
    frame3.pack()
    label_title.grid(column=1)
    label_genre.grid(row=3, column=1)
    label_release_date.grid(row=4, column=1)
    label_plot.grid(row=5, column=1, sticky=W)
    btn_back.grid(row=0, column=1, sticky=W)
    # description2.grid(row=6, column=1)

    # description.insert(END, all_anime['009 Re:Cyborg'][0])  # string formatting


def place_anime_info(name):
    # youranime.unpack(YouAnime(list_user_anime=your_anime))
    # print("called")
    description.grid(row=6, column=1)

    try:
        description.delete(1.0, END)
    except:
        print("didn't delete anything ")
    # print('\n', name, '\n')
    the_name = name.strip()

    description.insert(END, all_anime[the_name][0])  # ---Plot--- string formatting
    # youranime.unpack(YouAnime(list_user_anime=your_anime))
    # print("End calling")
    # # print("its here now ")
    # description.insert(END, all_anime[name][1])  # ---Genre---string formatting
    # description.insert(END, all_anime[name][2])  # --- Release Date ---string formatting
    the_title.set("Title : " + the_name)
    the_genre.set("Genre : " + ', '.join(map(str, all_anime[the_name][1])))
    the_release_date.set("Release Date : " + all_anime[the_name][2])


def back_btn():
    # print(description.delete(END))
    frame3.pack_forget()
    # frame3.destroy()
    frame2.pack()


# ----- Interaction of anime description pages-----

def youanime_description():  # outline how the frame 2 & 3 interact will interact
    frame2.pack_forget()
    # save changes to list of animes

#
def updated_your_anime():
    try:
        your_anime_updated = load(open("users_anime_save.p", "rb"))
        return your_anime_updated
    except FileNotFoundError:
        print("'FileNotFoundError', your_anime_updated doesn\'t exist")
        return your_anime


# --------CONTENT----------

# -----AddAnime content-----

frame1 = Frame(root, bg="gray")
your_anime = your_anime  # all of the anime the user likes
try:
    putback = load(open("putback_save.p", "rb"))
except FileNotFoundError:
    print("'FileNotFoundError', putback doesn\'t exist")
    putback = {}
# print("initial putback\n", putback)  #######3
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
libox_choices = Listbox(frame1, selectmode=SINGLE, width=77, height=15)
scrollbar1 = Scrollbar(frame1)
scrollbar2 = Scrollbar(frame1)

# -----configure scrollbars-----
libox_all_anime.configure(yscrollcommand=scrollbar1.set)
libox_choices.configure(yscrollcommand=scrollbar1.set)

scrollbar1.configure(command=libox_all_anime.yview)
scrollbar2.configure(command=libox_choices.yview)

# -----Run necessary function------
# ----- Function for updating the list/doing the search.------
# It needs to be called here to populate the listbox.
# update_list()


# -----Youanime Content -----

frame2 = Frame(root, bg="green")
frame2.pack()
your_anime = your_anime  # all of the anime the user likes

lbl_title = Label(frame2, text="Your Anime !!", padx=10, )
btn_remove_YU = Button(frame2, text="Remove", padx=2, relief=RAISED, command=delete)
libox_ur_anime = Listbox(frame2, selectmode=SINGLE, width=106, height=15, bg="grey")
btn_done2 = Button(frame2, text="Done", padx=7, command=quit)  # make the font larger ####
btn_add_anime1 = Button(frame2, text="Add Anime", padx=3, command=add_you_anime1)  # make the font larger ####
scrollbar3 = Scrollbar(frame2, )

libox_ur_anime.bind('<Double-Button-1>', get_and_set_anime_name)

# -----AnimeDescription content-----

frame3 = Frame(root, bg="red")

# all_anime = load(open("testing_save_.p", "rb"))  # TESTING PURPOSES
all_anime = load(open("anime_save.p", "rb"))  # TESTING PURPOSES

# string variables to update the labels
the_title = StringVar()
the_genre = StringVar()
the_release_date = StringVar()

label_title = Label(frame3, textvariable=the_title, )
label_genre = Label(frame3, textvariable=the_genre, )
label_release_date = Label(frame3, textvariable=the_release_date, )
label_plot = Label(frame3, text="Plot", )
description = Text(frame3, bg="pink")
description2 = Text(frame3, bg="green")
btn_back = Button(frame3, text="<---Back", padx=7, command=back_btn)

frame3.pack()

# create_AddAnime()
create_YouAnime()
root.mainloop()

# print(your_anime)
