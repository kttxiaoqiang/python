import time
from selenium import webdriver
# 进入浏览器设置
options = webdriver.ChromeOptions()
# 设置中文
options.add_argument('lang=zh_CN.UTF-8')
# 更换头部
options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')

url='http://www.geetest.com/exp.html'
driver=webdriver.Chrome()
driver.get(url)
driver.maximize_window()
time.sleep(3)
driver.execute_script('window.scrollTo(0,500)')

driver.find_element_by_xpath('//span[contains(text(),"点击按钮进行验证")]').click()
time.sleep(500)
driver.quit()
# driver.find_element_by_xpath('//*[@id="G1"]/div/div[2]/div[2]/div/div[4]/input').click()


