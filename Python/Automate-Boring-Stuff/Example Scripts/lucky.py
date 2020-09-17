#! python3
# lucky.py - Opens several Google search results.
import requests
import sys
import webbrowser
import bs4

print('Googling...')
# display text while downloading the Google page
s = 'http://google.com/search?q=' + ' '.join(sys.argv[1:])
print(s)
res = requests.get('https://google.com/search?q=' + '+'.join(sys.argv[1:]))
res.raise_for_status()

# TODO: Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, features="html.parser")

# print(soup.prettify())

# TODO: Open a browser tab for each result.
#link_elems = soup.find_all(class_="a")
link_elems = soup.select(".kCrYT a")
num_open = min(5, len(link_elems))

for i in range(num_open):
    webbrowser.open('http://google.com' + link_elems[i].get('href'))
