from pickle import load

all_anime = load(open("testing_save_.p", "rb"))

for key, value in all_anime.items():
    print(key, "=", value)


