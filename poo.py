#!/usr/bin/python2.7
#coding:utf-8

from math import *
import os

class Point :
	def __init__(self) :
		self.x = 0.0
		self.y = 0.0
		self.z = 0.0
		self.name = ""

	def printer(self) :
		print "{}({}, {}, {})".format(self.name, self.x, self.y, self.z)

	def setPosition(self, x, y, z) :
		self.x = x
		self.y = y
		self.z = z

	def inputs(self) :
		self.x = input("x = ")
		self.y = input("y = ")
		self.z = input("z = ")
		self.name = raw_input("Nom : ")

	def input(self) :
		value = raw_input("Coordonnées N(x, y, z) : ")

		if not "(" in value or not ")" in value :
			print "Erreur de mise en forme (parenthèse manquante)"
			return

		if value.index("(") > value.index(")") :
			print "Erreur de mise en forme (place des parenthèses)"
			return

		if len(Util.stringIndexesOf(value, "(")) > 1 or len(Util.stringIndexesOf(value, ")")) > 1 :
			print "Erreur de mise en forme (nombre de parenthèses)"
			return

		self.name = value.split("(")[0]

		value = value[len(self.name):]

		value = value.replace("(", "")
		value = value.replace(")", "")
		value = value.replace(" ", "")

		values = value.split(",")

		if len(values) == 1 :
			self.x = float(values[0])
			self.y = float(values[0])
			self.z = float(values[0])
			return
		elif len(values) != 3 :
			print "N'y a t-il pas un problème ?"
			return

		self.x = float(values[0])
		self.y = float(values[1])
		self.z = float(values[2])

	def inf_or_equal(self, p) :
		if self.x < p.x :
			return 1
		elif self.x == p.x :
			if self.y < p.y :
				return 1
			elif self.y == p.y :
				if self.z <= p.z :
					return 1

		return 0

	def range(self, p) :
		return sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2 + (self.z * p.z) ** 2)

	def belongsTo(self, c) :
		for p in c.points :
			if self.range(p) < 0.00001 :
				return 1

		return 0

#-----

class Collection :
	def __init__(self) :
		self.points = list()

	def add(self, p) :
		self.points.append(p)

	def printer(self) :
		print "La collection comporte {} points :".format(len(self.points))

		for p in self.points :
			p.printer()

	def intersect(self, c) :
		cp = Collection()

		for p in self.points :
			if p.belongsTo(c) :
				cp.add(p)

		return cp

	def centerOfGravity(self) :
		cog = Point()

		x, y, z = 0, 0, 0

		for p in self.points :
			x += p.x
			y += p.y
			z += p.z

		size = len(self.points)

		x /= size
		y /= size
		z /= size

		cog.setPosition(x, y, z)

		return cog

	def maximumIndex(self) :
		index = 0

		for i in range(len(self.points)) :
			if self.point[index].inf_or_equal(self.points[i]) :
				index = i

		return index

	def maximumIndexInRange(self, a) :
		index = 0

		for i in range(a) :
			if self.points[index].inf_or_equal(self.points[i]) :
				index = i

		return index

	def sort(self) :
		for i in range(len(self.points) - 1, -1, -1) :
			maxIndex = self.maximumIndexInRange(i + 1)
			self.points[maxIndex], self.points[i] = self.points[i], self.points[maxIndex]

	def sorted(self) :
		for i in range(len(self.points) - 1) :
			if not self.points[i].inf_or_equal(self.points[i + 1]) :
				return 0

		return 1

	def extends(self, c) :
		if not self.sorted() or not c.sorted() :
			print "Au moins une des collections n'est pas triée !"
			return 

		i, j = 0, 0
		l3 = list()

		while len(l3) < len(self.points) + len(c.points) :
			if i >= len(self.points) :
				l3.append(c.points[j])
				j += 1
				continue
			elif j >= len(c.points) :
				l3.append(self.points[i])
				i += 1
				continue

			if(c.points[j].inf_or_equal(self.points[i])) :
				l3.append(c.points[j])
				j += 1
			else :
				l3.append(self.points[i])
				i += 1

		self.points = list(l3)

#-----

class Util :
	@staticmethod
	def stringIndexesOf(string, char) :
		pos = list()

		for i in range(len(string)) :
			if string[i] == char :
				pos.append(i)

		return pos

	@staticmethod
	def clear() :
		os.system("clear")

#-----

class Vector2D :
	def __init__(self, x, y) :
		self.x = x
		self.y = y

	def normalize(self) :
		return sqrt(self.getX() ** 2 + self.getY() ** 2)

	def getX(self) :
		return self.x

	def getY(self) :
		return self.y

	def printer(self) :
		print "({}, {})".format(self.getX(), self.getY())

	@staticmethod
	def addVectors(v) :
		x, y = 0, 0

		for i in v :
			x += i.getX()
			y += i.getY()

		return Vector2D(x, y)

	def translate(self, p) :
		np = Point()

		np.setPosition(p.x + self.getX(), p.y + self.getY(), 0)

		return np

	def equals(self, v) :
		o = Point()
		p1 = self.translate(o)
		p2 = v.translate(o)

		p1.printer()
		p2.printer()

		print p1.range(p2)

		if p1.range(p2) < 0.5 :
			return 1

		return 0

#-----

class Character :
	def __init__(self, v) :
		self.vectors = list(v)

	def setChar(self, char) :
		self.value = char

	def getValue(self) :
		return Vector2D.addVectors(self.vectors)

#-----

Util.clear()

one = Character([Vector2D(1, 1), Vector2D(0, -3)])
one.setChar("1")

test = Character([Vector2D(0.94, 0.98), Vector2D(-0.02, -2.8)])

one.getValue().printer()
test.getValue().printer()

print one.getValue().equals(test.getValue())

print 