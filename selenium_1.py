from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://ruzan.ru/woman/women-s-purse-michael-kors-blue")

color_btn = driver.find_element(By.CSS_SELECTOR, "label img.img-thumbnail")
color_btn.click()

text_elem = driver.find_element(By.NAME, "quantity")
text_elem.clear()
text_elem.send_keys("22")

btn_add = driver.find_element(By.CSS_SELECTOR, "a#button-cart")
btn_add.click()

btn_qooci = driver.find_element(By.ID, "oct-policy-btn")
btn_qooci.click()

# driver.implicitly_wait(3)
AAA = driver.find_element(By.CSS_SELECTOR, "button#cls.testbutton")
AAA.click()

cart_btn = driver.find_element(By.ID, "cart")
cart_btn.click()

BBB = driver.find_element(By.LINK_TEXT, "Открыть корзину")
BBB.click()

assert "Кошелек женский Michael Kors синий" in driver.page_source
print("OK")

time.sleep(5)


driver.close()
driver.quit()
