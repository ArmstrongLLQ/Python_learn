
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
# 设置为无界面模式
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')

try:
	browser = webdriver.Chrome()
	browser.get('https://www.baidu.com')
	input = browser.find_element_by_id('kw')
	input.send_keys('Python')
	input.send_keys(Keys.ENTER)
	wait = WebDriverWait(browser, 10)
	wait.until(EC.presence_of_all_elements_located((By.ID, 'content_left')))
	# print(browser.current_url)
	# print(browser.get_cookies())
	# print(browser.page_source)
	with open('test.html', 'w', encoding='utf-8') as f:
		f.write(browser.page_source)

finally:
	browser.close()


