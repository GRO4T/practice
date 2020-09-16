#! python3
# Command Line Emailer - ....
# Usage: ...

# email: kowal.test.jan
# haslo: Haslo123

import logging 
from selenium import webdriver
from impl import accept_data_collection, login, send_email

profile = webdriver.FirefoxProfile()
profile.set_preference("permissions.default.desktop-notification", 1);
profile.set_preference("geo.prompt.testing", True)
profile.set_preference("geo.prompt.testing.allow", True)
profile.set_preference("geo.provider.testing", True)
browser = webdriver.Firefox(firefox_profile=profile)
browser.get('https://www.o2.pl/')

accept_data_collection(browser)
login(browser)
send_email(browser, "damkol123@interia.pl", "Test Email", "Elo Mordo jak leci?")

# browser.quit()


