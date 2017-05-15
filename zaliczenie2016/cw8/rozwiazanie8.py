#   Napisac funkcje, ktora z zestawu par postaci (imie i nazwisko, ocena) opisujacych oceny uczniow, 
#   wybierze i zwroci liste tych uczniow, ktorzy spelniaja zadane kryterium dotyczace oceny np.ocena = 4. 
#   Lista uczniow oraz kryterium wyboru powinny byc parametrami funkcji.

def krytegia(studenci,kry):
	lista_kry=[]
	for i in studenci:
		if i.ocena == kry:
			lista_kry.append(i)
	return lista_kry
	
	

class Uczen():

    def __init__(self, name, surname, ocena=0):
        self.name = name
        self.surname = surname
        self.ocena = ocena
        
    def __str__(self):
        return self.name + " " + self.surname + " " + str(self.ocena)
    
    def increa_ocena(self,ocena):
        self.ocena += ocena
        
    def decrease_ocena(self,ocena):
        self.ocena -= ocena
        
    def get_ocena(self):
        return self.ocena

c=int(raw_input("podaj liczbe uczniow: "))
lista_uczniow=[]
while(c):
	lista_uczniow.append(Uczen(raw_input("imie? "),raw_input("nazwisko? "),int(raw_input("ocena? "))))
 	c-=1

for i in lista_uczniow:
	print i

#kryterium = int(raw_input("Kryterium? "))


for i in krytegia(lista_uczniow,raw_input("Kryterium? ")):
	print i


























