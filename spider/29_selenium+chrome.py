from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# driver=webdriver.PhantomJS()
driver=webdriver.Chrome()
url='http://www.baidu.com'
driver.get(url)
text=driver.find_element_by_id('wrapper').text
# print(text)

driver.find_element_by_id('kw').send_keys('小熊猫')
driver.find_element_by_id('su').click()
time.sleep(3)
driver.save_screenshot('1.png')
# for i in driver.get_cookies():
#     print(i)
driver.find_element_by_id('kw').send_keys(Keys.LEFT_CONTROL,'a')
driver.find_element_by_id('kw').send_keys(Keys.LEFT_CONTROL,'x')
driver.find_element_by_id('kw').send_keys('航空母舰')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="su"]').click()
driver.find_element_by_id('kw').clear()
time.sleep(3)
driver.save_screenshot('1.png')
driver.quit()
