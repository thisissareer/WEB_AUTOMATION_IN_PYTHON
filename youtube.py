from selenium import webdriver
import time

web = webdriver.Chrome()
web.get('https://www.youtube.com/')
time.sleep(2)

Search = "Sareer Talks"
Enter = web.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')
Enter.send_keys(Search)

Final = web.find_element_by_xpath('//*[@id="search-icon-legacy"]/yt-icon')
Final.click()