from selenium import webdriver
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    submitBtn = browser.find_element_by_css_selector("button[type='submit']")
    submitBtn.click()

    handle = browser.window_handles[1]
    browser.switch_to_window(handle)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    input_field = browser.find_element_by_id('answer')
    input_field.send_keys(y)

    secondsubmitBtn = browser.find_element_by_css_selector("button[type='submit']")
    secondsubmitBtn.click()

finally:
    time.sleep(15)
    browser.quit()