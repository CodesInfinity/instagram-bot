from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def login(browser):
    browser.get("https://www.instagram.com/?hl=es")
    time.sleep(2)
    username = browser.find_element_by_css_selector("[name='username']")
    password = browser.find_element_by_css_selector("[name='password']")
    login = browser.find_element_by_css_selector("button")

    username.send_keys("your_name_account")
    password.send_keys("your_password")
    login.click()

    time.sleep(4)

def Visit_Tag(browser, url):
    sleepy_time = 5
    browser.get(url)
    time.sleep(sleepy_time)

    pictures = browser.find_elements_by_css_selector("div[class='_9AhH0']")

    image_count = 0

    for picture in pictures:
        if image_count >= 2:
            break

        picture.click()
        time.sleep(sleepy_time)

        corazon = browser.find_element_by_css_selector("[aria-label='Me gusta']")
        corazon.click()

        cerrar = browser.find_element_by_css_selector("[aria-label='Cerrar']")
        cerrar.click()

        image_count += 1
        time.sleep(sleepy_time)

def main():
    browser = webdriver.Chrome()
    login(browser)

    tags = [ 
        "programming",
        "softwaredeveloper",
        "programminglife",
        "programmerslife",
        "programmerlife",
        "developerlife",
        "programmers",
    ]

    while True:
        for tag in tags:
            Visit_Tag(browser, f"https://www.instagram.com/explore/tags/{tag}")
        time.sleep(3600)

main()
