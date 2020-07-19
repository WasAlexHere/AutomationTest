from selenium import webdriver
import math

browser = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser.get(link)
x = browser.find_element_by_id('input_value')
x_value = x.text

y = calc(int(x_value))

browser.execute_script("window.scrollBy(0, 100);")

answer = browser.find_element_by_id('answer')
answer.send_keys(y)

checkbox = browser.find_element_by_id('robotCheckbox')
checkbox.click()

radio_button = browser.find_element_by_id('robotsRule')
radio_button.click()

submit_button = browser.find_element_by_tag_name("button")
submit_button.click()