######################################################
# Class
######################################################
import sys
import random
#print sys.argv[1]

#ord()
#chr()

class Osoba:
    pass

class Employee(Osoba):

    company_name = "EricPol"
    
    def __init__(self, name, surname="grajacy", los="0", wins=0):
        self.name = name
        self.surname = surname
        self.salary=random.randint(1,1111)
        self.los=los
        self.winner=wins
        
    def __str__(self):
        return self.name + " " + self.surname
    
    def increa_salary(self,salary):
        self.salary += salary
        
    def decrease_salary(self,salary):
        self.salary -= salary
        
    def get_salary(self):
        return self.salary
    
    @classmethod #dekoratory
    def get_company_name(cls):
        return cls.company_name
    
    pass

emp = Employee("Alice","Spring")
print emp
emp.increa_salary(1000)
print emp.get_salary()
print Employee.get_company_name()



class A():
    def __init__(self):
        self.lista = [ z for z in range(1,10)]

    def __getitem__(self,index):
        return self.lista[index]

    def __setitem__(self,index,value):
        self.lista[index]=value

a=A()


print a[0]
print a[1]
print a[2]

a[0]=3
a[1]=7
a[2]=67

print a[0]
print a[1]
print a[2]


#######################################################
# Zad 8
#######################################################
#ruletka

#a1 = str(raw_input("podaj imie pierwszego gracza: ")
#a2 = raw_input("podaj imie drugiego gracza: ") # jest typu str

lista_graczy=[]
liczba_graczy=0
for x in range(liczba_graczy):#int(sys.argv[1])):
    lista_graczy.append(Employee(raw_input("podaj imie gracza: ")))
#player2 = Employee(raw_input("podaj imie drugiego gracza: "))

#print sys.argv[1]
#print sys.argv[2]
gry=0#int(sys.argv[2])
while(gry):
    gry-=1
    for x in range(liczba_graczy):
        print lista_graczy[x].name,
        git = False
        while not git:
            lista_graczy[x].los=raw_input("podaj los gracza Z PRZEDZIALU [1-2]: ")
            if ord(lista_graczy[x].los[0])==49 or ord(lista_graczy[x].los[0])==50:
                git = True
            else:
                git = False

    losowanie = random.randint(1,2)
    print losowanie
    print ord("1")
    for x in range(liczba_graczy):
        if losowanie==lista_graczy[x].los:
            lista_graczy[x].winner+=1

            
#najlepszy=lista_graczy[0]
for x in range(liczba_graczy):
    #najlepszy=lista_graczy[x]
    if najlepszy.winner<lista_graczy[x].winner:
        najlepszy = lista_graczy[x]

#print najlepszy




#######################################################
# Generators
#######################################################

seasons = ["zima","lato","wiosna","jesien"]

print list(enumerate(seasons))

def custom_enumerate(seasons):
    lista=[]
    for x in seasons:

        lista.append(x)

    return lista


print custom_enumerate(seasons)   

def custom_enumerate(sq, start =0):
    n=start
    for x in sq:
        yield n,x
        n+=1
    

#######################################################
# Kolekcje
#######################################################

class Container:

    def __init__(self):
        self.licznik=0

    def __inter__(self):
        return self

    def next(self):
        if self.licznik>=10:
            raise StopIteration
        self.licznik+=1
        return self.licznik
    
    pass

a = Container()

for i in a :
    print i



























