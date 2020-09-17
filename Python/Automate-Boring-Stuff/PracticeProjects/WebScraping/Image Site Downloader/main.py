#! python3
# Image Site Downloader - downloads specified number of images with given category from Imgur.com
#
# "Usage: python main.py <search_term> [number_of_images]"

import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
from time import sleep
import os
from datetime import datetime
import requests


images_to_be_downloaded = 10


def usage():
    print("Usage: python main.py <search_term> [number_of_images]")


def accept_cookies(browser):
    logging.info("Accepting Cookies")
    try:
        accept_button = browser.find_element_by_xpath("//button[text()='I accept']")
        accept_button.click()
    except Exception as err:
        logging.error(err)
        sleep(1)


def search_term(browser, term):
    while 1:
        try:
            accept_cookies(browser)
            logging.info("Searching for term")
            search_field = browser.find_element_by_class_name("Searchbar-textInput")
            search_field.send_keys(term)
            search_submit_button = browser.find_element_by_class_name("Searchbar-submitInput")
            search_submit_button.click()
            break
        except Exception as err:
            logging.error(err)
            sleep(1)


def download_first_n_images(browser, n):
    logging.info("Downloading images")

    # Create a directory for images
    date = datetime.now().strftime("%d_%m_%Y")
    i = 0
    images_path = "{}/{}".format(date, str(i))
    while os.path.isdir(images_path):
        i += 1
        images_path = "{}/{}".format(date, str(i))
    os.makedirs(images_path)

    # Download and store images
    for i in range(n):
        while 1:
            try:
                # Get image url
                img_tile = browser.find_element_by_xpath("//div[@class='cards']//div[{}]//a[1]".format(str(i + 1)))
                img_tile.click()
                img_placeholder = browser.find_element_by_class_name("image-placeholder")
                img_url = img_placeholder.get_attribute("src")
                # Download the image
                logging.info("Downloading image " + img_url)
                img_response = requests.get(img_url)
                img_response.raise_for_status()
                # Save the image
                img_file = open(os.path.join(images_path, os.path.basename(img_url)), 'wb')
                for chunk in img_response.iter_content(100000):
                    img_file.write(chunk)
                img_file.close()
                # Return one page
                browser.back()
                break
            except Exception as err:
                logging.error(err)
                sleep(1)

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        usage()
        sys.exit("Wrong number of arguments!")

    logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s -  %(message)s')
    logging.disable(logging.DEBUG)

    browser = webdriver.Firefox()
    browser.get("https://imgur.com/")

    search_term(browser, sys.argv[1])
    download_first_n_images(browser, int(sys.argv[2]))

    exit("Success")

if __name__ == "__main__":
    main()
