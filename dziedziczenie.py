class rodzice():
	def nazwisko(self):
		print("Jozwikowski")

class dziecko(rodzice):
	def imie(self):
		print("Krzysiek")

obiekt = dziecko()

obiekt.imie()
obiekt.nazwisko()
