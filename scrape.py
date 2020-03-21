import shutil 
import os 
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import difflib
#import emailScript

url = "https://www.adidas.com.au/yeezy"

#web_r = requests.get(url)
#web_soup = BeautifulSoup(web_r.text, 'html.parser')

#print(len(web_soup.findAll("img")))
listVersion = []

driver = webdriver.Firefox()
inter = 0

driver.get(url)

html = driver.execute_script("return document.documentElement.outerHTML")
sel_soup = BeautifulSoup(html, 'html.parser')
listVersion.append(sel_soup.prettify())

while(inter < 10):
	driver.get(url)

	html = driver.execute_script("return document.documentElement.outerHTML")
	sel_soup = BeautifulSoup(html, 'html.parser')

	#listVersion.append(sel_soup.prettify())
	#print(sel_soup.prettify())
	listVersion.append(sel_soup.prettify())
	if len(listVersion)> 2:
		listVersion.remove()
	diff = difflib.ndiff(listVersion[1],listVersion[0])

	print(''.join(diff))
	inter +=1 
	print(inter)
	time.sleep(10)






# images = []
# for i in sel_soup.findAll('img'):
# 	try: 

# 		src = i["src"]
# 		images.append(src)
# 	except:
# 		pass

# for src in images:
# 	print(src)



# currPath = os.getcwd()


# count = 1
 
# for img in images:
# 	try :
# 		fileName = os.path.basename(img)
# 		imgR = requests.get(img, Stream = True)
# 		newPath = os.join(currPath, "images", fileName)
# 		with open(newPath, "wb") as outputFile:
# 			shutil.copyfileobj(imgR.raw, outputFile)
# 		del imgR
# 	except:
# 		pass

# 	count = count+1
# 	print(count)






#driver.quit()
#print(len(listVersion))

#print(listVersion[0] == listVersion[1])






  