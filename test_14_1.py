from selenium import webdriver
import time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/wait1.html"

browser.implicitly_wait(5) # говорим WebDriver искать каждый элемент в течение 5 секунд

browser.get(link)

#time.sleep(2) # пауза на 5 секунд

button = browser.find_element_by_id("verify")
button.click()

message = browser.find_element_by_id("verify_message")

assert "successful" in message.text
