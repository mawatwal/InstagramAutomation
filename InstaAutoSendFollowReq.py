# import necessary libraries
from selenium import webdriver
import time
# enter the file path of chromedriver
browser = webdriver.Chrome("C:/Users/mawat/Desktop/Downloads/project/chromedriver.exe")
# to maximise the window
browser.maximize_window()
# enter the url of the website, username, password, and the username of the person to be followed
url="https://www.instagram.com/"
username="enter your username"
password="enter your password"
find="mawatwalmanish"
# open the url of the website
browser.get(url)
time.sleep(3)
# locate the username field and pass the username
a=browser.find_element_by_css_selector("#react-root > section > main > article > div.rgFsT > div:nth-child(1) > div > form > div:nth-child(2) > div > label > input")
a.send_keys(username)
# locate the password field and pass the password
b=browser.find_element_by_css_selector("#react-root > section > main > article > div.rgFsT > div:nth-child(1) > div > form > div:nth-child(3) > div > label > input")
b.send_keys(password)
# locate the log in button and click enter
browser.find_element_by_css_selector("#react-root > section > main > article > div.rgFsT > div:nth-child(1) > div > form > div:nth-child(4) > button > div").click()
time.sleep(5)
# locate Not Now in Turn on Notifications popup in case you haven't specified it already in your account, it is by default, uncomment the next two lines if you have any error
browser.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm").click()
time.sleep(3)
# locate the explore button and click
browser.find_element_by_css_selector("#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg > div > div:nth-child(2) > a > svg").click()
time.sleep(5)
# locate the search bar, pass the name of the instagram account to be followed and click 
c=browser.find_element_by_css_selector("#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > input")
c.send_keys(find)
time.sleep(8)
browser.find_element_by_class_name("z556c").click()
time.sleep(5)
# locate the follow button and click
browser.find_element_by_xpath("//*[text()='Follow']").click()
time.sleep(10)
