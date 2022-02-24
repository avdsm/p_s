# 2.3 Задание: переход на новую вкладку
#  https://stepik.org/lesson/184253/step/6?unit=158843

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

def calc(x):
  return math.log(abs(12*math.sin(x)))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    # Можно остановить кнопку с посомщью JS и после нажать
    # browser.execute_script("document.getElementsByTagName('button')[0].classList.remove('trollface');")
    pl_botton = browser.find_element(By.CSS_SELECTOR, 'button.trollface.btn.btn-primary')
    pl_botton.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

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