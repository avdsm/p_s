from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    nkar_x = browser.find_element(By.CSS_SELECTOR, "img#treasure")

    x_text = nkar_x.get_attribute("valuex")
    x = int(x_text)
    y = calc(x)

    answer_text = browser.find_element(By.CSS_SELECTOR, "#answer")
    #answer_text.clear()
    answer_text.send_keys(y)

    cb_robot = browser.find_element(By.ID, "robotCheckbox")
    cb_robot.click()

    radio_rule = browser.find_element(By.CSS_SELECTOR, "#robotsRule[value='robots']")
    #radio_rule = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio_rule.click()

    button_s = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    button_s.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.close()
    browser.quit()
