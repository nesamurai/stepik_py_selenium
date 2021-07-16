import pytest
from selenium import webdriver
import time
import math



@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    return browser

@pytest.mark.parametrize('link', [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
])
def test_task(browser, link):
	url = link
	answer = math.log(int(time.time()))
	browser.implicitly_wait(5)
	browser.get(url)

	answer_form = browser.find_element_by_tag_name('textarea')

	answer_form.send_keys(str(answer))

	send_btn = browser.find_element_by_class_name('submit-submission')

	send_btn.click()

	time.sleep(4)

	hint = browser.find_element_by_class_name('smart-hints__hint')
	hint_text = hint.text
	print(hint_text)

	assert hint_text == "Correct!", "test failed, you can find a part for answer"

	browser.quit()