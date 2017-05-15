# Napisac funkcje, ktora podany przez uzytkownika tekst rozbije na slowa, a nastepnie uporzadkuje je malejaco wg #     dlugosci.
#   Jesli slowa maja te sama dlugosc to porzadkujemy je w kolejnosci alfabetycznej. 
#   Funkcja zwraca liste uporzadkowanych slow.


def uporzadkuj(text):
	lista = text.split()
	print lista
	i=0
	for x in lista:
		j=0
		for y in lista:
			#print lista[x]
			if len(lista[j])>len(lista[i]):
				lista[j], lista[i] = lista[i], lista[j]
			elif len(lista[j])<len(lista[i]):
				pass
			else: # lista[j] == lista[i]
				if ord(lista[j][0])>ord(lista[i][0]):
					lista[j], lista[i] = lista[i], lista[j] 
				elif ord(lista[j][0])<ord(lista[i][0]):
					pass
				else:
					if ord(lista[j][1])>ord(lista[i][1]):
						lista[j], lista[i] = lista[i], lista[j]
					elif ord(lista[j][1])<ord(lista[i][1]):
						pass
					else:
						pass

			j+=1


		i+=1
	return lista
tekst = str(raw_input("podaj tekst: "))

print uporzadkuj(tekst)
























