from selenium import webdriver
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    input_field = browser.find_element_by_id('answer')
    input_field.send_keys(y)

    chb = browser.find_element_by_id('robotCheckbox')
    chb.click()

    radioBtn = browser.find_element_by_id('robotsRule')
    radioBtn.click()

    submitBtn = browser.find_element_by_css_selector("button[type='submit']")
    submitBtn.click()

finally:
    time.sleep(15)
    browser.quit()