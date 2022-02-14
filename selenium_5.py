from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select  # Добавляем списки
from selenium.webdriver.common.keys import Keys  #  Добавляем ввод из клавиатуры
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_1 = browser.find_element(By.ID, "num1").text
    x_2 = browser.find_element(By.ID, "num2").text
    suma = int(x_1) + int(x_2)
    print(f'Сумма чисел на странице равно --- {suma}')

    select_s = Select(browser.find_element(By.TAG_NAME, "select"))
    # select_s.select_by_value(f'{suma}')
    select_s.select_by_visible_text(f'{suma}')

    # ####################
    # browser.find_element(By.TAG_NAME, "select").click()
    #  browser.find_element(By.CSS_SELECTOR, "[value={suma}]").click()
    # browser.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()

    button_s = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    button_s.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.close()
    browser.quit()
