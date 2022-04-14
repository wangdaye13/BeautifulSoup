import os
import sys
import json

from flask import Flask, render_template 
from flask import request, redirect, url_for, flash

app = Flask(__name__)


@app.route('/')
def displayJobDetails():
	responseJSON = {}
	responseJSON = json.dumps(responseJSON)
	return render_template('index.html', responseJSON=responseJSON)
