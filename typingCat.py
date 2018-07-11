# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 14:36:33 2018

@author: 11scw
"""
#some random shit somewhere that doesn't affect your code
from selenium import webdriver as driver
import time as T
from selenium.webdriver.common.keys import Keys


chromedriver_path = r"chromedriver.exe"
chrome_browser = driver.Chrome(executable_path=chromedriver_path)
chrome_browser.get("http://thetypingcat.com/typing-speed-test/1m")

#current_char = chrome_browser.find_element_by_css_selector(".char.active").get_attribute("data-char")
#print(current_char)

active_element = chrome_browser.switch_to_active_element()
print(active_element.__dir__)

#char_element = chrome_browser.find_element_by_css_selector(".char.active")
#current_char = char_element.get_attribute("data-char")
#active_element.send_keys(current_char)
        
#for i in range(1,999):
#    try:
#        char_element = chrome_browser.find_element_by_css_selector(".char.active")
#        current_char = char_element.get_attribute("data-char")
#        if current_char == '⏎':
#            active_element.send_keys(Keys.ENTER)
#        else:
#            active_element.send_keys(current_char)
#        T.sleep(0.02)
#        
#    except:
#        print (Exception)
#        break
    
while True:
    try:
        char_element = chrome_browser.find_element_by_css_selector(".char.active")
        current_char = char_element.get_attribute("data-char")
        if current_char == '⏎':
            active_element.send_keys(Keys.ENTER)
        else:
            active_element.send_keys(current_char)
        T.sleep(0.015)        
    except:
        print (Exception.__str__)
        print ("End of typing")
        break
