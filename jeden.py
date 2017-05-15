#!/usr/bin/env python
a = 'Witaj w swiecie Pythona'
print (a[3])
print (a[0:15])

c = 'Witaj w swiecie Pythona'
b = ' w 2007 roku'
print (c + b)

d = 'Witaj w swiecie Pythona'
e = ' w 2006 roku. Szczesliwy numerek to: '
f = 13
print (d + e + str(f))
print (d + e + repr(f))

g = 2
h = 5
print (g+h)
print (g*h)
print (g/h)
print(g%h)

i = 2.0
j = 5.0
wynik = i/j
poczatek = "Wynik dzielenia wynosi:"
koniec = "co bylo oczekiwane"
print ("%s %f %s" % (poczatek, wynik, koniec))
