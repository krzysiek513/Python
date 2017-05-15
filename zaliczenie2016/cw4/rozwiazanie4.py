# Napisac funkcje, ktora przeksztalci wprowadzona liczbe dziesietna na jej postac slowna (funkcja powinna #obslugiwac # liczby max pieciocyfrowe).
git = False
while not git:
	licz = raw_input("podaj liczbe od 0 do 99999, gora 5 cyfr: ")
	if len(licz) < 6 and len(licz) > 0:
		git = True
	for i in licz:
		#print i
		if ord(i) < ord("0") or ord(i) > ord("9"):
			git = False


liczba=int(licz)

def slownie(liczba):
	slownie=[]
	if liczba/10000:
		i=int(liczba/10000%10)
		if i==1:
			slownie.append("dziesiec")
		elif i==2:
			slownie.append("dwadziescia")
		elif i==3:
			slownie.append("trzydziesci")
		elif i==4:
			slownie.append("czterdziesci")
		elif i==5:
			slownie.append("piecdziesiat")
		elif i==6:
			slownie.append("szescdziesiat")
		elif i==7:
			slownie.append("siedemdziesiat")
		elif i==8:
			slownie.append("osiemdziesiat")
		else:
			slownie.append("dziewiecdziesiat")
	
	if liczba/1000:
		i=int(liczba/1000%10)
		if i==1:
			slownie.append("jeden tysiecy")
		elif i==2:
			slownie.append("dwa tysiace")
		elif i==3:
			slownie.append("trzy tysiace")
		elif i==4:
			slownie.append("cztery tysiace")
		elif i==5:
			slownie.append("piec tysiacy")
		elif i==6:
			slownie.append("szesc tysiacy")
		elif i==7:
			slownie.append("siedem tysiacy")
		elif i==8:
			slownie.append("osiem tysiacy")
		elif i==9:
			slownie.append("dziewiec tysiacy")
		else:
			slownie.append("tysiacy")
	
	if liczba/100:
		i=int(liczba/100%10)
		if i==1:
			slownie.append("sto")
		elif i==2:
			slownie.append("dwiescie")
		elif i==3:
			slownie.append("trzysta")
		elif i==4:
			slownie.append("czterysta")
		elif i==5:
			slownie.append("piecset")
		elif i==6:
			slownie.append("szescset")
		elif i==7:
			slownie.append("siedemset")
		elif i==8:
			slownie.append("osiemset")
		elif i==9:
			slownie.append("dziewiecset")
		else:
			slownie.append("")
	
	if liczba/10:
		i=int(liczba/10%10)
		if i==1:
			slownie.append("dziesiec")
		elif i==2:
			slownie.append("dwadziescia")
		elif i==3:
			slownie.append("trzydziesci")
		elif i==4:
			slownie.append("czterdziessci")
		elif i==5:
			slownie.append("piecdziesiat")
		elif i==6:
			slownie.append("szescdziesiat")
		elif i==7:
			slownie.append("siedemdziesiat")
		elif i==8:
			slownie.append("osiemdziesiat")
		elif i==9:
			slownie.append("dziewiencdziesiat")
		else:
			slownie.append("")
	
	i=int(liczba%10)
	if i==1:
		slownie.append("jeden")
	elif i==2:
		slownie.append("dwa")
	elif i==3:
		slownie.append("trzy")
	elif i==4:
		slownie.append("cztery")
	elif i==5:
		slownie.append("piec")
	elif i==6:
		slownie.append("szesc")
	elif i==7:
		slownie.append("siedem")
	elif i==8:
		slownie.append("osiem")
	elif i==9:
		slownie.append("dziewiec")
	else: #0
		slownie.append("")

	string=""
	for i in slownie:
		string+=i+" "
	return string

print slownie(liczba)












