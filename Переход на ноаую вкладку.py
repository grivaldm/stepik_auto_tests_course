from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import time
import math
from math import sin
from math import log
import pyperclip as pc



def calc(x):
    return math.log(abs(12*sin(x)))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    buttonm = browser.find_element(By.TAG_NAME, "button")
    buttonm.click()


    browser.switch_to.window(browser.window_handles[1])


    x1 = browser.find_element(By.ID, 'input_value')
    print(x1.text)

    y=calc(int(x1.text))
    print(y)

    x2 = browser.find_element(By.ID, 'answer')
    x2.send_keys(y)
    #option1 = browser.find_element(By.ID, 'robotCheckbox')
    #option1.click()
    #option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    #option2.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    pc.copy(browser.switch_to.alert.text.split(': ')[-1])



finally:
    # успеваем скопировать код за 30 секунд

    time.sleep(0.5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
