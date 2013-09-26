from flask import render_template
from flask import request
from app import app

from dominion import Dominion

@app.route('/')
@app.route('/index')
def index():
	d = Dominion()

	sets = ['Base', 'Alchemy', 'Cornucopia', 'Dark Ages', 'Hinterlands', 'Intrigue', 'Prosperity', 'Seaside']

	selected = request.args.getlist('selected[]')

	result = d.get_random_cards(selected)

	if (selected == None):
		selected = []

	return render_template("index.html", sets=sets, selected=selected, result=result)
