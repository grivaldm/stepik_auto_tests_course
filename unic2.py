from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestAbs(unittest.TestCase):
    def test_blablabla(self):
        welcome_text = ""
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            test1 = browser.find_element(By.XPATH, '//label[text()="First name*"]')
            print(test1.text)
            first_name = browser.find_element(By.CLASS_NAME, "form-control.first")
            first_name.send_keys("name")
            test2 = browser.find_element(By.XPATH, '//label[text()="Last name*"]')
            print(test2.text)
            last_name = browser.find_element(By.CLASS_NAME, "form-control.second")
            last_name.send_keys("last")
            test3 = browser.find_element(By.XPATH, '//label[text()="Email*"]')
            print(test3.text)
            email = browser.find_element(By.CLASS_NAME, "form-control.third")
            email.send_keys("email")
            time.sleep(10)

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            assert "Congratulations! You have successfully registered!" == welcome_text

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "bla bla bla1")


if __name__ == "__main__":
    unittest.main()