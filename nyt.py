from urllib.request import urlopen
from bs4 import BeautifulSoup

def times():
	url = "https://www.nytimes.com/section/technology"
	page = urlopen(url)
	html = page.read().decode("utf-8")
	soup = BeautifulSoup(html, "html.parser")
	try:
		main = str(soup.find('h2', {'class': 'css-4tvmog eecsw3u0'})).split('href="')[1].split('">')
		directory = main[0]
		title = main[1].split('</a>')[0]
		description = str(soup.find('p', {'class': 'css-1jhf0lz eecsw3u1'})).split('>')[1].split('<')[0]
		image = str(soup.find('article', {'class': 'css-1pagwdx'})).split('src="')[1].split('"')[0]
		image_alt = str(soup.find('article', {'class': 'css-1pagwdx'})).split('<img alt="')[1].split('"')[0]
		author = str(soup.find('p', {'class': 'css-s7sl7h e4e4i5l2'}))
		soup = BeautifulSoup(author, "html.parser")
		for data in soup(['style', 'script']):
			data.decompose()
		author = ''.join(soup.stripped_strings).split('By')[1].split('and')
		author = author[0] + " and " + author[1]
		data = {'title': title, 'description': description, 'author': 'Author: ' + author, 'image': image, 'alt': image_alt, 'link': "https://www.nytimes.com/" + directory, "source": "New York Times"}
		return data
	except:
		print("Error")

times()