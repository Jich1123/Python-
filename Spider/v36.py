from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.PhantomJS()
driver.get("http://www.baidu.com")
print("Ttile:{0}".format(driver.title))