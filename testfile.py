import sqlite3


conn = sqlite3.connect("products.db")
c = conn.cursor()

#c.execute("""ALTER TABLE produkto
#	ADD quantity int""")

#c.execute('''CREATE TABLE product(
#	name text,
#	quantity int,
#	high int,
#	low int,
#	prevail int
#)''')""


#m = "UPDATE produkto SET product = trim(product)"

#c.execute(m)
#conn.commit()
#*// Start of the Code //*#


hihello = "SELECT prevailing FROM produkto"
c.execute(hihello)


def updater():
	low = input("Low: ")
	high = input("High: ")
	prevailing = input("Prevailing: ")
	newname = input("Enter new name: ")
	up = "UPDATE produkto SET product = ? WHERE low = ? AND high = ? AND prevailing = ?"
	c.execute(up, (newname, low, high, prevailing,))
	conn.commit()
def cart():
	cart.product_cart = []

def addProduct():
	add = "INSERT INTO product (name, quantity, high, low, prevail) VALUES = (?,?,?,?,?)"
	name = input("Name: ")
	quanti = input("Quantity: ")
	high = input("High: ")
	low = input("Low: ")
	prevail = input("Prevailing: ")
	
def check():
	search = "SELECT * FROM produkto"
	c.execute(search)
	print(c.fetchall())
	
def add():
	addproduct = input("Product: ")	
	exist = "SELECT * FROM produkto WHERE product = ?"
	c.execute(exist, (addproduct.title(), ))
	result = c.fetchall()
	if result:
		ex = 0
	else:
		print("Product Doesn't Exist")
		ex = 1
		
	if ex != 1:
		quanti = input("Quantity (in Kilos):  ")
		updateproduct = "UPDATE produkto SET quantity = ? WHERE product = ?" 
		c.execute(updateproduct, (quanti, addproduct.title()))
		conn.commit()
		cart.product_cart.append(addproduct.title())
def logic():
	z = 0
	for item in cart.product_cart:
		try:
			i = item
			cal = "SELECT * FROM produkto WHERE product = ?"
			c.execute(cal, (item,))
			result = c.fetchall()
			prevail = float(result[0][3])
			quantity = float(result[0][4])
			calculate = prevail * quantity
			z += calculate
		except:
			pass
	return print(f"Total cost: {z}")
	
def checkcart():
	for i in cart.product_cart:
		find = "SELECT * FROM produkto WHERE product = ?"
		c.execute(find, (i,))
		result = c.fetchall()
		quantity = result[0][4]
		print(f"{i}  {quantity} kilos")
def test():
	t = "SELECT * FROM produkto"
	c.execute(t)
	result = c.fetchall()
	print(result[12:19])
	print(result[0:6])
	print(result[6:12])

def shop():
		for i in cart.product_cart:
			ele = i
			default = "UPDATE produkto set quantity = 0 WHERE product = ?"
			c.execute(default, (ele,))
			conn.commit()
cart()
test()
while(True):
			cmd = input(">")
			if cmd.lower() == "shop":
				add()
				#do_something
				pass
			
			if cmd.lower() == "checkdb":
				check()
			if cmd.lower() == "checkcart":
				checkcart()
			if cmd.lower() == "update":
				updater()
			if cmd.lower() == "checkout":
				logic()
				shop()
				break

				
scratch = '''												
	  <button type="button"
	   onclick ="increase()" 
	   id = "{{i}}add">+
	   </button>
	  <input type ="number" 
	  min = 0 
	  value = {{req['Cabbageqty']}}
	  id = "{{i}}num">
	  <button type = "button"
	   onclick = "decrease()"
	   id = "{{i}}sub"> - </button>	
	   
	   		
	   				
	   						
	   								
	   										
	   

{% if i == "Chayote" %}

<h3 style = "font-family:Times New Roman;">{{i}} x {{req['Chayoteqty']}}</h3>

{% endif %}

{% if i == "Cabbage" %}


	  
{% endif %} 

{% if i == "Carrots" %}

<h3>{{i}} x {{req['Carrotsqty']}}</h3>

{% endif %} 

{% if i == "Habitchuelas" %}

<h3>{{i}} x {{req['Habitchuelasqty']}}</h3>

{% endif %}

 {% if i == "White Potato" %}
 
<h3>{{i}} x {{req["White Potatoqty"]}}</h3>

{% endif %}


{% endfor %} 
</form>
</div>
</div>

<!-- Lowland -->

												
	   																
			
		'''

