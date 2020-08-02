import pytest
import time
import math
from selenium import webdriver

class TestMainPage():

    def test_enter_correct_answer_1(self):
        answer = math.log(int(time.time()))

        browser = webdriver.Chrome()
        link = "https://stepik.org/lesson/236895/step/1"
        browser.get(link)

        time.sleep(10)
        input1 = browser.find
        input1 = browser.find_element_by_tag_name("textarea")
        input1.send_keys(str(answer))

        button = browser.find_element_by_class_name("submit-submission")
        button.click()

        time.sleep(5)

        verify_answer = browser.find_element_by_class_name("smart-hints__hint")
        final_answer = verify_answer.text

        assert final_answer == "Correct!","Incorrect answer!"
        #browser.quit()

    def test_enter_correct_answer_2(self):
        answer = math.log(int(time.time()))

        browser = webdriver.Chrome()
        link = "https://stepik.org/lesson/236896/step/1"
        browser.get(link)

        time.sleep(5)

        input1 = browser.find_element_by_tag_name("textarea")
        input1.send_keys(str(answer))

        button = browser.find_element_by_class_name("submit-submission")
        button.click()

        time.sleep(5)

        verify_answer = browser.find_element_by_class_name("smart-hints__hint")
        final_answer = verify_answer.text

        assert final_answer == "Correct!","Incorrect answer!"
        #browser.quit()

    def test_enter_correct_answer_3(self):
        answer = math.log(int(time.time()))

        browser = webdriver.Chrome()
        link = "https://stepik.org/lesson/236897/step/1"
        browser.get(link)

        time.sleep(10)

        input1 = browser.find_element_by_tag_name("textarea")
        input1.send_keys(str(answer))

        button = browser.find_element_by_class_name("submit-submission")
        button.click()

        time.sleep(5)

        verify_answer = browser.find_element_by_class_name("smart-hints__hint")
        final_answer = verify_answer.text

        assert final_answer == "Correct!","Incorrect answer!"
        #browser.quit()

    def test_enter_correct_answer_4(self):
        answer = math.log(int(time.time()))

        browser = webdriver.Chrome()
        link = "https://stepik.org/lesson/236898/step/1"
        browser.get(link)

        time.sleep(10)

        input1 = browser.find_element_by_tag_name("textarea")
        input1.send_keys(str(answer))

        button = browser.find_element_by_class_name("submit-submission")
        button.click()

        time.sleep(5)

        verify_answer = browser.find_element_by_class_name("smart-hints__hint")
        final_answer = verify_answer.text

        assert final_answer == "Correct!","Incorrect answer!"
        #browser.quit()

    def test_enter_correct_answer_5(self):
        answer = math.log(int(time.time()))

        browser = webdriver.Chrome()
        link = "https://stepik.org/lesson/236899/step/1"
        browser.get(link)

        time.sleep(10)

        input1 = browser.find_element_by_tag_name("textarea")
        input1.send_keys(str(answer))

        button = browser.find_element_by_class_name("submit-submission")
        button.click()

        time.sleep(5)

        verify_answer = browser.find_element_by_class_name("smart-hints__hint")
        final_answer = verify_answer.text

        assert final_answer == "Correct!","Incorrect answer!"
        #browser.quit()

    def test_enter_correct_answer_6(self):
        answer = math.log(int(time.time()))

        browser = webdriver.Chrome()
        link = "https://stepik.org/lesson/236903/step/1"
        browser.get(link)

        time.sleep(10)

        input1 = browser.find_element_by_tag_name("textarea")
        input1.send_keys(str(answer))

        button = browser.find_element_by_class_name("submit-submission")
        button.click()

        time.sleep(5)

        verify_answer = browser.find_element_by_class_name("smart-hints__hint")
        final_answer = verify_answer.text

        assert final_answer == "Correct!","Incorrect answer!"
        #browser.quit()

    def test_enter_correct_answer_7(self):
        answer = math.log(int(time.time()))

        browser = webdriver.Chrome()
        link = "https://stepik.org/lesson/236904/step/1"
        browser.get(link)

        time.sleep(10)

        input1 = browser.find_element_by_tag_name("textarea")
        input1.send_keys(str(answer))

        button = browser.find_element_by_class_name("submit-submission")
        button.click()

        time.sleep(5)

        verify_answer = browser.find_element_by_class_name("smart-hints__hint")
        final_answer = verify_answer.text

        assert final_answer == "Correct!","Incorrect answer!"
        #browser.quit()

    def test_enter_correct_answer_8(self):
        answer = math.log(int(time.time()))

        browser = webdriver.Chrome()
        link = "https://stepik.org/lesson/236905/step/1"
        browser.get(link)

        time.sleep(10)

        input1 = browser.find_element_by_tag_name("textarea")
        input1.send_keys(str(answer))

        button = browser.find_element_by_class_name("submit-submission")
        button.click()

        time.sleep(5)

        verify_answer = browser.find_element_by_class_name("smart-hints__hint")
        final_answer = verify_answer.text

        assert final_answer == "Correct!","Incorrect answer!"
        #browser.quit()