# FrontPage

A minimal tech news aggregator. [Test it here](https://jackokeeffe.me/FrontPage/)

**NOTE:** The API (hosted on Heroku) may take up to 10-15 seconds to load the content, due to the limitations of the free plan.

![Website Preview Gif](https://cdn.glitch.com/366c5838-3763-4787-9bd2-8eefd6b529ab%2Fpreview.gif?v=1623615357210)

### How-To Run Locally:
1. Clone this repo `git clone https://github.com/jackokeeffe/FrontPage.git` into your command prompt.
2. If your outermost folder is not FrontPage type `cd FrontPage` into your command prompt.
3. Type `python setup.py install` into your command prompt. Wait for it to finish installing packages.
4. Run app.py, this will return a link (http://127.0.0.1:5000/).
5. In display.js, change the api_url variable to this link with 'news/' at the end (ex. http://127.0.0.1:5000/news/).
6. Finally, open index.html in your browser.

### Built With:
- Python
- Flask & Beautiful Soup 4
- HTML & CSS
- JavaScript
- Heroku

### Libraries Used:
- [Flask](https://flask.palletsprojects.com/en/2.0.x/): creating API and sending data on GET requests.
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/): collecting stock data from New York Times, TechCrunch and CNET.

### Author:
- Author: Jack O'Keeffe
- [Website](https://jackokeeffe.me)
