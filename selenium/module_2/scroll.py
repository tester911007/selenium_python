import math
import time

from selenium import webdriver

with webdriver.Chrome() as browser:
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)

    x = browser.find_element_by_id("input_value").text
    print(x)
    result = math.log(abs(12 * math.sin(int(x))))

    browser.find_element_by_id("answer").send_keys(str(result))

    button = browser.execute_script("return document.getElementsByTagName('button')[0].scrollIntoView();")

    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()

    browser.find_element_by_tag_name("button").click()
    time.sleep(15)
    browser.quit()
