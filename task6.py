import os
import sys
import json
import requests
from flask import Flask, render_template 
# from flask import request, redirect, url_for, flash



# Flask expects the template folder to be `templates` by default. Change this to `template` to fit assignment criteria.
app = Flask(__name__, template_folder='template')




@app.route('/')
def displayJobDetails():
	url = 'https://raw.githubusercontent.com/crispycret/pythonBeautifulSoup/main/jobDetails.json'
	
	# Request the jobDetails.json file that we retireved from indeed.com
	response = requests.get(url)
	
	# Retireve the response content as json data
	responseJSON = response.json()
	
	# Render the index.html template by passing in the responseJSON data.
	return render_template('index.html', responseJSON=responseJSON)








