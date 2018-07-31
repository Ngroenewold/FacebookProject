from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get("https://www.youtube.com/watch?v=Qn7OuGW9KEU")
elm = browser.find_element_by_tag_name('html')
time.sleep(3)
#while(Keys.END):
while(Keys.END):
    elm.send_keys(Keys.END)



time.sleep(2)
comment_div= browser.find_element_by_xpath('//*[@id="contents"]')
comments=comment_div.find_elements_by_xpath('//*[@id="content-text"]')
for comment in comments:
    print(comment.text)



