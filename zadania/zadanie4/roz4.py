#!/usr/bin/env python
k = int(input("podaj liczbe k "))
plik = input("podaj nazwe pliku ")
jak=True
with open( 'input.txt', "r" ) as f:
    lista = [ line.rstrip( "\n" ) for line in f ]
wyjscie = open(plik+".txt", "w")
for linia in lista:
	for pole in linia.split():
		
		if k<int(pole):
			jak=True
			break
		else:
			jak=False
	if jak:
		wyjscie.write( "tak\n" )
	else:
		wyjscie.write( "nie\n" )



