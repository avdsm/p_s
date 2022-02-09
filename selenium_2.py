from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element(By.CSS_SELECTOR, "input.form-control.first")
    first_name.clear()
    first_name.send_keys('UserName')

    first_name_second = browser.find_element(By.CSS_SELECTOR, "input.form-control.second")
    first_name_second.clear()
    first_name_second.send_keys('UserNameSecond')

    email_name = browser.find_element(By.CSS_SELECTOR, "input.form-control.third")
    email_name.clear()
    email_name.send_keys('UserNameSecond@mail.ru')

    # Отправляем заполненную форму
    time.sleep(3)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    #browser.implicitly_wait(3)
    #time.sleep(3)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.CSS_SELECTOR, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    browser.close()
    browser.quit()
