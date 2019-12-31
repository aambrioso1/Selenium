from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('http://google.com')

"""
linkElem = browser.find_elements_by_name('btnK')
button = linkElem[1]
# button = browser.find_element_by_id('6146a529-3ed8-4ef4-adfe-f165352f6fc6')
print(linkElem)
button.send_keys('Alan Turing')
# button.click()
"""


elem = driver.find_element_by_name("q")
print(elem)
elem.clear()
elem.send_keys("Alan Turing")
elem.send_keys(Keys.RETURN)
# time.sleep(3)
