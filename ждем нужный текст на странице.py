from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
from math import sin
from math import log
import pyperclip as pc

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    price = browser.find_element(By.XPATH, '//*[@id="price"]')
    price1 = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="price"]'), "$100"))
    #assert "$100" in price.text
    print(price.text)

    button = browser.find_element(By.XPATH, '//*[@id="book"]')

    button.click()
    #print(button.text)
    time.sleep(1)
    x1 = browser.find_element(By.XPATH, '//*[@id="input_value"]')

    print(x1.text)

    y=calc(int(x1.text))
    print(y)

    x2 = browser.find_element(By.ID, 'answer')
    x2.send_keys(y)
    button1 = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "solve")))
    button1.click()
    #print(button1.text)



finally:
    # успеваем скопировать код за 30 секунд

    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
