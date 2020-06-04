import sys, os, time
from selenium import webdriver

rootPath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(rootPath)

driverPath = os.path.abspath(os.path.join(rootPath, "chromedriver.exe"))

driver = webdriver.Chrome(driverPath)

driver.get("http://www.baidu.com")

driver.find_element_by_css_selector("input#kw").send_keys("aaa")

time.sleep(5)

driver.quit()