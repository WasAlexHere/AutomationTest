from selenium import webdriver
import os

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"

browser.get(link)

first_name = browser.find_element_by_css_selector('[placeholder="Enter first name"]')
first_name.send_keys('Alexey')

last_name = browser.find_element_by_css_selector('[placeholder="Enter last name"]')
last_name.send_keys('Malakhov')

email = browser.find_element_by_css_selector('[placeholder="Enter email"]')
email.send_keys('aaaa@aa.aa')

file = browser.find_element_by_id('file')
current_dir = os.path.abspath(os.path.dirname(__file__)) # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'CustomAR.txt')  # добавляем к этому пути имя файла
file.send_keys(file_path)

submit_button = browser.find_element_by_tag_name("button")
submit_button.click()

