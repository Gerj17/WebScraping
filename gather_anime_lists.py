def gather_gogo_anime():
    from gapurl import parseurl
    from string import ascii_lowercase as alphabet
    """adds anime link, plot,genres and release date to dictionary name anime with the key being the anime name
    """

    gogo = 'http://www3.gogoanime.tv/'
    gogo_anime_list = 'http://www3.gogoanime.tv/anime-list-0?page=1'

    counter = 1  # iterate through alphabet to anime url
    while True:
        print(gogo_anime_list)
        print('Parsing')
        soup = parseurl(gogo_anime_list)
        listing = soup.find("ul", {"class", "listing"}).findAll("li")
        print('Done Parsing')

        # adds anime link, plot, genres and release date to dictionary called all_anime with the key being the anime
        # name

        # Cycle through Letter category of anime and gather data
        for li in listing:
            # get title of anime
            title = li.a.text

            # get link to anime has to concatenated with gogo (loops once)
            for url in li.find_all('a', href=True):
                link = gogo + (url['href'])

                if title in all_anime:
                    continue

                print('Second Parsing')
                anime_soup = parseurl(link)
                print('Done Second Parsing')
                anime_info = anime_soup.find("div", {"class", "anime_info_body_bg"}).findAll("p")

                plot = anime_info[2].text

                gets_genre = anime_info[3].findAll('a')
                genre = []
                for x in gets_genre:
                    genre.append(x['title'])

                release_date = anime_info[4].text[9:]

                """
                # may add if useful Status
                status = anime_info[5].text[8:]

                latest_episodes = anime_soup.find("div", {"class", "anime_video_body"})

                if status == "Completed":
                    episodes = latest_episodes.ul.li.a.text[2:]
                    all_anime[title] = episodes
                else:
                    current_episode = latest_episodes.ul.li.a.text[2:]
                    all_anime[title] = current_episode
                    """

                all_anime[title] = plot, genre, release_date  # Final product

                """consider that the website knows how many episodes a show should have and gogo has current episodes 
                probably probably can use that with an if statement to give 'current episode', 'expected episode' and 
                'episodes remaining' """  # Code for consideration

        # Breaks loop
        if not listing:
            print('Success!!')
            break

        # Update the url to get every letter category of anime
        counter += 1
        if counter < 10:
            gogo_anime_list = str(gogo_anime_list[:-1] + str(counter))
            continue
        gogo_anime_list = str(gogo_anime_list[:-2] + str(counter))


# Dictionary containing all anime

all_anime = {}
gather_gogo_anime()

# read and write dictionary in a file (Dictionaries can't be stored in a file as a string)
from pickle import dump, load

dump(all_anime, open("anime_save_.p", "wb"))  # store anime in file
all_anime = load(open("anime_save_.p", "rb"))
