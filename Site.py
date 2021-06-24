from flask import Flask, redirect, url_for, render_template, request, session, flash
import sqlite3
conn = sqlite3.connect("products.db")
c = conn.cursor()

cmd = "SELECT product FROM produkto"
c.execute(cmd)
item = c.fetchall()



app = Flask(__name__)
app.secret_key = "hello"
@app.route("/")
def homepage():	
	return render_template("index.html", content = item)
	
@app.route("/login", methods = ["POST", "GET"])
def loginpage():
	if request.method == "POST":
		user = request.form["nm"]
		session["user"] = user
		return redirect(url_for("userpage"))
	
	else:
		if "user" in session:
			flash("Already Login.")
			return redirect(url_for("userpage"))			
		return render_template("login.html")
		
		
	
@app.route("/user")
def userpage():
	if "user" in session:
		user = session["user"]
		return render_template("user.html")
	else:
		return redirect(url_for("loginpage"))
	

@app.route('/logout')
def logoutpage():
	session.pop("user", None)
	return redirect(url_for("loginpage"))
	
if __name__ == "__main__":
	app.run()
