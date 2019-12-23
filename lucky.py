#! /usr/bin/python3

# lucky.py      - takes a search term from cmd and opens mutiple tabs with search
# results from Google



#    Read cmd line arguments from sys.argv
#    Fetch the search results page with the requests module
#    Find the links to each search result
#    call webbrowser.open() function to open the new browser


try:
    import sys, webbrowser
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

print('Googling...') # display text while downloading the Google page


# to search
SEARCHVAR = sys.argv[1:]
query = 'http://google.com/search?q=' + ' '.join(SEARCHVAR)

for links in search(query, tld="co.in", num=10, stop=5, pause=2):
    print(links)

    webbrowser.open(links)
