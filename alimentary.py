#!/usr/bin/python2.7
#coding:utf-8

class Date :
	def __init__(self, d = 1, m = 1, y = 2000) :
		self.d = d
		self.m = m
		self.y = y

	def scan(self) :
		date = raw_input("Entrez une date : ")
		values = date.split("/")

		self.d = int(values[0])
		self.m = int(values[1])
		self.y = int(values[2])

	@staticmethod
	def format(date) :
		d = Date()
		values = date.split("/")

		d.d = int(values[0])
		d.m = int(values[1])
		d.y = int(values[2])

		return d

	def printer(self) :
		print "{}/{}/{}".format(self.d, self.m, self.y)

	def __le__(self, obj) :
		if self.y < obj.y : return 1
		elif self.y > obj.y : return 0

		if self.m < obj.m : return 1
		elif self.m > obj.m : return 0

		if self.d <= obj.d : return 1

		return 0

	def __ge__(self, obj) :
		if self.y > obj.y : return 1
		elif self.y < obj.y : return 0

		if self.m > obj.m : return 1
		elif self.m < obj.m : return 0

		if self.d >= obj.d : return 1

		return 0

	def __str__(self) :
		return "{}/{}/{}".format(self.d, self.m, self.y)

class Ingredient :
	def __init__(self, name = "Unamed", quantity = 0, unity = "") :
		self.name = name
		self.quantity = quantity
		self.unity = unity

	def scan(self) :
		self.name = raw_input("Entrez le nom de l'ingrédient : ")
		self.quantity = input("Sa quantité : ")
		self.unity = raw_input("Et son unité : ")

	def printer(self) :
		print "{} : {}{}".format(self.name, self.quantity, self.unity)

class Alimentary_Product :
	def __init__(self) :
		self.name = "Unamed"
		self.brand = "No brand"
		self.ref = 0
		self.productionDate = Date()
		self.expirationDate = Date()
		self.ingredients = list()

	def printer(self) :
		print "> Nom : {}\n> Marque : {}\n> Référence : {}\n> Production : {}\n> Expiration : {}\n".format(self.name, self.brand, self.ref, self.productionDate, self.expirationDate)
		print "> Ingrédients :"

		for v in self.ingredients :
			print "\t- ",
			v.printer()

	def scan(self) :
		print "------------------"
		self.name = raw_input("Nom du produit : ")
		self.brand = raw_input("Marque : ")
		self.ref = input("Référence : ")
		self.productionDate.scan()
		self.expirationDate.scan()
		n = input("Combien y a t-il d'ingrédients ? ")

		for i in range(n) :
			ing = Ingredient()
			ing.scan()

			self.ingredients.append(ing)

		print "------------------"

class Store :
	def __init__(self) :
		self.products = list()

	def add(self, p) :
		self.products.append(p)

	def scanProducts(self) :
		n = input("Combien de produits ? ")

		for i in range(n) :
			pro = Alimentary_Product()
			print "Produit {} : ".format(len(self.products) + i + 1)

			pro.scan()
			self.products.append(pro)

	def printer(self) :
		print "EN MAGASIN : "
		for i in range(len(self.products)) :
			print "\n------------------\n"
			print "\tPRODUIT {} : \n".format(i + 1)
			self.products[i].printer()
		print "\n------------------\n"

	def searchByName(self, name) :
		l = ProductList()

		for v in self.products :
			if name.lower() in v.name.lower() :
				l.append(v)

		return l

	def searchByRef(self, ref) :
		l = ProductList()

		for v in self.products :
			if v.ref == ref :
				l.append(v)

		return l

	def searchByIngredientOverflow(self, ingredient, quantity) :
		l = ProductList()

		for v in self.products :
			for e in v.ingredients :
				if ingredient.lower() in e.name.lower() :
					if e.quantity >= quantity :
						l.append(v)

		return l

	def sell(self, toSell) :
		l = ProductList()
		if type(toSell) == str :
			l = self.searchByName(toSell)
		elif type(toSell) == int :
			l = self.searchByRef(toSell)
		else :
			print "Votre demande est impossible :o"
			return

		if len(l) > 1 :
			print "Précisez votre vente ..."
		else :
			self.products.remove(l[0])

	def removeExpired(self, date) :
		for v in self.products :
			if v.expirationDate <= date :
				self.products.remove(v)

	def printerBetween(self, d1, d2) :
		l = ProductList()

		for v in self.products :
			if v.expirationDate <= d2 and v.expirationDate >= d1 :
				l.append(v)

		l.printer()

class ProductList(list) :
	def printer(self) :
		for v in self :
			v.printer()
			print "\n"

class FileReader :
	def __init__(self) :
		self.products = open("objects.txt", "r")
		self.lines = self.file.readlines()

	def getProducts(self) :
		l = ProductList()

		ingredients = open("ingredient.txt", "r")
		lines2 = ingredients.readlines()

		for v in self.lines :
			p = Alimentary_Product()
			a = v.split(",")
			p.name = a[0]
			p.brand = a[1]
			p.ref = int(a[2])
			p.productionDate = Date.format(a[3])
			p.expirationDate = Date.format(a[4])



p1 = Alimentary_Product()
p2 = Alimentary_Product()
p3 = Alimentary_Product()
p4 = Alimentary_Product()

p1.name = "Brownie"
p1.brand = "Isa"
p1.ref = 122211
p1.productionDate = Date(10, 01, 2006)
p1.expirationDate = Date(10, 01, 2007)
p1.ingredients.append(Ingredient("chocolat", 600, "g"))
p1.ingredients.append(Ingredient("oeufs", 4, ""))
p1.ingredients.append(Ingredient("farine", 200, "g"))
p1.ingredients.append(Ingredient("beurre", 250, "g"))

p2.name = "Soupe de légume"
p2.brand = "Bonne maman"
p2.ref = 157948
p2.productionDate = Date(1, 1, 2015)
p2.expirationDate = Date(21, 12, 2017)
p2.ingredients.append(Ingredient("eau", 50, "dL"))
p2.ingredients.append(Ingredient("pommes de terre", 5, ""))
p2.ingredients.append(Ingredient("carottes", 3, ""))
p2.ingredients.append(Ingredient("courgettes", 4, ""))

p3.name = "Soupe de poisson"
p3.brand = "Bonne maman"
p3.ref = 24550
p3.productionDate = Date(10, 12, 2016)
p3.expirationDate = Date(10, 06, 2026)
p3.ingredients.append(Ingredient("poisson", 1, "kg"))
p3.ingredients.append(Ingredient("eau", 40, "cL"))

p4.name = "Crêpes"
p4.brand = "Harrys"
p4.ref = 1702
p4.productionDate = Date(14, 12, 2016)
p4.expirationDate = Date(16, 12, 2016)
p4.ingredients.append(Ingredient("oeufs", 2, ""))
p4.ingredients.append(Ingredient("farine", 300, "g"))
p4.ingredients.append(Ingredient("beurre", 270, "g"))

today = Date(15, 12, 2016)

store = Store()
store.add(p1)
store.add(p2)
store.add(p3)
store.add(p4)

print Date.format("12/12/2012")