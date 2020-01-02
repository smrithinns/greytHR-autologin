#Author: Smrithin N S
#Date: 02 Jan 2019
#Version:v1
#Requirement: Selenium and geckodriver/chromedriver in $PATH 

from selenium import webdriver 
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time 
options = FirefoxOptions()
options.add_argument("--headless")
browser = webdriver.Firefox(options=options)
print ("Headless Firefox Initialized")

#browser = webdriver.Chrome()


browser.get('https://domain.greythr.com') 
time.sleep(3) 

# Enter your user name and password here. 
username = "<username>"
password = "<password>"

# username send 
a = browser.find_element_by_xpath("//input[@id='username']")
a.send_keys(username) 

# password send 
b = browser.find_element_by_xpath("//input[@id='password']")
b.send_keys(password) 

#Click Login
c = browser.find_element_by_xpath("//button[@type='submit']")
c.click()
time.sleep(5) 

#Click Attendance tab
d = browser.find_element_by_xpath("//*[@class='icon-gt-leave-calendar']")
d.click()
time.sleep(7)

#Click Sign In/Out
#e= browser.find_element_by_xpath("//button[@class='btn btn-large btn-success signOut']")
e= browser.find_element_by_xpath("//button[@class='btn btn-large btn-success signIn']")
e.click()

#Exit browser
browser.close()


