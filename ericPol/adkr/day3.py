a = ["aaa", "bb", "bbbbb"]


def filterLongWord(arg, limit):
    return filter(lambda x: True if len(x) > limit else False, arg)

print filterLongWord(a,3)

def maps_list_word_to_list_len(arg):
    pass

#####################
# CLASSES
#####################

class Employee():
    companyName = "MI6"
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.salary = 0
    def getName(self):
        return self.name
    def getSurname(self):
        return self.surname
    def __str__(self):
        return self.name + " " + self.surname
    @classmethod
    def getCompanyName(cls):
        return cls.companyName
        

emp = Employee("James","Bond")
print emp.name," ",emp.surname
print emp.getName()
print emp.getSurname()
print emp
print Employee.getCompanyName()

#####################
# INHERITANCE
#####################

class D(object):
    arg = 20
    pass
class C(D):
    arg = 30
    pass
class B(D):
    pass
class A(B,C):
    pass
a = A()
print a.arg

#####################
# Overload operators
#####################

class A():
    def __init__(self):
        self.lista = [1,2,3,4,5,6,7,8,9,10]

    def __setitem__ (self, index, value):
        self.lista[index] = value

    def __getitem__ (self, index):
        return self.lista[index]

a = A()
print a[0]
print a[1]
print a[2]
a[3] = "a"
a[4] = "b"
print a[3]
print a[4]


#####################
# Iterable class
#####################

class CustomIterable():
    def __init__(self):
        self.licznik = 0
    def __iter__(self):
        return self
    def next(self):
        if self.licznik >= 10:
            raise StopIteration
        self.licznik +=1
        return self.licznik

iterable = CustomIterable()

for i in iterable:
    print i


#####################
# Modifiers
#####################

class Cup():
    arg   = 30
    _arg  = 20
    __arg = 10

c = Cup()

#Public
print c.arg
#Protected - "nie tykaj jesli nie dziedziczysz po"
print c._arg
#Private ale mozna sie dostac za pomoca _ClassName i wtedy private
print c._Cup__arg

#####################
# SUPER keyword
#####################

#super dziala ale musi byc w "nowym stylu" czyli klasa nadrzedna musi dziedziczyc po 'object'
class A(object):
    def fun(self):
        print self
        return "funA"
class B(A):
    def fun(self):
        return super(B, self).fun()

b = B()
print b.fun()
print "____________+==============+______________"
#####################
# YIELD
#####################

def fun():
    licznik = 0
    for i in range(1,10):
        licznik+=1
        yield licznik
a=list(fun())
print a

t=()
print type(t)












