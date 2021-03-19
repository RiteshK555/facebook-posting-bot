import time
from selenium import webdriver
from instapy_cli import client
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import credentials
browser1 = webdriver.Chrome()
browser1.get('https://www.facebook.com')
browser1.find_element_by_id("email").send_keys(credentials.username)
browser1.find_element_by_id("pass").send_keys(credentials.password)
browser1.find_element_by_name("login").click()
time.sleep(7)
browser1.find_element_by_xpath('/html/body/div[10]/div[1]/div/div[2]').click()
browser1.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/div[3]/span/div/i').click()
time.sleep(1)
browser1.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div[2]/div[1]/div/div[1]/div[1]/div/i').click()
time.sleep(2)
browser1.find_element_by_xpath('/html/body/div[10]/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[3]/div[1]/div[2]/div/div[1]/input').send_keys('/home/username/Desktop/otherproj/weekend.jpg')
time.sleep(2)
browser1.find_element_by_xpath('/html/body/div[10]/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[3]/div[2]/div/div/span/div/span/span').click()
# browser2 = webdriver.Chrome()
# browser2.get('https://www.instagram.com/accounts/login/')
# time.sleep(1)
# browser2.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input').send_keys("riteshkatukojwala@gmail.com")
# time.sleep(1)
# browser2.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input').send_keys("R!7995832372")
# browser2.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button/div').click()
# time.sleep(3)
# browser2.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
# time.sleep(1)
# browser2.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()