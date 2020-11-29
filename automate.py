from selenium import webdriver
import time

web = webdriver.Chrome()
web.get('https://forms.gle/zp7oFNKvVoyYWGsc7')
time.sleep(2)

Name = "Sareer Showket Mir"
fullname = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
fullname.send_keys(Name)

Roll = "46"
rollno = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
rollno.send_keys(Roll)

Std = "8th"
stdclass = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
stdclass.send_keys(Std)

Section = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div/span/div/div[1]/label/div')
Section.click()
time.sleep(1)

Submit = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
Submit.click()