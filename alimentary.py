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
	def formatDate(date) :
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
		self.productionPlace = "Unknown"

	def printer(self) :
		print "> Nom : {}\n> Marque : {}\n> Référence : {}\n> Production : {}\n> Expiration : {}\n> Lieu de production : {}\n".format(self.name, self.brand, self.ref, self.productionDate, self.expirationDate, self.productionPlace)
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
		self.productionPlace = raw_input("Lieu de production : ")
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
		elif type(toSell) == int or type(toSell) == long :
			l = self.searchByRef(toSell)
		else :
			print "Votre demande est impossible :o"
			return

		if len(l) > 1 :
			print "Voulez-vous vraiment acheter {} produits ?".format(len(l))

			r = raw_input("O = Oui ; N = Non : ")
			while r.lower() != 'o' and r.lower() != 'n' :
				r = raw_input("O = Oui ; N = Non : ")

			if r.lower() == 'o' :
				for e in l :
					self.products.remove(e)
			else :
				print "Soyez plus précis la prochaine fois ;)"
				return
		else :
			self.products.remove(l[0])

		print "Merci de votre achat !"

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
	def getProducts(self) :
		l = ProductList()

		file = open("products.txt", "r")
		lines = file.readlines()

		for v in lines :
			if v[0] == "!" or len(v) == 1 :
				continue

			p = Alimentary_Product()
			a = v.split(",")
			p.name = a[0]
			p.brand = a[1]
			p.ref = int(a[2])
			p.productionDate = Date.formatDate(a[3])
			p.expirationDate = Date.formatDate(a[4])
			p.productionPlace = a[5]
			b = a[6].split(";")

			if len(b) % 3 != 0 :
				print "Une erreur est survenue sur les ingrédients"
				file.close()
				return

			for i in range(len(b) / 3) :
				p.ingredients.append(Ingredient(b[3 * i], b[3 * i + 1], b[3 * i + 2]))

			print "Lecture finie : "
			p.printer()
			l.append(p)
			print "\n\n"

		return l

today = Date(15, 12, 2016) #Pensez à changer cette date !

store = Store()
fr = FileReader()

for e in fr.getProducts() :
	store.add(e)

store.sell(raw_input("Que voulez-vous acheter ? "))

store.printer()