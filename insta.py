from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import sys
import json

browser = webdriver.Chrome("./chromedriver")
browser.implicitly_wait(5)

browser.get('https://www.instagram.com/')


username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")


username_input.send_keys("<Username>")
password_input.send_keys('<password>')

login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()

sleep(3)

getsearch = sys.argv[1]

browser.get("https://instagram.com/"+getsearch+"?__a=1")

x = browser.execute_script("return document.body.innerText;")
y = json.loads(x)
browser.get(y["graphql"]["user"]["profile_pic_url_hd"])


sleep(6)
#browser.close()


