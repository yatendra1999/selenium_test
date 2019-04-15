from os import path
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
import time
opts = Options()
browser = Firefox(options=opts)
browser.get('https://imgur.com/upload')
pic = browser.find_element_by_id('global-files-button')
pic.send_keys(path.dirname(path.abspath(__file__))+'/upload.png')
time.sleep(4)
pic_url = browser.current_url
print('pic URL: ',pic_url)
browser.get('https://paste.debian.net/')
name = browser.find_element_by_id('poster')
name.send_keys('TEst NAme')
security = browser.find_element_by_id('private')
if not security.is_selected():
    # print(security.is_selected())
    security.click()
code = browser.find_element_by_id('code')
code.send_keys('Post: \n \n image has been uploaded at : ', pic_url)
# fileee = browser.find_element_by_name('upload')
# fileee.send_keys('/home/mml/test/upload.png')
submit = browser.find_element_by_name('paste')
submit.submit()
# print(browser.title)
time.sleep(4)
url = browser.current_url
print('Post URL: ',url)
browser.close()