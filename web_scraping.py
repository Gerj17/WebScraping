from gather_anime_lists import gather_gogo_anime
from pickle import dump, load

# The websites
gogo = 'http://www3.gogoanime.tv/'
gogo_anime_list = 'http://www3.gogoanime.tv/anime-list-0'
croll = 'http://www.crunchyroll.com/'  # FOR LATER USE refer to Evernote for use
anime_list = 'https://myanimelist.net/'  # FOR LATER USE refer to Evernote for use
# maybe store websites is a dictionary

all_anime = {}

gather_gogo_anime()
dump(all_anime, open("anime_save_.p", "wb"))  # store anime in file

all_anime = load(open("anime_save_.p", "rb"))


