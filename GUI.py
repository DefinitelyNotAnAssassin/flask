import sqlite3
from tkinter import *

#Note: Try the for loop command with ~elif~

conn = sqlite3.connect("products.db")
c = conn.cursor()


master = Tk() 

color = '#ffffff'


wlcm = Label(text = "E - Palengke Prevailing Price — Metro Manila")
wlcm.pack()



def cart():
	cart.basket = []
	
def checkcart():
	checkcart.filtered = []
	for i in cart.basket:
		if i not in checkcart.filtered:
			checkcart.filtered.append(i)
	
	for i in checkcart.filtered:
		try:
			find = "SELECT * FROM produkto WHERE product = ?"
			c.execute(find, (i,))
			res = c.fetchall()
			quantity = res[0][4]
			productlbl = Label(cartWindow.new, text = f"{i}  {quantity}")
			productlbl.pack()
		except:
			pass
		

def count():
	#highland  vegetables
	count.sayote = 0
	count.cabbage = 0
	count.carrot = 0
	count.habitchuelas = 0
	count.pechay = 0
	count.potato = 0
	#lowland vegetables
	count.ampalaya = 0
	count.pechaynative = 0
	count.tomato = 0
	count.squash = 0
	count.eggplant = 0
	count.sitao = 0
	#livestock
	count.beefrump = 0
	count.beefbrisket = 0
	count.porkham = 0
	count.liempo = 0
	count.wholechicken = 0
	count.chickenegg = 0

#lowland 
def ampalaya():
	m = "UPDATE produkto SET quantity = ? WHERE product = ?"
	count.ampalaya += 1
	cart.basket.append("Ampalaya")
	s = "Ampalaya"
	c.execute(m, (count.ampalaya, s))
	conn.commit()	

def pechaynative():
	cart.basket.append("Pechay")

def squash():
	m = "UPDATE produkto SET quantity = ? WHERE product = ?"
	count.squash += 1
	cart.basket.append("Squash")
	s = "Squash"
	c.execute(m, (count.squash, s))
	conn.commit()	
def sitao():
	m = "UPDATE produkto SET quantity = ? WHERE product = ?"
	count.sitao += 1
	s = "Sitao"
	cart.back.append(s)
	c.execute(m, (count.sitao, s))
	conn.commit()
def eggplant():
	count.eggplant += 1
	m = "UPDATE produkto SET quantity = ? WHERE product = ?"
	cart.basket.append("Eggplant")
	s = "Eggplant"
	c.execute(m, (count.eggplant, s))
	conn.commit()

def sitao():
	cart.basket.append("Sitao")	
	
#Livestock

def beefrump():
	count.beefrump += 1
	b = "UPDATE produkto SET quantity = ? WHERE product = ?"
	d = "Beef Rump"
	cart.basket.append(d)
	c.execute(b, (count.beefrump, d))
	conn.commit()
	
def beefbrisket():
	count.beefbrisket += 1
	b = "UPDATE produkto SET quantity = ? WHERE product = ?"
	d = "Beef Brisket"
	cart.basket.append(d)
	c.execute(b, (count.beefbrisket, d))
	conn.commit()
def porkham():
	count.porkham += 1
	b = "UPDATE produkto SET quantity = ? WHERE product = ?"
	d = "Pork Ham"
	cart.basket.append(d)
	c.execute(b, (count.porkham, d))
	conn.commit()

def liempo():
	count.liempo += 1
	b = "UPDATE produkto SET quantity = ? WHERE product = ?"
	d = "Liempo"
	cart.basket.append(d)
	c.execute(b, (count.liempo, d))
	conn.commit()

def wholechicken():
	count.wholechicken += 1
	b = "UPDATE produkto SET quantity = ? WHERE product = ?"
	d = "Whole Chicken"
	cart.basket.append(d)
	c.execute(b, (count.wholechicken, d))
	conn.commit()
	
