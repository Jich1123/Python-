from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
url = "http://www.baidu.com"
driver.get(url)

text = driver.find_element_by_id('wrapper').text
print(text)
print(driver.title)

driver.save_screenshot('index.png')
driver.find_element_by_id('kw').send_keys(u"大熊猫")

driver.find_element_by_id('su').click()
time.sleep(5)
driver.save_screenshot('daxiongmao.png')

print(driver.get_cookies())

driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'x')

driver.find_element_by_id('kw').send_keys(u"航空母舰")
driver.save_screenshot('hangmu.png')
driver.find_element_by_id('su').send_keys(Keys.RETURN)
time.sleep(5)
driver.save_screenshot('hangmu2.png')

driver.find_element_by_id('kw').clear()
driver.save_screenshot('clear.png')

driver.quit()