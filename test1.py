from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selene.driver import SeleneDriver
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_argument('--headless')

driver = SeleneDriver.wrap(webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options))

driver.get('https://worldofwarships.asia/ja/community/accounts/')
input = driver.find_element_by_name('search')
input.send_keys('b_l_e_n_d_S')
time.sleep(3)
# driver.find_element_by_id('searchBtn').click()  
input.send_keys(Keys.RETURN)
time.sleep(3)

cur_url = driver.current_url
element = driver.find_element_by_xpath('//*[@id="account_page"]/div[3]/div[2]/div/div/div[2]/div/div[2]/table/tbody/tr[3]/td[3]')
print(element.text)
element2 = driver.find_element_by_xpath('//*[@id="account_page"]/div[3]/div[2]/div/div/div[2]/div/div[2]/table/tbody/tr[2]/td[3]')
print(element2.text)
driver.save_screenshot('result.png')

driver.quit()


