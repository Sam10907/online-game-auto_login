from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep

driver=webdriver.Ie()
driver.get('https://tw.beanfun.com/kartrider/main.aspx')
driver.execute_script('$("#Image23").click();')
account='ACCOUNT'
password='PASSWORD'
sleep(10)
driver.switch_to_frame("ifmForm1")
driver.find_element_by_xpath('//*[@id="t_AccountID"]').send_keys(account)
driver.find_element_by_xpath('//*[@id="t_Password"]').send_keys(password)
driver.execute_script('$("#btn_login").click()')
sleep(7)
driver.switch_to_frame("fbContent")
driver.execute_script('$("#ulServiceAccountList").children().first().click()')
