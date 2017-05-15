#**tuple
#*listy



###################################################
# zad 6
###################################################

#a = str(raw_input("podaj pierwsza liczb: "))
#b = str(raw_input("podaj druga liczbe: "))
#print dir(str)
#c=a[::-1]
#d=b[::-1]
#print c, d
#e=int(c)+int(d)
#h=str(int(a[::-1])+int(b[::-1]))


###### rozwiazanie ------> print str(int(str(raw_input("podaj pierwsza liczb: "))[::-1])+int(str(raw_input("podaj druga liczbe: "))[::-1]))[::-1]


###################################################
# Functions
###################################################

def fun(arg):
    return arg

print fun(10)


def fun(a,b=10):
    print a
    print b

fun(1,5)
fun(1)

def fun(*arg):
    print arg[0] 
    

fun(1)
fun(1,2,3,4,56,)
fun(1,345,5677,76,789,5678,789,5789)

def fun(**arg):
    print arg["a"]

fun(a=1,b=21,c=5)
fun(a=1,b=5)
fun(a=1)

def fun(a,*b):
    print a
    print b


###################################################
# Lambda
###################################################

a=lambda x: x*2
print a(2)
print type(a)

a=[1,2,3,4,5,6,7,8,9,0]

def fun(a):
    for i in a:
        if i>3:
            print i

c=[1,2,3,54,5,6,7]

fun(c)



def fun(arg):
    """
        my first manual
    """
    if arg>3:
        return True
    else:
        return False

print filter(fun,c)


print filter(lambda arg: True if arg > 3 else False,c)

help(fun)


print map(lambda x:x*2,c)

help(map)
help(reduce)
help(filter)

a=[1,2,3,4,5]

print reduce(lambda x,y:x*y,a)

def filter_long_words(lis,num):
    return filter(lambda arg: True if len(arg)>num else False, lis)

lista=["ef","fdsf","fd","dfs","gfdgh","ads"]    
n=3

print filter_long_words(lista,n)






###################################################
# Challenge 4
###################################################


tekst = """
nJzRgMGZxzpZkQGuZzPolAPNsDsHpyjmFlKnmMxj
OMDgqLpYTMFmlRsKYqRyUHXHCKmknKTWJTRWXDfEZqBHnBHcQaDseMoUjONIarxTWJwZPfVPEkhQZylK
sIkVuORXFsIvtaPuJUuGwFsyhZHpHWWTvenoaPYfwwFqTYhcYcsjaHliyIotgstirQurQJLyMcwEliIk
EUBkywIQmZLNURadZzPuWEKucvTNConMvILAQekRhmwlnVTbeGqZGEqOqSnJvqxXIzsDOJfcENBdxRkk
mkMFlxpLfDgwiwjFaeJKLaApQLNalgytHcyrVtXRGbNVKCWiWAtiZKkShJbJwEAyEfUYySCGvdigKokL
KgBKMyFFbikGyZioXmFpxbAeFUxijcsFrgxkEzgbLRYiYTJRvQgGqsEaEHLADBVyOXpbVzliNKmxWawYihziiavGSYofPNeKsTXruMUumRRPQJzvSzJkKbtSipiqBd
"""
import re

wzor = "[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+"

print re.findall(wzor, tekst)


"""
print ord("A")
print ord("Z")
print chr(97)
lista = ""
for x in tekst:
        print x
    #if ord(x)>= 97 and ord(x)<=122:
     #   lista+=x

#print lista 65 90
"""

##############################################
# Regular Expresion
##############################################

text="this is this is sample text 54 4 sample"

print re.search("s.*", text, re.IGNORECASE).group()
print re.match("s.*", text, re.IGNORECASE)



print re.match("(.*) is sample text (\d{2})", text).group()

print re.match(".*? is",text).group()

#gwiazdka jest operatorem zachlannym

text="23cdfsgsrgth09"

print re.match("[0-9]{2}", text).group()
print re.findall("[0-9]{2}", text)

text=":****::::"

print re.match("[:*]{9}$",text).group()

# $ mowi ze szukamy dok.adnie 9 znakow

##############################################
# File Oprations
##############################################

try:
    f = open("plik.txt")

    lines = f.readlines()
    print lines
    f.seek(0) # ustawia kursor na poczatek
    lines = f.readlines()
    print lines
    f.seek(0)
    lines=f.read().splitlines()
    print lines
    
except IOError as e:
    print e
else:
    f.close()

finally:
    pass

####################

with open("plik.txt") as f:
    #print f.readlines()
    for line in f.read().splitlines():
        print line

text="Allowed Hello Hollow"

for m in re.finditer("ll", text):
    print "ll found", m.start(), m.end()

##############################################
# Zad 7
##############################################

a=0
b=0
with open("plik.txt") as f:
    linia = f.read().splitlines()
    print linia, "<--------------------"
    if len(linia)==5:
        if re.match("[:]{9}$",linia[0]) and re.match("[:]{9}$",linia[4]):
            print "git"
            if len(re.findall("[*]",linia[1])) == 1 and len(re.findall("[*]{1}",linia[3])) == 1 and len(re.findall("[:]",linia[1])) == 8 and len(re.findall("[:]",linia[3])) == 8:
                print "git2"
                if re.match("::\*:::\*::",linia[2]):
                    print "dodawanie"
                    for m in re.finditer("\*", linia[1]):
                        a=m.start()+1
                        print m.start()+1
                    for m in re.finditer("\*", linia[3]):
                        b=m.start()+1
                        print m.start()+1
                    print a+b

                elif re.match("::::\*::::",linia[2]):
                    print "odejmowanie"
                    for m in re.finditer("\*", linia[1]):
                        a=m.start()+1
                        print m.start()+1
                    for m in re.finditer("\*", linia[3]):
                        b=m.start()+1
                        print m.start()+1
                    print a-b

                elif re.match(":::\*\*\*:::",linia[2]):
                    print "dzielenie"
                    for m in re.finditer("\*", linia[1]):
                        a=m.start()+1
                        print m.start()+1
                    for m in re.finditer("\*", linia[3]):
                        b=m.start()+1
                        print m.start()+1
                    print a/b

                elif re.match("\*:\*:::\*:\*",linia[2]):
                    print "mnozenie"
                    for m in re.finditer("\*", linia[1]):
                        a=m.start()+1
                        print m.start()+1
                    for m in re.finditer("\*", linia[3]):
                        b=m.start()+1
                        print m.start()+1
                    print a*b
                    
                else:
                    print "zla operacja"
            else:
                print "zle2"
        else:
            print "zle"
    else:
        print "za dlugi kod"

# http://holger.thoelking.name/python-challenge/all
##############################################
# Chalenge 4
##############################################       
'''
import urllib2
import re
html=str(44827)
while True:
    yrl=urllib2.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+html)
    html1 = yrl.read()
    html2= html1.split()
    html=html2.pop()
    print html
        '''

##############################################
# Chalenge 5
##############################################  

import urllib2


yrl=urllib2.urlopen('http://www.pythonchallenge.com/pc/def/peakhell.jpg')






































