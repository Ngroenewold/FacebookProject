from bs4 import BeautifulSoup
import requests
from selenium import webdriver

import time

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/watch?v=66y-llDYxIs")
driver.execute_script('window.scrollTo(1,50000);')
print("Before Sleep")
time.sleep(5)
print("After Sleep")
driver.execute_script('window.scrollTo(1,3000);')
time.sleep(5)
river.execute_script('window.scrollTo(1,3000);')
comment_div=driver.find_element_by_xpath('//*[@id="contents"]')
comments=comment_div.find_elements_by_xpath('//*[@id="content-text"]')
for comment in comments:
    print(comment.text)

#page = requests.get("https://www.youtube.com/watch?v=66y-llDYxIs")
#soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())
#list(soup.children)
#print([type(item) for item in list(soup.children)])
#html = list(soup.children)[2]
#print(html)
#print(list(html.children))