def chickenegg():
	count.chickenegg += 1
	b = "UPDATE produkto SET quantity = ? WHERE product = ?"
	d = "Chicken Egg"
	cart.basket.append(d)
	c.execute(b, (count.chickenegg, d))
	conn.commit()	

	

count()
cart()
def checkoutWindow():
	checkcart()
	master.withdraw()
	checkoutWindow.new = Toplevel(master)
	total = 0
	for i in checkcart.filtered:
		try: 
			fnd = "SELECT * FROM produkto WHERE product = ?"
			c.execute(fnd, (i,))
			price = c.fetchall() 
			quantity = float(price[0][4])
			prevailing = float(price[0][3])
			final = quantity * prevailing
			checkoutlbl = Label(checkoutWindow.new, text = f"{price[0][0]}  x {price[0][4]} kg = {final}")
			if price[0][0] == "Chicken Egg":
				checkoutlbl.config(text = f"{price[0][0]} x {price[0][4]} pc = {final}")
			checkoutlbl.pack()
			total += final
		except:
			pass
	finallbl = Label(checkoutWindow.new, text = f"Total Cost (Prevailing Price): {total}")
	finallbl.pack()
	
	
	
def cartWindow():
	ShopWindow.shop.withdraw()
	cartWindow.new = Toplevel(ShopWindow.shop)
	checkcart()
	
def minimizeShop(): 
	ShopWindow.shop.withdraw()
	master.deiconify()
	
def lbck():
	LivestockWindow.new.withdraw()
	ShopWindow.shop.deiconify()
def LivestockWindow():
	ShopWindow.shop.withdraw()
	LivestockWindow.new = Toplevel(ShopWindow.shop)
	liveall = "SELECT * FROM produkto"
	c.execute(liveall)
	result = c.fetchall()
	liveres = result[12:19]
	for i in liveres:
		lbtn = Button(LivestockWindow.new, text = f"{i[0]}  {i[3]}")
		item = i[0]
		if i[0] == "Beef Rump":
			lbtn.config(command = beefrump)
		elif item == "Pork Ham":
			lbtn.config(command = porkham)			
		elif item == "Beef Brisket":
			lbtn.config(command = beefbrisket)
		elif item == "Liempo":
			lbtn.config(command = liempo)
		elif item == "Whole Chicken":
			lbtn.config(command = wholechicken)
		elif item == "Chicken Egg":
			lbtn.config(command = chickenegg)
		lbtn.pack()
		
			
	lbackbtn = Button(LivestockWindow.new, text = "Back", command = lbck)
	lbackbtn.pack()
	

	
def lvback():
	low_vegWindow.new.withdraw()
	ShopWindow.shop.deiconify()
def low_vegWindow():
	ShopWindow.shop.withdraw()
	low_vegWindow.new = Toplevel(ShopWindow.shop)
	all = "SELECT * FROM produkto"
	c.execute(all)
	allresult = c.fetchall()
	low_vegWindow.iterate = allresult[6:11]
	#for loop
	#TODO fix the function!!!
	for i in low_vegWindow.iterate:
		lbl = Label(low_vegWindow.new, text = i[0])
		lbl.pack()
		abtn = Button(low_vegWindow.new, text = f"{i[0]}  {i[3]}")
		if i[0] == "Ampalaya":
			abtn.config(command = ampalaya)
			
		elif i[0] == "Squash":
			abtn.config(command = squash)
			
		elif i[0] == "Pechay":
			abtn.config(command = pechaynative)
			conn.commit()
			
		elif i[0] == "Eggplant":
			abtn.config(command = eggplant)
			
		elif i[0] == "Sitao":
			abtn.config(command = sitao)
		
		abtn.pack()
		
	#back button
	backbtn = Button(low_vegWindow.new, text="Back", command = lvback)
	backbtn.pack()
