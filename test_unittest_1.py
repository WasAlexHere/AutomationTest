import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):

    browser = webdriver.Chrome()

    def test_login1(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = self.browser.find_element_by_css_selector(".first:required")
        input1.send_keys("Ivan")
        input2 = self.browser.find_element_by_css_selector(".second:required")
        input2.send_keys("Petrov")
        input3 = self.browser.find_element_by_css_selector(".third:required")
        input3.send_keys("Petrov")

        # Отправляем заполненную форму
        button = self.browser.find_element_by_tag_name("button")
        button.click()

        # находим элемент, содержащий текст
        welcome_text_elt = self.browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Text is incorrect!")
        #self.browser.quit()


    def test_login2(self):

        link1 = "http://suninjuly.github.io/registration2.html"
        self.browser.get(link1)

        # Ваш код, который заполняет обязательные поля
        input1 = self.browser.find_element_by_css_selector(".first:required")
        input1.send_keys("Ivan")
        input2 = self.browser.find_element_by_css_selector(".second:required")
        input2.send_keys("Petrov")
        input3 = self.browser.find_element_by_css_selector(".third:required")
        input3.send_keys("Petrov")

        # Отправляем заполненную форму
        button = self.browser.find_element_by_tag_name("button")
        button.click()

        # находим элемент, содержащий текст
        welcome_text_elt = self.browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Text is incorrect!")
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()