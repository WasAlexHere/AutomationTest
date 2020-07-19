from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    x_value = browser.find_element_by_id('input_value')
    x = x_value.text
    y = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)

    checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']")
    checkbox.click()

    radio_button = browser.find_element_by_css_selector("[for='robotsRule']")
    radio_button.click()

    submit_button = browser.find_element_by_tag_name('button')
    submit_button.click()

finally:
    time.sleep(30)
    browser.quit()