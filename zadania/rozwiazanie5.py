# Napisac funkcje, ktora dostaje dwie nazwy miesiecy i sprawdza, ile miesiecy mija od pierwszego do drugiego z #nich.  
# Jesli drugi jest wczesniejszy niz pierwszy, zakladamy, ze jest on w nastepnym roku.
rok={
    "styczen":1,
    "luty":2,
    "marzec":3,
    "kwiecien":4,
    "maj":5,
    "czerwiec":6,
    "lipiec":7,
    "sierpien":8,
    "wrzesien":9,
    "pazdziernik":10,
    "listopad":11,
    "grudzien":12,
    }
bar2 = {"imie" : "jurek", "nazwisko" : "lepper"}

def miesiace(start, koniec):
    a = 1
    pocz = (rok[start])
    kon = (rok[koniec])
    for i in range(pocz, kon):
	    a = a + 1

    print(a)

pierwszy = input("Podaj 1 miesiac ")
drugi = input("Podaj 2 miesiac ")

miesiace(pierwszy, drugi)