import listy_sortowane
import dziekanat

studenci = listy_sortowane.Lista()
for spec in ("GRA", "SID"):
    try:
        we = open(spec + ".txt", "r")
    except:
        print("Nie znaleziono pliku", spec + ".txt")
    else:
        for linia in we: #ptla obsugi kolejnych linii w pliku
            try:
                osoba = dziekanat.Student(linia)
            except dziekanat.Student.BrakDanych:
                print("Brak wymaganych danych:", linia)
            except dziekanat.Student.NiepoprawnyIndeks:
                print("Niepoprawny numer indeksu:", linia)
            except dziekanat.Student.NiepoprawnaOcena: 
                print("Niepoprawna ocena:", linia)                
            else:
                try:
                    studenci.wstaw(osoba)
                except listy_sortowane.Lista.Pelna:
                    #Uwaga: Na ocen 4 bd przepeienia listy nie moe zosta zgoszony.
                    print("Lista pelna")
        we.close()
    
if not studenci.czyPusta():
    wy = open("INF.txt", "w")
    while(True): #petla obsugi kolejnych elementow w linijcie
        try:
            osoba = studenci.pobierz()
            wy.write(osoba.indeks() + ";" + osoba.ocena() + ";" + osoba.nazwisko() + " " + osoba.inicjaly() + "\n")
        except listy_sortowane.Lista.Pusta:
            break
    wy.close()
    
# na ocen 5 - pocztek #############################################
for i in range(int(input("Podaj ilu studentw wyszuka:"))):
    try:
        osoba = dziekanat.znajdz("INF.txt", int(input("Podaj indeks:")))
    except dziekanat.NieznanyIndeks:
        print("Szukany student nie znajduje sie w bazie")
    else:
        studenci.wstaw(osoba)
        
while not studenci.czyPusta():
    print(studenci.pobierz())
# na ocen
