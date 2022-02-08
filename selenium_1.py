from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://ruzan.ru/woman/women-s-purse-michael-kors-blue")

color_btn = driver.find_element(By.CSS_SELECTOR, "label img.img-thumbnail")
color_btn.click()

text_elem = driver.find_element_by_name("quantity")
text_elem.clear()
text_elem.send_keys("22")

btn_add = driver.find_element_by_css_selector("a#button-cart")
btn_add.click()

driver.implicitly_wait(5)
AAA = driver.find_element_by_css_selector("button#cls")
AAA.click()

cart_btn = driver.find_element_by_id("cart")
cart_btn.click()

BBB = driver.find_element_by_link_text("Открыть корзину")
BBB.click()

assert "Кошелек женский Michael Kors синий" in driver.page_source
print("OK")

time.sleep(5)


driver.close()
driver.quit()
