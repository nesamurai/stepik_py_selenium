from selenium import webdriver
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    chest = browser.find_element_by_id('treasure')
    hiddenX = chest.get_attribute('valuex')

    y = calc(hiddenX)

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