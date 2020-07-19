from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser.get(link)
    treasure = browser.find_element_by_tag_name('img')
    x = treasure.get_attribute('valuex')
    y = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)

    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()

    radio_button = browser.find_element_by_id('robotsRule')
    radio_button.click()

    submit_button = browser.find_element_by_tag_name('button')
    submit_button.click()

finally:
    time.sleep(30)
    browser.quit()