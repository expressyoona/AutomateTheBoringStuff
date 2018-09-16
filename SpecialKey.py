from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#import sleep
browser = webdriver.Firefox()
browser.get('https://news.zing.vn/')
htmlEle = browser.find_element_by_tag_name('html')
print(htmlEle)
while True:
    htmlEle.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
#htmlEle.send_keys(Keys.HOME)
print('Done')
