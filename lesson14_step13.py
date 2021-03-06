import unittest
from selenium import webdriver
import time

class TestRegistr(unittest.TestCase):
	def test_registration1(self):
		link = "http://suninjuly.github.io/registration1.html"
		browser = webdriver.Chrome()
		browser.get(link)

		input1 = browser.find_element_by_css_selector('div.first_block input.first')
		input1.send_keys("Ivan")

		input2 = browser.find_element_by_css_selector('div.first_block input.second')
		input2.send_keys("Petrov")

		input3 = browser.find_element_by_css_selector('div.first_block input.third')
		input3.send_keys("someEmail")

		button = browser.find_element_by_css_selector("button.btn")
		button.click()

		time.sleep(2)

		welcome_text_elt = browser.find_element_by_tag_name("h1")
		welcome_text = welcome_text_elt.text

		self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "NoSuchElementException")

		time.sleep(3)
		browser.quit()


	def test_registration2(self):
		link = "http://suninjuly.github.io/registration2.html"
		browser = webdriver.Chrome()
		browser.get(link)

		input1 = browser.find_element_by_css_selector('div.first_block input.first')
		input1.send_keys("Ivan")

		input2 = browser.find_element_by_css_selector('div.first_block input.second')
		input2.send_keys("Petrov")

		input3 = browser.find_element_by_css_selector('div.first_block input.third')
		input3.send_keys("someEmail")

		button = browser.find_element_by_css_selector("button.btn")
		button.click()

		time.sleep(2)

		welcome_text_elt = browser.find_element_by_tag_name("h1")
		welcome_text = welcome_text_elt.text

		self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "NoSuchElementException")

		time.sleep(13)
		browser.quit()


if __name__ == "__main__":
	unittest.main()