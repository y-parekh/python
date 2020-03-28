from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("https://web.whatsapp.com")

input("Press any key")

send = ""
flag = True
while True:
	i_msg_elements = driver.find_elements_by_class_name('_3zb-j')
	i_msg = i_msg_elements[len(i_msg_elements)-1].text

	if i_msg != send:
		flag = True

	if 'Hi' in i_msg:
		if flag:
			send = "Hey, how are you?"
			m = driver.find_element_by_class_name('_1Plpp')
			m.send_keys(send)
			time.sleep(2)

			btn = driver.find_element_by_class_name('_35EW6')
			btn.click()
			time.sleep(2)
			flag = False
	else:
		if flag:
			send = "Sorry, didn't get it."
			m = driver.find_element_by_class_name('_1Plpp')
			m.send_keys(send)
			time.sleep(2)

			btn = driver.find_element_by_class_name('_35EW6')
			btn.click()
			time.sleep(2)
			flag = False