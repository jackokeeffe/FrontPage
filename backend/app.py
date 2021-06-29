# Libraries used to create API
from flask import Flask
from flask_cors import CORS

# Functions needed to return HTML data
from nyt import times
from techCrunch import tech
from cnet import net

# Creating Flask Object
app = Flask(__name__)
cors = CORS(app)

# Path to access data (through GET request)
@app.route('/news/')

# Returns HTML news data when a GET request is made
def news_data():
    condensed = {'nyt': times(), 'techCrunch': tech(), 'cnet': net()} # Puts data from functions into dict for Javascript
    return condensed, 200 # Return dict with data and code (200 = success)

if __name__ == '__main__':
    app.run() # Run API
