# -*- coding: utf-8 -*-
########################
# Primitive data types 
########################

a = 1
print type(a)
b = "1"
print type(b)
c = 1.0
print type(c)
d = 2 + 3j
print type(d)
########################
#funkcje dla a
print dir(a)
#potegowanie -> **
print 2**38
#manual dla funkcji str
print help(str)

########################
# Tuple
########################
#immutable czyli nie mozna jej zmienic po utworzeniu
a = (1,2,3,4,5)
print a
print type(a)
#a[0] = 4
#odwolanie sie do pierwszego elementu tupli
print a[0]
#inne tworzenie tupli (bez () )
a = 1,2,3,4,5
print type(a)
#tupla jedno elementowa
b = 1,
print type(b)

#switch(a,b)
a = 1
b = 2
print a
print b
a,b = b,a
print a
print b

########################
# List
########################
a = [1,2,3,4,5]
print type(a)
print a
a[0] = 6
print a
a.append(7)
print a
print dir(a)
a.insert(1,10)
print a
a.insert(0,"jestem sobie string na poczatku listy intow")
print a
#z lewej domkniety zakres
a = range(1,100,3)
print a
print 3/10.0
print [x * 0.1 for x in range(0,10)]

a = [1,2,3,4,5,6,7,8,9,10]
#te dwukropki to slice czyli od 2(including) do 7(excluding) co 2
print a[2:7:2]
#domyslny krok 1
print a[-1:-4:-1]
print a[-4:-1]
#odwracamy stringa
a = "sample"
print a[::-1]
print a[-1::-1]


########################
# Set
########################

a = set([1,2,3,4,5])
print type(a)
print a
a.add(5)
print a
# a = set([1,2,3,[1,2,3],5]) nie mozna dodac listy - jest mutable czyli nie ma wlasnego unikalnego identyfikatora
a = {1,2,3,4,5}
#sprawdzamy czy 4 jest w zbiorze
print 4 in a

a = frozenset([1,2,3,4,5])
# a.add(5)


########################
# Map
########################
#kluczem musza byc elementy immutable (niezmienne)
a = {
    (1,2,3):1,
    "b":2,
    "c":3
    }
#odwalanie wg tupli
print a[(1,2,3)] 
print a.keys()
print a.values()
print a
del a["b"]
print a


########################
# Loop
########################

myList  = [1,2,3,4,5]
newList = []

#classic way

for x in myList:
    newList.append(x*2)
print  newList
#else: (optional) kiedy wykona sie petla bez break to sie wykona else
#python way

newList = [x*2 for x in myList]
print newList

# ZADANIE 0

help(str)
help(list)

# ZADANIE 1

a = "She sells sea shells"
print " ".join(a.split()[::-1])

########################
# if else
########################

if 1<2:
    print "ok"
else:
    print "not ok"

#Komentarz wielolinijkowy
"""
To jest
komentarz
wielolinijkowy
"""
import sys
print sys.getdefaultencoding()

if False:
    print "ok"
else:
    print "not ok"

#pass pozwala na nie konczenie funkcji, czyli nic nie robi, ale pozwala na uruchomienie skryptu
if 1<2:
    pass

# ZADANIE 3
a = 1232323232323232121321321321321321321321321321321321
print len(set(str(a)))

# ZADANIE 2
zdanie = "Eve has a cat"
dic = {
    "2" : "abc",
    "3" : "def",
    "4" : "ghi",
    "5" : "jkl",
    "6" : "mno",
    "7" : "pqrs",
    "8" : "tuv",
    "9" : "wxyz",
    "#" : " "
    }
b = " "
c = ""
for litera in zdanie.lower(): # dla kazdej litery w zdaniu
    for tup in dic.items(): #dla kazdej pary klawisz - litery w klawiszu
        if litera in tup[1]: #jesli litera z zdania jest w klawiszu
            index = tup[1].index(litera)+1 #znajdz index litery w stringu klawisza
            c += str(tup[0])*index #wyswietl tyle razy klawisz jaki jest index

print c

# ZADANIE 4

stackXeqY   = []
stackXlessY = []
stackOther  = []
for x in range(1, 7):
    for y in range(1, 7):
        a = x,y
        if x<y:
            stackXlessY.append(a)
        elif x == y:
            stackXeqY.append(a)
        else:
            stackOther.append(a)

print "X == Y: ",stackXeqY
print ""
print "X <  Y: ",stackXlessY
print ""
print "X >  Y: ",stackOther
print ""
sumaX = 0
sumaY = 0
while stackXeqY:
    a = stackXeqY.pop()
    sumaX += a[0]
    sumaY += a[1]
print "X=Y:\nSuma X = ",sumaX,"\nSuma Y = ",sumaY

sumaX = 0
sumaY = 0
while stackXlessY:
    a = stackXlessY.pop()
    sumaX += a[0]
    sumaY += a[1]
print "X<Y:\nSuma X = ",sumaX,"\nSuma Y = ",sumaY

sumaX = 0
sumaY = 0
while stackOther:
    a = stackOther.pop()
    sumaX += a[0]
    sumaY += a[1]
print "X>Y:\nSuma X = ",sumaX,"\nSuma Y = ",sumaY,"\n"

print "X == Y: ",stackXeqY
print ""
print "X <  Y: ",stackXlessY
print ""
print "X >  Y: ",stackOther
print ""

# ZADANIE 5

zdanie = "kajak kajak"
print "Jest to palindrom" if zdanie.lower().replace(" ","")[:len(zdanie.lower().replace(" ",""))/2-1:-1]==zdanie.lower().replace(" ","")[:len(zdanie.lower().replace(" ",""))/2] else "Nie jest to palindrom"
"""
zdanie = zdanie.lower().replace(" ","")
if zdanie[:len(zdanie)/2-1:-1]==zdanie[:len(zdanie)/2]:
    print "Jest to palindrom"
else:
    print "Nie jest to palindrom"
"""


# Python Challenge 2
zdanie = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
zdanie = "map"
zdanie2 = ""
for x in zdanie:
    if x == "y":
        zdanie2 += "a"
    elif x == "z":
        zdanie2 += "b"
    elif x == ".":
        zdanie2 += "."
    elif x == "'":
        zdanie2 += "'"
    elif x == "(":
        zdanie2 += "("
    elif x == ")":
        zdanie2 += ")"
    else:
        a=ord(x)
        a = a+2
        if x != " ":
            zdanie2 += chr(a)
        else:
            zdanie2 += " "
print zdanie2






















