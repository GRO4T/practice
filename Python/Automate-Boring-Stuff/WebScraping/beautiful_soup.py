import bs4
example_file = open('example.html')
example_soup = bs4.BeautifulSoup(example_file.read(), features='html.parser')
elems = example_soup.select('#author')
print(type(elems))
print(type(elems[0]))
print(str(elems[0]))
print(elems[0].attrs)
print(elems[0].get("id"))
