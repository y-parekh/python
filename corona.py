import requests
from bs4 import BeautifulSoup
from plyer import notification
import time


def show(col):
	country = col[1].string.strip()
	cases = col[3].string.strip()
	death = col[7].string.strip()
	print('*'*10)
	print("Country: ",country)
	print("Cases:   ",cases)
	print("Deaths:  ",death)

res = requests.get("https://www.worldometers.info/coronavirus/").text
soup = BeautifulSoup(res, "html.parser")
soup.encode("utf-8")

l = ["india", "uk"]
for i in l:
	href = "country/{}/".format(i)
	data = soup.find("a", {"href": href})
	row = data.parent.parent
	col = row.contents
	show(col)