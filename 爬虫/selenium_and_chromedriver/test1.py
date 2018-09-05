from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://www.baidu.com')

browser.save_screenshot('baidu.png')

from selenium.webdriver.common.keys import Keys

browser.find_element_by_id('kw').send_keys('美女')
browser.find_element_by_id('su').click()
print(browser.get_cookies())