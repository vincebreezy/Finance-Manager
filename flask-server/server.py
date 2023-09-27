from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
app = Flask(__name__)
app.secret_key = 'finance_manager'

db = con.cursor("CREATE TABLE user(user_id, username, password, )")

#members API route
def create_connection():
	con = sqlite3.connect("finance.db")
	return con
@app.route('/')
def home():
	if 'username' in sessions:
		#route to dashboard
	else:
		#route the login


@app.route("/members")
def members():
	return {"members": ["Member1", "Member2", "Member3"]}

if __name__ == "__main__":
	app.run(debug = True)