# !/usr/bin/python
# encoding: utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
#import asyncio
from time import gmtime, strftime, ctime
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')
chrome_options.add_argument('blink-settings=imagesEnabled=false')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome('/srv/fake-net-account-folder/account/pixuser/samuellu/chromedriver',chrome_options=chrome_options)
driver.get('https://www.pixnet.net')
Login = driver.find_element_by_class_name("pixnavbar__top-bar__login-link").click()
PIX_username = driver.find_element_by_name("email").send_keys("samuellu@pixnet.tw")
PIX_password = driver.find_element_by_name("password").send_keys("12345678")
Login2 = driver.find_element_by_name("password").send_keys(Keys.ENTER)
time.sleep(3)
if driver.title == (u"痞客邦"):
    print("大首頁 活著")
elif driver.title != (u"痞客邦"):
    print("大首頁 掛了")
driver.get('https://streamtopic.pixnet.net/')
time.sleep(3)
if driver.title == (u":: 痞客邦 邦邦 - 你的興趣話題交流圈 ::"):
    print("邦邦 活著")
elif driver.title != (u":: 痞客邦 邦邦 - 你的興趣話題交流圈 ::"):
    print("邦邦 掛了")
driver.get('https://styleme.pixnet.net')
time.sleep(3)
if driver.title == (u"潮流、美妝、消費 創造個人化風格的女性社群 PIXstyleMe"):
    print("styleme 活著")
elif driver.title != (u"潮流、美妝、消費 創造個人化風格的女性社群 PIXstyleMe"):
    print("styleme 掛了")
driver.get('https://www.pixnet.net/blog')
time.sleep(3)
if driver.title == (u"部落格首頁 痞客邦"):
    print("部落格首頁 活著")
elif driver.title != (u"部落格首頁 痞客邦"):
    print("部落格首頁 掛了")
time.sleep(3)
driver.close()
