class ZleDane:
    pass
try:
    wzrost1 = int(input("Wzrost1 [cm] = "))
    if wzrost1 <=0 or wzrost1 >=300:
        raise ZleDane
    wzrost2 = int(input("Wzrost2 [cm] = "))
    if wzrost2 <=0 or wzrost2 >=300:
        raise ZleDane
    wspol1  = float(input("Wspolczynnik1 [%] = "))
    if wspol1 < 0 or wspol1 > 100:
        raise ZleDane
    wspol2  = float(input("Wspolczynnik2 [%] = "))
    if wspol2 < 0 or wspol2 > 100:
        raise ZleDane
except ZleDane:
   print("Zla wartosc")
except:
    print("Podane dane sa bledne")

if wzrost1 > wzrost2:
    tmpWzrost = wzrost1
    tmpWspol  = wspol1
    wzrost1   = wzrost2
    wspol1    = wspol2
    wzrost2   = tmpWzrost
    wspol2    = tmpWspol
elif wzrost1==wzrost2 and wspol1<wspol2 :
    tmpWspolczynnik = wspol1
    wspol1 = wspol2
    wspol2 = tmpWspolczynnik
    
czyPrzekroczy = False
lata     = 0
miesiace = 1

for i in range(7, 18, 1):
    for j in range(1,13,1):
        wzrost1 += ( wzrost1 * wspol1 ) / 100
        wzrost2 += ( wzrost2 * wspol2 ) / 100
        if wzrost1 > wzrost2:
            czyPrzekroczy = True
            break
        miesiace += 1
    if czyPrzekroczy == True:
        break
    lata += 1
    miesiace = 1
    
if czyPrzekroczy == True:
    print("Tak, lata:" , lata ,"miesiace:", miesiace)
else:
    print("Nie")




