import os
import random
import sqlite3 as sql

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
lunch_list = ["마라탕", "맥도날드", "인도카레", "육수당", "돈카츠", "서브웨이", "라멘", "초밥"]

def menu_choice(lunch_list):
	menu = random.sample(lunch_list, k=1)
		
	return menu

@app.route('/', methods = ['GET'])
def lunch():
		
	if request.method == "GET":
		
		menu = "".join(menu_choice(lunch_list))

		return render_template('lunch.html', lunch_menu=menu, lunch_menus=lunch_list)


@app.route('/add_menu', methods=['POST', 'GET'])
def add_menu():    	
	if request.method == "POST":

		menu = request.form.get('menu_add', False)

		lunch_list.append(menu)

		return redirect(url_for('lunch'))

	else:
		return render_template('addmenu.html')

	"""
	elif request.method == "POST":
		try:
			menu = request.form['menu']

			with sql.connect('database.db') as con : 
				cur = con.cursor()

				cur.execute('INSERT INTO menus (menu) values(?)', (menu))

				con.commit()

		finally:
			#return render_template('lunch.html', lunch_menu=menu, lunch_menus=lunch_list)
			con.close()
	"""


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)		
