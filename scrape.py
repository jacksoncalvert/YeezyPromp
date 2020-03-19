import requests
from bs4 import BeautifulSoup
from selenium import webdriver

url = "https://www.adidas.com.au/yeezy"

#web_r = requests.get(url)
#web_soup = BeautifulSoup(web_r.text, 'html.parser')

#print(len(web_soup.findAll("img")))


driver = webdriver.Firefox()
driver.get(url)

html = driver.execute_script("return document.documentElement.outerHTML")
sel_soup = BeautifulSoup(html, 'html.parser')

print(sel_soup.('Cinder'))

  