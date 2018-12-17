import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')
htmlEle = browser.find_element_by_tag_name('html')
while True:
	htmlEle.send_keys(Keys.DOWN)
	time.sleep(0.5)
	htmlEle.send_keys(Keys.RIGHT)
	time.sleep(0.5)
	htmlEle.send_keys(Keys.UP)
	time.sleep(0.5)
	htmlEle.send_keys(Keys.LEFT)
	time.sleep(0.5)
