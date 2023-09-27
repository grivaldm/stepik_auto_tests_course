from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    valuex = browser.find_element(By.XPATH, "//*[@id='treasure']")
    xx = valuex.get_attribute("valuex")
    print("valuex: ", xx)
    #print(valuex.text)

    y=calc(int(xx))
    print(y)

    x2 = browser.find_element(By.ID, 'answer')
    x2.send_keys(y)
    option1 = browser.find_element(By.ID, 'robotCheckbox')
    option1.click()
    option2 = browser.find_element(By.XPATH, "//*[@id='robotsRule']")
    option2.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
