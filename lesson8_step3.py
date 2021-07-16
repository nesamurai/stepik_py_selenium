from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_num = browser.find_element_by_id('num1')
    num1 = first_num.text

    second_num = browser.find_element_by_id('num2')
    num2 = second_num.text

    total = int(num1) + int(num2)

    select = Select(browser.find_element_by_id('dropdown'))
    select.select_by_visible_text(str(total))

    submitBtn = browser.find_element_by_css_selector("button[type='submit']")
    submitBtn.click()

finally:
    time.sleep(15)
    browser.quit()