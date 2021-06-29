from urllib.request import urlopen
from bs4 import BeautifulSoup

def net():
	url = "https://www.cnet.com"
	page = urlopen(url)
	html = page.read().decode("utf-8")
	soup = BeautifulSoup(html, "html.parser")
	try:
		main = str(soup.find('a', {'class': 'mainStory'}))
		title = main.split('title="')[1].split('">')[0]
		link = url + str(main.split('href="')[1].split('"')[0])
		description = str(soup.find('div', {'class': 'content'})).split('<p>')[1].split('</p>')[0]
		author = 'Author: ' + str(soup.find('a', {'rel': 'author'})).split('>')[1].split('<')[0]
		image = str(soup.find('figure', {'class': 'img'})).split('src="')[1].split('"')[0]
		print(image)
		image_alt = "image from cnet"
		data = {'title': title, 'description': description, 'author': author, 'image': image, 'alt': image_alt, 'link': link, "source": "CNET"}
		return data
	except:
		print("Error")

net()
