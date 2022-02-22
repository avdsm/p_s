# 2.2 Работа с файлами, списками и js-скриптами
#  https://stepik.org/lesson/228249/step/6?auth=login&unit=200781
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

def calc(x):
  return math.log(abs(12*math.sin(x)))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)

    x_text = browser.find_element(By.ID, "input_value").text
    x = int(x_text)
    y = calc(x)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    answer = browser.find_element(By.CSS_SELECTOR, "input#answer")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(y)

    cb_robot = browser.find_element(By.ID, "robotCheckbox")
    cb_robot.click()

    radio_rule = browser.find_element(By.CSS_SELECTOR, "label[for='robotsRule']")
    radio_rule.click()

    button.click()

finally:
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.close()
    browser.quit()

