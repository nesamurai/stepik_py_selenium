from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    booking = WebDriverWait(browser, 15).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )

    nowBook = browser.find_element_by_id('book')
    nowBook.click()

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    input_field = browser.find_element_by_id('answer')
    input_field.send_keys(y)

    secondsubmitBtn = browser.find_element_by_css_selector("button[type='submit']")
    secondsubmitBtn.click()


finally:
    time.sleep(25)
    browser.quit()