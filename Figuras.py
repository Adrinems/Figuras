#!/usr/bin/env python

class Figuras():
	def area_cuadrado(self, l):
		return l*l

	def area_circulo(self, r): 
		area = ((r**2) * 3.1416)
		return  round(area,2)

	def area_rectangulo(self, b, a):
		return (a*b)

	def area_triangulo(self, a, b):
		return ((a*b) / 2)

	def area_octagono(self, a, l):
		perimetro = l*8
		return (perimetro*a/2)

	def esfigura(self, figura):
		if figura == "Cuadrado":
			return "Cuadrado"
		elif figura == "Circulo":
			return "Circulo"
		elif figura == "Triangulo":
			return "Triangulo"
		elif figura == "Rectangulo":
			return "Rectangulo"
		elif figura == "Octagono":
			return "Octagono"
