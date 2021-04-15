import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(num):
    return math.log(abs(12 * math.sin(float(num))))


with webdriver.Chrome() as browser:
    browser.get(link)
    browser.implicitly_wait(5)

    # Ожидать, когда цена будет равна 100$
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    browser.find_element_by_id("book").click()

    x = browser.find_element_by_id("input_value").text
    answer = str(calc(x))
    browser.find_element_by_id("answer").send_keys(answer)
    browser.find_element_by_id("solve").click()

    # Содержимое alert
    alert = browser.switch_to.alert.text
    result = alert.split(': ')[-1]
    print(result)

    browser.quit()
