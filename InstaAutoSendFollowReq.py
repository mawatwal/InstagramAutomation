from selenium import webdriver
import time
browser = webdriver.Chrome("C:/Users/mawat/Desktop/Downloads/project/chromedriver.exe")
browser.maximize_window()
url="https://www.instagram.com/"
username="mawatwalmanish@yahoo.com"
password="qdchptj376h9i9Q"
find="faraz_bangalore"
browser.get(url)
time.sleep(3)
a=browser.find_element_by_css_selector("#react-root > section > main > article > div.rgFsT > div:nth-child(1) > div > form > div:nth-child(2) > div > label > input")
a.send_keys(username)
b=browser.find_element_by_css_selector("#react-root > section > main > article > div.rgFsT > div:nth-child(1) > div > form > div:nth-child(3) > div > label > input")
b.send_keys(password)
browser.find_element_by_css_selector("#react-root > section > main > article > div.rgFsT > div:nth-child(1) > div > form > div:nth-child(4) > button > div").click()
time.sleep(5)
browser.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm").click()
time.sleep(3)
browser.find_element_by_css_selector("#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg > div > div:nth-child(2) > a > svg").click()
time.sleep(5)
c=browser.find_element_by_css_selector("#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > input")
c.send_keys(find)
time.sleep(8)
browser.find_element_by_class_name("z556c").click()
time.sleep(5)
browser.find_element_by_xpath("//*[text()='Follow']").click()
time.sleep(10)