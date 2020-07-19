from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()

def calc(x,y):
  return x + y

try:
    browser.get(link)
    x = browser.find_element_by_id('num1')
    x_value = int(x.text)
    y = browser.find_element_by_id('num2')
    y_value = int(y.text)

    result = str(calc(x_value, y_value))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(result)

    submit_button = browser.find_element_by_tag_name('button')
    submit_button.click()
finally:
    time.sleep(30)
    browser.quit()
