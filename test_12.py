from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser.get(link)

    click_button = browser.find_element_by_tag_name("button")
    click_button.click()

    alert = browser.switch_to.alert
    alert.accept()

    x = browser.find_element_by_id('input_value')
    x_value = x.text

    y = calc(int(x_value))

    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)

    submit_button = browser.find_element_by_tag_name("button")
    submit_button.click()

finally:
    time.sleep(30)
    browser.quit()

