import time, math

from selenium import webdriver

link = "http://suninjuly.github.io/redirect_accept.html"


def calc(num):
    return math.log(abs(12 * math.sin(float(num))))


with webdriver.Chrome() as browser:
    browser.get(link)

    browser.find_element_by_tag_name("button").click()
    time.sleep(1)

    # Получить имя новой закладки
    new_window = browser.window_handles[1]
    # Перейти на новую закладку
    browser.switch_to.window(new_window)
    time.sleep(1)

    x = browser.find_element_by_id("input_value").text
    answer = str(calc(x))
    browser.find_element_by_id("answer").send_keys(answer)
    browser.find_element_by_tag_name("button").click()

    # Получить содержимое alert
    alert = browser.switch_to.alert.text
    result = alert.split(': ')[-1]
    print(result)

    time.sleep(10)
    browser.quit()
