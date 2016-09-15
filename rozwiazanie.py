#!/usr/bin/env python

def ile_znakow(tekst):

	a=set(tekst)
	return len(a)


tekst1 = str(raw_input("podaj tekst: "))


print ile_znakow(tekst1)
