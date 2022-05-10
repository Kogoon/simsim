from flask import Flask, render_template

import random

app = Flask(__name__)


def menu_choice():
		lunch_list = ["마라탕", "맥도날드", "인도카레", "육수당", "돈카츠", "서브웨이", "라멘", "초밥"]
		menu = random.sample(lunch_list, k=1)
		
		return menu

@app.route('/', methods = ['GET'])
def lunch():
		menu = "".join(menu_choice())

		return render_template('lunch.html', lunch_menu=menu)


if __name__ == '__main__':
		app.run(host='0.0.0.0', port=80)		
