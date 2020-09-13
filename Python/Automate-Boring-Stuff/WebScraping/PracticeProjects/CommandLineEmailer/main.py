#! python3
# Command Line Emailer - ....
# Usage: ...

# email: kowal.test.jan
# haslo: Haslo123

import logging 
from selenium import webdriver
from impl import accept_data_collection, login, send_email

browser = webdriver.Firefox()
browser.get('https://www.o2.pl/')

accept_data_collection(browser)
login(browser)
send_email(browser, "damkol123@interia.pl", "Test Email", "Elo Mordo jak leci?")

# browser.quit()


