from selenium import webdriver
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/cats.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    submitBtn = browser.find_element_by_id("button")
    submitBtn.click()


finally:
    time.sleep(5)
    browser.quit()