def high_vegWindow():
	ShopWindow.shop.withdraw()
	high_vegWindow.new = Toplevel(ShopWindow.shop)
	select = "SELECT * FROM produkto"
	c.execute(select)
	result = c.fetchall()
	
	#Function if clicked >> append to cart.basket
	def sayoteclck():
		count.sayote += 1
		m = "Chayote"
		cart.basket.append(m)
		update = "UPDATE produkto SET quantity = ? WHERE product = ?"
		c.execute(update, (count.sayote, m))
		conn.commit()
		
	def cabbageclck():
		count.cabbage += 1
		m = "Cabbage"
		cart.basket.append(m)
		update = "UPDATE produkto SET quantity = ? WHERE product = ?"
		c.execute(update, (count.cabbage, m))
		conn.commit()
		#
	def carrotclck():
		count.carrot += 1
		m = "Carrots"
		cart.basket.append(m)
		update = "UPDATE produkto SET quantity = ? WHERE product = ?"
		c.execute(update, (count.carrot, m))
		conn.commit()
		
	def habitchuelasclck():
		count.habitchuelas += 1
		m = "Habitchuelas"
		cart.basket.append(m)
		update = "UPDATE produkto SET quantity = ? WHERE product = ?"
		c.execute(update, (count.habitchuelas, m))
		conn.commit()
		
	def pechayclck():
		count.pechay += 1
		m = "Pechay Baguio"
		cart.basket.append(m)
		update = "UPDATE produkto SET quantity = ? WHERE product = ?"
		c.execute(update, (count.pechay, m))
		conn.commit()
	
	def potatoclck():
		count.potato += 1
		m = "White Potato"
		cart.basket.append(m)
		update = "UPDATE produkto SET quantity = ? WHERE product = ?"
		c.execute(update, (count.potato, m))
		conn.commit()
		
		
	
	def min():
		high_vegWindow.new.withdraw()
		ShopWindow.shop.deiconify()
	#Buttons
	sayotebtn = Button(high_vegWindow.new, text = f"{result[0][0]}  {result[0][3]}", command = sayoteclck)
	cabbagebtn = Button(high_vegWindow.new, text= f"{result[1][0]} {result[1][3]}", command = cabbageclck)
	carrotsbtn = Button(high_vegWindow.new, text= f"{result[2][0]} {result[2][3]}", command = carrotclck)
	habitchuelas_btn = Button(high_vegWindow.new, text= f"{result[3][0]} {result[3][3]}", command = habitchuelasclck)
	potatobtn = Button(high_vegWindow.new, text= f"{result[4][0]} {result[4][3]}", command = potatoclck)
	pechay_btn = Button(high_vegWindow.new, text = f"{result[5][0]} {result[5][3]}", command = pechayclck)
	backbtn = Button(high_vegWindow.new, text ="Back", command = min)
	#TODO: Arrange the order + scaling
	carrotsbtn.pack()
	pechay_btn.pack()
	potatobtn.pack()
	cabbagebtn.pack()
	habitchuelas_btn.pack()
	sayotebtn.pack()
	backbtn.pack()
	
def ShopWindow():
	master.withdraw()
	ShopWindow.shop = Toplevel(master)
	shopwlcm = Label(ShopWindow.shop,text = "Shop")
	shopwlcm.pack()
	poultrybtn = Button(ShopWindow.shop, text = "Livestock and Poultry", command = LivestockWindow)
	poultrybtn.pack()
	l_vegbtn = Button(ShopWindow.shop, text ="Lowland Vegetables", command = low_vegWindow)
	l_vegbtn.pack()
	h_vegbtn = Button(ShopWindow.shop, text = "Highland Vegetables", command = high_vegWindow)
	h_vegbtn.pack()
	backbtn = Button(ShopWindow.shop, text = "Back", command = minimizeShop)
	backbtn.pack()

shopbtn = Button(text = "Shop", command = ShopWindow, bg = color)
shopbtn.pack()
cartbtn = Button(text = "Cart", command = cartWindow, bg = color)
cartbtn.pack()
checkoutbtn = Button(text="Checkout", command = checkoutWindow,bg = color)
checkoutbtn.pack()

mainloop()