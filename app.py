from flask import *
import sqlite3


#users 
#username and password



conn = sqlite3.connect("products.db")
c = conn.cursor()

all = "SELECT * FROM produkto"
c.execute(all )
result = c.fetchall()


app = Flask(__name__)

def cart():
	cart.basket = []
	cart.filter = []
	for i in cart.basket:
		if i not in cart.filter:
			cart.filter.append(i)
	
		

def checkcart():
	checkcart.filter = []
	for i in cart.basket:
		if i not in checkcart.filter:
			checkcart.filter.append(i)
			
		

def count():
	count.chayote = 0
	count.cabbage = 0


def logic():
	if count.chayote != 0:
		cart.basket.append("Chayote")
	if count.cabbage != 0:
		cart.basket.append("Cabbage")
	
	

cart()
count()
logic()

@app.route("/")
def homepage():
	return render_template("index.html")
 
@app.route("/shop", methods = ["POST", "GET"])
def shopPage():
	req = request.get_json()
	print(req)
	return render_template("shop.html", item = result)
	
	
	


@app.route("/cart")
def cartPage():
	print(f"{count.chayote} {count.cabbage} {cart.filter}")
	logic()
	checkcart()
	print(f"{count.chayote} {count.cabbage} {checkcart.filter}")
	return render_template("cart.html", cart = checkcart.filter, req = sendPage.req)



@app.route("/checkout")
def checkoutPage():
	pass
	

@app.route("/send", methods = ["POST"])
def sendPage():
	sendPage.req = request.get_json()
	print(sendPage.req)
	chayoteqty = sendPage.req["chayoteqty"]
	cabbageqty = sendPage.req["cabbageqty"]
	try:
		count.chayote += float(chayoteqty)
		count.cabbage += float(cabbageqty)
	except:
		pass

	return "hi"
if __name__ == "__main__":
	app.run()
	
 