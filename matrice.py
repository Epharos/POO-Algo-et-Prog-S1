#!/usr/bin/python2.7
#coding:utf-8

import random

class Matrix2D :
	def __init__(self, height, width, v = 0) :
		self.width = width
		self.height = height

		self.matrix = []

		self.fill(v)
		
	def fill(self, v = 0) :
		for i in range(self.width) :
			temp = []

			for j in range(self.height) :
				temp.append(v)

			self.matrix.append(temp)

	def input(self) :
		for i in range(self.width) :
			for j in range(self.height) :
				self.matrix[i][j] = input("Entrez une valeur pour la position ({} ; {}) : ".format(j, i))

	def printer(self) :
		for i in range(self.width) :
			for j in range(self.height) :
				print self.matrix[i][j],

			print ""

	def dim(self) :
		return self.width, self.height

	def randomize(self) :
		for i in range(self.width) :
			for j in range(self.height) :
				self.matrix[i][j] = random.uniform(-1, 1)

	def __add__(self, B) :
		w1, h1 = self.dim()
		w2, h2 = B.dim()

		temp = Matrix2D(w1, h1)

		if w1 != w2 and h1 != h2 :
			print "Dimensions différentes !"
			#exit()
			return

		for i in range(w1) :
			for j in range(h1) :
				temp.matrix[i][j] = self.matrix[i][j] + B.matrix[i][j]

		return temp

	def scalar(self, k) :
		for i in range(self.width) :
			for j in range(self.height) :
				self.matrix[i][j] *= k

	def __mul__(self, B) :
		w1, h1 = self.dim()

		if type(B) == int or type(B) == float or type(B) == long:
			out = Matrix2D(w1, h1)
			out.matrix = self.copy()
			out.scalar(B)
			return out
		elif isinstance(B, self.__class__) :
			w2, h2 = B.dim()

			if w1 != h2 :
				print "Dimensions incorrectes !"
				#exit()
				return

			out = Matrix2D(w2, h1)

			for i in range(w2) :
				for j in range(h1) :
					value = 0

					for k in range(w1) :
						value += self.matrix[k][j] * B.matrix[i][k]

					out.matrix[i][j] = value

			return out
		return 

	def transpose(self) :
		temp = Matrix2D(self.width, self.height)

		for i in range(self.width) :
			for j in range(self.height) :
				temp.matrix[j][i] = self.matrix[i][j]

		self.width, self.height = self.height, self.width
		self.matrix = temp.matrix

	def power(self, n) :
		if n < 1 :
			print "n doit être supérieur à 0"
		elif n > 1 :
			m = Matrix2D(self.height, self.width)
			m.matrix = self.copy()

			for i in range(n - 1) :
				m = m.mul(self)

			self.matrix = m.copy()

	def copy(self) :
		return list(self.matrix)

class Identity(Matrix2D) :
	def __init__(self, size) :
		Matrix2D.__init__(self, size, size)

		for i in range(size) :
			self.matrix[i][i] = 1


m = Matrix2D(input("Largeur : "), input("Hauteur : "))
m.input()
m.printer()

print m.__class__

# print ""

# o = m * 3

# o.printer()

