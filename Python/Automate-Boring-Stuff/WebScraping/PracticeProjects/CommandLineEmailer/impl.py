#! python3
# Here I implement most of the functions used by a program

import logging 
from selenium import webdriver
from time import sleep

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s -  %(message)s')
logging.disable(logging.DEBUG)

def accept_data_collection(browser):
    found = False
    while (not found):
        logging.info("Accepting Data Collection")
        try:
            accept_button = browser.find_element_by_xpath("//button[contains(text(), 'AKCEPTUJĘ')]")
            accept_button.click()
            found = True
        except:
            sleep(1)

def accept_cookies(browser):
    logging.info("Accepting Cookies")
    try:
        accept_button = browser.find_element_by_xpath("//div[@id='WP-cookie-info']//div[1]//div[1]")
        accept_button.click()
        return True
    except:
        sleep(1)
        return False

def skip_ad(browser):
    logging.info("Skipping Ad")
    try:
        skip_button = browser.find_element_by_xpath("//div[contains(text(), 'Przejdź')]")
        skip_button.click()
        return True
    except:
        sleep(1)
        return False

def expand_login_form(browser):
    logging.info("Expanding Login Form")
    try:
        expand_login_button = browser.find_element_by_xpath('//span[contains(text(), "Poczta")]')
        expand_login_button.click()
        return True
    except:
        sleep(1)
        return False
    
def login(browser):
    # skip ads, accept cookies and expand login form
    cookies_accepted = False
    ad_skipped = False
    login_form_expanded = False
    while (not login_form_expanded):
        if not cookies_accepted:
            cookies_accepted = accept_cookies(browser)
        if not ad_skipped:
            ad_skipped = skip_ad(browser)
        login_form_expanded = expand_login_form(browser)

    # provide credentials and login
    login_form = browser.find_element_by_xpath("//form[@id='loginForm']")
    email_field = login_form.find_element_by_xpath("//input[@name='username']")
    password_field = login_form.find_element_by_xpath("//input[@name='password']")
    email_field.send_keys("kowal.test.jan")
    password_field.send_keys("Haslo123")
    submit_button = login_form.find_element_by_xpath("//button[@type='submit']")
    submit_button.click()

def send_email(browser, recipient, title, email_body):
    email_sent = False
    while (not email_sent): 
        logging.info
        try:
            new_email_button = browser.find_element_by_xpath("//button[contains(text(), 'Napis')]")
            new_email_button.click()
            email_sent = True
        except:
            sleep(1)
            pass


    
