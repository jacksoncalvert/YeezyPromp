import requests
from bs4 import BeautifulSoup
from selenium import webdriver

url = "https://www.chrisburkard.com/"

web_r = requests.get(url)
web_soup = BeautifulSoup(web_r.text, 'html.parser')

print(len(web_soup.findAll("img")))


driver = webdriver.Firefox()
driver.get("https://www.adidas.com.au/yeezy")
	