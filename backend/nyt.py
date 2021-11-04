from urllib.request import urlopen
from bs4 import BeautifulSoup

def times():
	url = "https://www.nytimes.com/section/technology"
	page = urlopen(url)
	html = page.read().decode("utf-8")
	soup = BeautifulSoup(html, "html.parser")
	try:
		# ID Changed on 11/04/21 due to HTML change on NYT's homepage.
		main = str(soup.find('ol', {'class': 'css-11jjg eb97p612'}))
		directory = main.split('href="')[1].split('">')[0]
		index = main.split('</a></div>')[1].split('.html">')[1]
		title = index.split('<')[0]
		description = index.split('">')[1].split('<')[0]
		image = main.split('src="')[1].split('"')[0]
		image_alt = main.split('img alt="')[1].split('src')[0]
		author = index.split('itemprop')[1].split('>')[1].split('<')[0]
		data = {'title': title, 'description': description, 'author': 'Author: ' + author, 'image': image, 'alt': image_alt, 'link': "https://www.nytimes.com/" + directory, "source": "New York Times"}
		return data
	except:
		print("Error")

times()
