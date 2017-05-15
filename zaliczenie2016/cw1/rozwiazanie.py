#!/usr/bin/env python
from math import sqrt
'''
def zakres(malo,duzo):
	liczby=[]
	while malo<>duzo+1:
		liczby.append(malo)
		malo+=1
	return liczby

'''

nLista = []

def nLiczby(nLiczbaOd, nLiczbaDo):
    for i in range(nLiczbaOd, nLiczbaDo):
       for x in range(2,i):
           if (i % x) == 0:
               break
       else:
           nLista.append(i)


start = int(raw_input("podaj poczatek przedzialu: "))
stop = int(raw_input("podaj koniec przedzialu: "))

nLiczby(start, stop)
	
wyjscie = open("output.txt", "w")
for liczba in nLista:	
	wyjscie.write(str(liczba)+" ")
