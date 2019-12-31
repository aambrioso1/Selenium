import time
from selenium import webdriver
browser = webdriver.Chrome()

from selenium.webdriver.common.keys import Keys

browser.get('http://nostarch.com')
htmlElem = browser.find_element_by_tag_name('html')
for i in range(3):
    time.sleep(1)
    htmlElem.send_keys(Keys.END)
    time.sleep(1)
    htmlElem.send_keys(Keys.HOME)
browser.get('http://google.com')
time.sleep(1)
browser.back()
time.sleep(1)
browser.forward()
time.sleep(1)
browser.back()