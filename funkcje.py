#!/usr/bin/env python
def n1asza_funkcja(argument1, argument2):
 argumenty = argument1+" - "+argument2
 return ( argumenty, 3 )

print (n1asza_funkcja("tak", "pewnie"))

def nasza_funkcja(argument1, argument2 = "Koniec"):
 global a
 argumenty = argument1+" - "+argument2
 a = 1
 return argumenty

print (nasza_funkcja("Poczatek"))
print (a)
