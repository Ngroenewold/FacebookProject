from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get("https://www.youtube.com/watch?v=9hDKfBKuXjI")
time.sleep(1)
print("window.scrollHeight();")
driver.execute_script('window.scrollTo(1,50);')
time.sleep(3)
driver.execute_script('window.scrollTo(1,100);')
time.sleep(3)
print(1)
driver.execute_script('window.scrollTo(1,3000);')
time.sleep(3)
print(2)
driver.execute_script('window.scrollTo(1,3000);')
time.sleep(3)
print(3)
driver.execute_script('window.scrollTo(1,3000);')


comment_div=driver.find_element_by_xpath('//*[@id="contents"]')
comments=comment_div.find_elements_by_xpath('//*[@id="content-text"]')
for comment in comments:
    print(comment.text)

