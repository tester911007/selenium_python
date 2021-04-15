import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

with webdriver.Chrome() as browser:
    # link = "http://suninjuly.github.io/selects1.html"
    link = "http://suninjuly.github.io/selects2.html"
    browser.get(link)

    x1 = browser.find_element_by_id("num1").text
    x2 = browser.find_element_by_id("num2").text
    result = str(int(x1) + int(x2))

    select = Select( browser.find_element_by_id("dropdown"))
    select.select_by_value(result)

    button = browser.find_element_by_tag_name("button").click()

    time.sleep(15)
    browser.quit()
