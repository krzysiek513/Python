with open( 'input.txt', "r" ) as f:
    lista = [ line.rstrip( "\n" ) for line in f ]
wyjscie = open("output.txt", "w")

#print(lista)
i = 1
for linia in lista:
	#print(linia, i)
	jakasLista = []
	najwieksza = 0
	najwieksze = 0
	duze = 0
	liczby = 0
	if(i%2!=0):
		wyjscie.write( linia+"\n" )
		#print("i%2")
	else:
		#print("-------------")
		for pole in linia.split( " " ):
			#print (pole)
			jakasLista.append(pole)
		for liczba in jakasLista:
			liczby+=1
			if najwieksza==0:
				najwieksza = liczba
			if najwieksza<liczba:
				najwieksza = liczba
			if najwieksza == liczba:
				duze+=1
		for liczba in jakasLista:
			if najwieksza == liczba:
				najwieksze+=1
		#print str(najwieksze) + "<--------------"
		#print liczby
		#print duze
		jakasLista.sort()
		h = najwieksze
		while h:
			h-=1
			if najwieksze != liczby:
				jakasLista.remove(najwieksza)
		
		for k in jakasLista:
			wyjscie.write( k+" ") 			
		wyjscie.write( "\n") 	
	i+=1

