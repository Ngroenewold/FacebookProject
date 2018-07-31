from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/watch?v=Qn7OuGW9KEU")
# get both instances of the html tag to use of the logic of the loop iterating through the page
# while ! elm_list[1] // do code


elm = driver.find_element_by_tag_name('html')


time.sleep(3)

#while(Keys.END):
    #elm.send_keys(Keys.END)

#time.sleep(2)
comment_div= driver.find_element_by_xpath('//*[@id="contents"]')
comments=comment_div.find_elements_by_xpath('//*[@id="content-text"]')
for comment in comments:
    print(comment.text)
driver.close()


