#!/usr/bin/env python
import unittest
from Figuras import Figuras

class TestCase(unittest.TestCase):

	def test_cuadrado_5(self):
		fig = Figuras()
		self.assertEquals("Cuadrado", fig.esfigura("Cuadrado"))
		self.assertEquals(25, fig.area_cuadrado(5))

	def test_cuadrado_76(self):
		fig = Figuras()
		self.assertEquals("Cuadrado", fig.esfigura("Cuadrado"))
		self.assertEquals(5776, fig.area_cuadrado(76))

	def test_cuadrado_18(self):
		fig = Figuras()
		self.assertEquals("Cuadrado", fig.esfigura("Cuadrado"))
		self.assertEquals(324, fig.area_cuadrado(18))

	def test_circulo_4(self):
		fig = Figuras()
		self.assertEquals("Circulo", fig.esfigura("Circulo"))
		self.assertEquals(50.27, fig.area_circulo(4))

	def test_circulo_10(self):
		fig = Figuras()
		self.assertEquals("Circulo", fig.esfigura("Circulo"))
		self.assertEquals(314.16, fig.area_circulo(10))

	def test_circulo_8_9(self):
		fig = Figuras()
		self.assertEquals("Circulo", fig.esfigura("Circulo"))
		self.assertEquals(248.85, fig.area_circulo(8.9))

	def test_rectangulo_4_3(self):
		fig = Figuras()
		self.assertEquals("Rectangulo", fig.esfigura("Rectangulo"))
		self.assertEquals(12, fig.area_rectangulo(4,3))

	def test_rectangulo_8_2_10(self):
		fig = Figuras()
		self.assertEquals("Rectangulo", fig.esfigura("Rectangulo"))
		self.assertEquals(82, fig.area_rectangulo(8.2,10))

	def test_rectangulo_15_6(self):
		fig = Figuras()
		self.assertEquals("Rectangulo", fig.esfigura("Rectangulo"))
		self.assertEquals(90, fig.area_rectangulo(15,6))

	def test_triangulo_3_4(self):
		fig = Figuras()
		self.assertEquals("Triangulo", fig.esfigura("Triangulo"))
		self.assertEquals(6, fig.area_triangulo(3,4))

	def test_triangulo_24_11(self):
		fig = Figuras()
		self.assertEquals("Triangulo", fig.esfigura("Triangulo"))
		self.assertEquals(132, fig.area_triangulo(24,11))

	def test_triangulo_28_33(self):
		fig = Figuras()
		self.assertEquals("Triangulo", fig.esfigura("Triangulo"))
		self.assertEquals(462, fig.area_triangulo(28,33))

	def test_octagono_4_6(self):
		fig = Figuras()
		self.assertEquals("Octagono", fig.esfigura("Octagono"))
		self.assertEquals(96, fig.area_octagono(4,6))

	def test_octagono_7_10(self):
		fig = Figuras()
		self.assertEquals("Octagono", fig.esfigura("Octagono"))
		self.assertEquals(280, fig.area_octagono(7,10))

	def test_octagono_9_15(self):
		fig = Figuras()
		self.assertEquals("Octagono", fig.esfigura("Octagono"))
		self.assertEquals(540, fig.area_octagono(9,15))


if __name__ == '__main__':
	unittest.main()
