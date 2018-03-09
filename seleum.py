# coding=utf-8
from selenium import webdriver

driver=webdriver.Chrome()
driver.get('https://mail.qq.com/')

driver.switch_to_frame('login_frame')
driver.find_element_by_id('u').send_keys('2680465171')
driver.find_element_by_id('p').send_keys('1054921935..')
driver.find_element_by_id('login_button')

# ret=driver.find_elements_by_xpath('//pre/a')
# for i in ret:
#     rets=i.get_attribute('href')
#     print(rets)

driver.quit()