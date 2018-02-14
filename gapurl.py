def parseurl(website):
    """Return a variable containing parsed website.

    Keyword arguments:
    Website -- the website to be parsed

    if BeautifulSoup4 not installed :
        ModuleNotFoundError: No module named 'bs4'

    store function in a variable so it can be used later on in a script
    """

    try:

        import urllib
        from urllib.request import Request, urlopen as uReq  # to open URL,page
        """Allows use of fake a web client.
         Its purpose is to avoid mod_security or some similar server security feature which blocks
        known spider/bot user agents.
        """
        from bs4 import BeautifulSoup as soup  # parse HTML

        # use fake web client,open website, download HTML, store in a variable and close connection
        req = Request(website, headers={'User-Agent': 'Mozilla/5.0'})  # in case of mod_security
        get_site = uReq(req)  # open website
        html_page_site = get_site.read()  # store read file in variable
        get_site.close()  # close web connection

        # parse the page
        page_soup = soup(html_page_site, "html.parser")

        return page_soup

    except urllib.error.URLError:
        print("Check your internet connection or check you URL link ")


