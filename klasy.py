#!/usr/bin/env python
class koszyk:
	def __init__ (self):
		self.koszyk = []
	def dodaj(self,obiekt):
		self.koszyk.append(obiekt)
	def rozmiar(self):
		return len(self.koszyk)

s = koszyk()
print (s.rozmiar())
s.dodaj("pierwszy wpis")
s.dodaj("drugi wpis")
print (s.rozmiar())
del s
