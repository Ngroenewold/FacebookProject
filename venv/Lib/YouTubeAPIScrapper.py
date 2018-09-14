from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.youtube.com/watch?v=5lOp1eXgeYc")
time.sleep(2)
driver.execute_script('window.scrollTo(1,500);')
elm = driver.find_element_by_tag_name('html')
time.sleep(5)
for x in range(1, 20):
    elm.send_keys(Keys.END)
    time.sleep(1)
comment_div = driver.find_element_by_xpath('//*[@id="contents"]')
comments = comment_div.find_elements_by_xpath('//*[@id="content-text"]')
for comment in comments:
    print(comment.text)
driver.close()


