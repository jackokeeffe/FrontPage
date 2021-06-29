from urllib.request import urlopen
from bs4 import BeautifulSoup

def tech():
	url = "https://techcrunch.com/"
	page = urlopen(url)
	html = page.read().decode("utf-8")
	soup = BeautifulSoup(html, "html.parser")
	try:
		main = str(soup.find('a', {'class': 'post-block__title__link'})).split('href="')[1].split('">')
		link = main[0]
		title = main[1].split("\t")[4]
		description = str(soup.find('div', {'class': 'post-block__content'})).split('	')[2]
		if description[-1] != ".":
			description = description + "..."
		author = str(soup.find('span', {'class': 'river-byline__authors'})).split('	')[4]
		image = str(soup.find('figure', {'class': 'post-block__media'})).split('img src="')[1].split('"/>')[0]
		image_alt = "image from tech crunch"
		data = {'title': title, 'description': description, 'author': 'Author: ' + author, 'image': image, 'alt': image_alt, 'link': link, "source": "Tech Crunch"}
		return data
	except:
		print("Error")

tech()
