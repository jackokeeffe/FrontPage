// Change this URL if running locally
// It should look something like this: http://127.0.0.1:5000/news/
var api_url = 'https://this-front-page.herokuapp.com/news/'

// Used to fetch information from API
async function get_data() {
	var data = await fetch(api_url);
	update_elements([await data.json()]);
}

// Used to update the page with information from API
function update_elements(data) {
	sources = ["nyt", "techCrunch", "cnet"]
	classes = ["title", "description", "author", "source", "image", "link"]

	var x = 0;
	var y = 0;
	var sourcesLength = sources.length - 1;
	var classesLength = classes.length - 1;
	// Iterates through elements and changes then based on id/class name
	while (y <= sourcesLength) {
		var id = sources[y];
		while (x <= classesLength) {
			var targetData = data[0][sources[y]][classes[x]]
			if (classes[x] == "image") {
				document.getElementById(id).getElementsByClassName(classes[x])[0].src = targetData;
				document.getElementById(id).getElementsByClassName(classes[x])[0].alt = data[0][sources[y]]["alt"];
			} else if (classes[x] == "link") {
				document.getElementById(id).getElementsByClassName(classes[x])[0].href = targetData;
			} else {
				document.getElementById(id).getElementsByClassName(classes[x])[0].innerHTML = targetData;
			}
			x++
		}
		x = 0
		y++
	}
}

get_data();
