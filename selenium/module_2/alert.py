import time, math

from selenium import webdriver

link = "http://suninjuly.github.io/alert_accept.html"

with webdriver.Chrome() as browser:
    browser.get(link)

    # Нажать на кнопку и подтвердить alert
    browser.find_element_by_tag_name("button").click()
    browser.switch_to.alert.accept()
    time.sleep(1)

    # Получить значение переменной и подставить в формулу
    x = browser.find_element_by_id("input_value").text
    answer = math.log(abs(12 * math.sin(float(x))))

    # Ответ поместить в input и нажать на кнопку
    browser.find_element_by_id("answer").send_keys(str(answer))
    browser.find_element_by_tag_name("button").click()

    # Считать содержимое alert
    alert = browser.switch_to.alert.text
    result = alert.split(': ')[-1]
    print(result)

    time.sleep(10)
    browser.quit()
