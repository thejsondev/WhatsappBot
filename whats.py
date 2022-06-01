
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import datetime

def xpathIsExist(xpath):
    try:
        xpath = ''
        driver.find_element_by_xpath(xpath)
    except:
        return False
    return True
options = Options()
options.add_argument("user-data-dir=/tmp/tarun")
driver = webdriver.Chrome('/usr/bin/chromedriver' , chrome_options=options)

driver.get('https://web.whatsapp.com/')
while True:
    try:
        allMessages = driver.find_element_by_xpath('//*[@class="_1pJ9J"]/span').click()
        message = driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div[2]/div[3]/div[last()]/div/div[1]/div[1]/div[1]/div/span[1]/span').text
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys(message,Keys.RETURN)
        driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/div/div').click()
        driver.find_element_by_xpath('//*[@id="app"]/div/span[4]/div/ul/div/div/li[3]').click()
        sleep(1)
    except:
        pass