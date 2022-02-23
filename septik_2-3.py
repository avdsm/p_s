# 2.3 Работа с окнами
#  https://stepik.org/lesson/184253/step/4?unit=158843

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

def calc(x):
  return math.log(abs(12*math.sin(x)))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    st_button = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
    st_button.click()

    alert = browser.switch_to.alert
    alert.accept()

    # time.sleep(1)
    browser.implicitly_wait(5)
    x_text = browser.find_element(By.ID, "input_value").text
    x = int(x_text)
    y = calc(x)

    answer = browser.find_element(By.CSS_SELECTOR, "input#answer")
    answer.send_keys(y)

    sb_button = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
    sb_button.click()

finally:
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.close()
    browser.quit()