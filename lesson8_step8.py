from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	input1 = browser.find_element_by_name('firstname')
	input1.send_keys("Anton")

	input2 = browser.find_element_by_name('lastname')
	input2.send_keys("Petrov")

	input3 = browser.find_element_by_name('email')
	input3.send_keys("someemail")

	current_dir = os.path.abspath(os.path.dirname(__file__))
	file_path = os.path.join(current_dir, 'Katyusha.txt')
	element = browser.find_element_by_css_selector("[type='file']")
	element.send_keys(file_path)

	button = browser.find_element_by_css_selector("button.btn")
	button.click()

finally:
	time.sleep(13)
	browser.quit()