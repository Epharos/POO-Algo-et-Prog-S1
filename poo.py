#!/usr/bin/python2.7
#coding:utf-8

from math import *

class Point :
	def __init__(self) :
		self.x = 0.0
		self.y = 0.0
		self.z = 0.0

	def printer(self) :
		print "({}, {}, {})".format(self.x, self.y, self.z)

	def setPosition(self, x, y, z) :
		self.x = x
		self.y = y
		self.z = z

	def inputs(self) :
		self.x = input("x = ")
		self.y = input("y = ")
		self.z = input("z = ")

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

	def test(self) :
		for i in range(len(self.points) - 1) :
			print self.points[i].inf_or_equal(self.points[i + 1])


c = Collection()

for i in range(3) :
	p = Point()
	p.inputs()
	c.add(p)


print ""

c.printer()

print ""

c.centerOfGravity().printer()

print ""

c.sort()
c.printer()

print ""

c.test()