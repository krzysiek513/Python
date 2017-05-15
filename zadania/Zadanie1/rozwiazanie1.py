#!/usr/bin/env python
wzrost1 = int(input("podaj wzrost pierwszego chlopaka: "))

wzrost2 = int(input("podaj wzrost drugiego chlopaka: "))

wspolczynnik1 = float(input("podaj wspolczynnik pierwszego chlopaka: "))

wspolczynnik2 = float(input("podaj wspolczynnik drugiego chlopaka: "))

i = 1	
rowne = False
przerosnie = False

if wzrost1 > wzrost2:
	#print wzrost1
	wzrostDuzy = wzrost1
	wzrostMaly = wzrost2
	wspolczynnikW = wspolczynnik2
	wspolczynnikN = wspolczynnik1
	if wspolczynnik2 > wspolczynnik1:
		przerosnie = True
elif wzrost1 < wzrost2:
	#print wzrost2
	wzrostDuzy = wzrost2
	wzrostMaly = wzrost1
	wspolczynnikW = wspolczynnik1
	wspolczynnikN = wspolczynnik2
	if wspolczynnik1 > wspolczynnik2: 
		przerosnie = True
else:
	rowne = True
	wzrostDuzy = " Rowne "
	wzrostMaly = " Rowne "
	if wspolczynnik1 != wspolczynnik2:
		przerosnie = True
		
if przerosnie:
	if rowne:
		print ("Tak, miesiace: 1")
	else:
		while wzrostDuzy > wzrostMaly:
			wzrostMaly = wzrostMaly + float(wzrostMaly * wspolczynnikW)
			wzrostDuzy = wzrostDuzy + float(wzrostDuzy * wspolczynnikN)		
			i = i + 1
			print( wzrostMaly)
			print (wzrostDuzy)
			if i == 132:
				break
		print( "Tak, lata:", i/12,"miesiace:",i%12-1)
else:
	print ("Nie")
