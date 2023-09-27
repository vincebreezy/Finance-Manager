from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
app = Flask(__name__)
app.secret_key = 'finance_manager'


#members API route
def create_connection():
	con = sqlite3.connect("finance.db")
	return con
@app.route('/')
def home():
	if 'username' in sessions:
		#route to dashboard
	#else:
		#route the login

@app.route('/register', methods = ['GET', 'POST'])
def register():
	if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        existing_user = cursor.fetchone()
        if existing_user:
            return "Username already exists. Please choose another one."
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        session['username'] = username
        return redirect(url_for('home'))
    return render_template('register.html')


@app.route("/members")
def members():
	return {"members": ["Member1", "Member2", "Member3"]}

if __name__ == "__main__":
	app.run(debug = True)

@app.route("/login", methods = ['GET', 'POST'])
def login():
	if request.method == 'POST':

		username = request.form['username']
		password = request.form['password']
		con = create_connection()
		cursor = con.cursor()
		cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
		user = cursor.fetchone()
		con.close()

		if user:
			session['username'] = username
			return redirect(url_for('home'))
		else:
			error = 'invalid'
			return render_template('login.html', error = error)