from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')
linkEle = browser.find_element_by_link_text('Read Online for Free')
linkEle.click()
