licznik = 10
wartosc = 15

while licznik <= wartosc:
		licznik += 1
		print ("Jestem w while.")


print ("petle for")
for i in range(10):
	print (i)

print ("Petla 2:")
for i in range(3, 5):
	print (i)

print ("Petla 3:")
for i in range(10, 100, 10):
	print (i)

print ("bar")
bar1 = "Zdrabniamy literki"
for i in bar1:
	print (i)

bar1 = ["foo", "bar", "yaz"]
for i in bar1:
	print (i)

bar2 = {"imie" : "jurek", "nazwisko" : "lepper"}
print (bar2["imie"])

for i in bar2:
	print (i + " - " +bar2[i])


bar = {
	"imie" : "adam",
	"nazwisko" : "ewa"
	 }

lista = bar.keys()
for i in lista:
	print( i)

del bar["imie"]
#print bar

lista = bar.keys()
for i in lista:
	print (i)


