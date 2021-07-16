from selenium import webdriver
import time

try:
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/huge_form.html")
	elements = browser.find_elements_by_xpath("//input[@type='text']")
	for elem in elements:
		elem.send_keys('m')

	button = browser.find_element_by_css_selector("button.btn")
	button.click()

finally:
	time.sleep(10)
	browser.quit()