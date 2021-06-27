from flask import *
import sqlite3
from datetime import timedelta
from collections import defaultdict

#users 
#username and password




conn = sqlite3.connect("products.db")
c = conn.cursor()

all = "SELECT * FROM produkto"
c.execute(all)
result = c.fetchall()
lowland = result[6:12]
highland = result[0:6]
livestock = result[12:19]


prevailing = "SELECT prevailing FROM produkto"
c.execute(prevailing)






temp_list = list(c.fetchall())
prevail = [float(i[0]) for i in temp_list]




app = Flask(__name__)
app.secret_key = "HiHelloHallo"
app.permanent_session_lifetime = timedelta(minutes=5)


def redirect_url(default='index'):
    return request.args.get('next') or \
           request.referrer or \
           url_for(default)




@app.route("/")
def homepage():
	return render_template("index.html")
 
@app.route("/shop", methods = ["POST", "GET"])
def shopPage():
	return render_template("test.html")
	
	
@app.route("/shop/lowland")
def lowlandPage():
	return render_template("lowland.html", item = lowland)
		
@app.route("/shop/highland")
def higlandPage():
	return render_template("highland.html", item = highland)
		
@app.route("/shop/livestock")
def livestockPage():
	return render_template("livestock.html", item = livestock)
	
	

	
	
	
	
	
@app.route("/cart")
def cartPage():
	if "Chayoteqty" in session or "Cabbageqty" in session or "Carrotsqty" in session: 
		return render_template("cart.html", cart = session["item"], req = sendPage.req)
	else:
		return redirect(url_for("shopPage"))


@app.route("/update", methods = ["POST"])
def updatePage():
	if request.method == "POST":
		for i in session['item']:
			try:
				session[f'{i}qty'] = int(request.form[f"{i}"])
			except:
				pass
			
			
		#print(session)
		return redirect(redirect_url())


@app.route("/checkout")
def checkoutPage():
	if "Chayoteqty" in session or "Cabbageqty" in session or "Carrotsqty" in session:
		return render_template("checkout.html", price = prevail, res = result, cart = session["item"], req = sendPage.req)
	else:
		return redirect(url_for("shopPage"))

	
	
		
				
@app.route("/test")
def testPage():
	return render_template("testpage.html")
	
	




@app.route("/send", methods = ["POST"])
def sendPage():
	if "iterate" in session:
		pass
	elif "iterate" not in session:
		session["item"] = []	
		
	session["iterate"] = "no"
	if request.method == "POST":
		for i in result: 
			try:
				if f"{i[0]}qty" in session:
					session[f"{i[0]}qty"] += int(request.form[f"{i[0]}"])
					print("Ping")
					if f"{i[0]}" not in session["item"] and session[f"{i[0]}qty"] >= 1:
						session["item"].append(f"{i[0]}")
					
				
				else:	
					session[f"{i[0]}qty"] = int(request.form[f"{i[0]}"])
					print("Pong")
					if f"{i[0]}" not in session["item"] and session[f"{i[0]}qty"] >= 1:
						session["item"].append(f"{i[0]}")
					elif f"{i[0]}":
						pass
						
	
			except:
				pass
		sendPage.req = session
		print(session)		
		return redirect(redirect_url())
	


if __name__ == "__main__":
	app.run()
	
 