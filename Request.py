

# The first page of the GUI

def request_anime(finished): # this will be integrated with tikinter
    anime_request = []
    while True:
        requests = input('Enter the anime you would like to know about')
        anime_request.append(requests)
        if finished:
            return anime_request




