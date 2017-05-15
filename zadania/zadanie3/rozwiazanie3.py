#!/usr/bin/env python
s = int(input("podaj poczatkowa dlugosc skoku [cm] "))
k = int(input("zaba bedzie odpoczywac jesli [cm] "))
d = int(input("podaj odleglosc do pokoniania przez zabe [m] "))

dd = d * 100
przerwa=False
hop=0
skok = ss = s
i=0
licznik=1
dzielnik=2

while dd:
	if dd<=0:
		break
	hop+=1
	dd-=skok
	#print dd, skok, licznik, dzielnik
	if hop%5==0:
		skok = skok*licznik/dzielnik
		licznik+=1
		dzielnik+=1
	
	if skok<k:
		przerwa=True
		break


if przerwa:
	print ("Nie")
else:
	print ("Tak w", hop-1, "skokach")
