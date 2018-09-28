from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import time
# driver=webdriver.Chrome()

# url='http://www.baidu.com'
# driver=webdriver.PhantomJS()
# driver.get(url)
# print(driver.title)

url='http://10.0.88.224:82/#/main-page/apply?userId=14a3133c-d336-47e7-97af-916f406630af&token=linus'
driver=webdriver.Chrome()
driver.get(url)
time.sleep(3) #经常会因为等待的问题报错要进行判断 await等
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/section/div/div[1]/div/div/div[1]/div[2]/button/span').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/section/div/div[2]/div[3]/table/tbody/tr[7]/td[7]/div/button/span').click()
time.sleep(100)