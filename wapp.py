from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome("./chromedriver")
driver.get("https://web.whatsapp.com")

time.sleep(10)
print("Starting job")

text1 = "Hello {},"
text2 = "Local time is: {}."
text3 = "Thanks"
names = ["Bharat Bhai", "Ala", "Gabriella", "Red"]

for name in names:

	search = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
	search.send_keys(name)
	time.sleep(2)

	ActionChains(driver).key_down(Keys.DOWN).key_up(Keys.DOWN).perform()
	time.sleep(2)
	
	gmt = time.ctime(time.time())
	m = driver.find_element_by_class_name('_1Plpp')
	m.send_keys(text1.format(name))
	ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
	m.send_keys(text2.format(gmt))
	ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
	m.send_keys(text3)
	time.sleep(2)

	btn = driver.find_element_by_class_name('_35EW6')
	btn.click()
	time.sleep(2)

print("Success")


# Making bash command

# nano corona
# #!/bin/bash 
# python <PATH>/count.py

# chmod +x corona
# sudo cp corona /usr/bin/
