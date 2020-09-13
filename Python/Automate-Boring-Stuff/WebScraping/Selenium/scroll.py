from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get('http://nostarch.com')
html_elem = browser.find_element_by_tag_name('html')
# send keys to general web page by sending it to html element of the page
html_elem.send_keys(Keys.END) # scrolls to bottom
html_elem.send_keys(Keys.HOME) # scrolls to top
