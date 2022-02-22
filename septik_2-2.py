# 2.2 Работа с файлами, списками и js-скриптами
#  https://stepik.org/lesson/228249/step/8?unit=200781

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    f_name = browser.find_element(By.NAME, 'firstname')
    f_name.send_keys("Arni")

    l_name = browser.find_element(By.NAME, 'lastname')
    l_name.send_keys('Vasilin')

    email = browser.find_element(By.NAME, 'email')
    email.send_keys('kashmar@mail.ru')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, '1.txt')
    f_id = browser.find_element(By.ID, 'file')
    f_id.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button.btn.btn-primary")
    button.click()

finally:
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.close()
    browser.quit()