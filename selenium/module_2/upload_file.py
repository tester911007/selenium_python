import os.path
import time

from selenium import webdriver

with webdriver.Chrome() as browser:
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    first_name = browser.find_element_by_name("firstname")
    first_name.send_keys("Vlad")

    last_name = browser.find_element_by_name("lastname")
    last_name.send_keys("Tester")

    email = browser.find_element_by_name("email")
    email.send_keys("test@mail.ru")

    # Путь к текущей дериктории
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    send_file = browser.find_element_by_id("file").send_keys(file_path)

    browser.find_element_by_tag_name("button").click()

    time.sleep(15)
    browser.quit()

