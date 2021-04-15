from selenium import webdriver
import time, math

link = "http://suninjuly.github.io/find_link_text"
hidden_link = str(math.ceil(math.pow(math.pi, math.e) * 10000))

with webdriver.Chrome() as browser:
    browser.get(link)
    found_link = browser.find_element_by_partial_link_text(hidden_link)
    found_link.click()

    input1 = browser.find_element_by_name("first_name")
    input1.send_keys("Vlad")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Tester")
    input3 = browser.find_element_by_class_name("form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    browser.quit()
