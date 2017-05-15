#################################
# Primitives data types
#################################

a=1
b="a"
c=2.3

print (type(a))
print (type(b))
print (type(c))

#################################
# Tuple
#################################

a=(1,2,3,4,5)
b=1,2,3,4,5
c=tuple()

print (type(a))
print (type(b))
print (type(c))

#nieda sie zmodyfikowac tupli  np a[2]= 54



a = ("1", 4,"2",6)
print (a)

#################################
# Listy
#################################

a=[1,2,3,4,5]

print (type(a))

a.append(6)
a.insert(1,7)
print (a, "log")
del a[0]
print (a)

a = range(1,10)
print( a, "lista as rande")

print (dir(a))

#a = range(1,10,2)
#print a, "lista as rande z krokiem 2"


print (a[3:7])
print (a[0:8:2])
print (a[-1])
print (a[-1:-5:-1])


a = "string"

print (a[::-1])

a=1
b=2

a,b=b,a
print( a, "2<---------------")
print (b, "1")
a = [x for x in range(1,10)]
print (a, "komprehention list")
#################################
# Set
################################# nie indeksowalne obiekty

a = set([1,2,3,4,5])
print (a)
print (type(a))

a = {1,2,3,4,5}
print (type(a))

for i in a:
    print (i)
    
a.remove(4)
print (a)

a.add(4)
print (a)

a=set("text")
print (a)

print( "t" in a)

#################################
# FrozenSet
#################################

a=frozenset([1,2,3,4,5])
print( a)
#a.add(5)

print( dir(a))

"""
multi line comment
"""


#################################
# Dictionary
#################################

a={
    "a":1,
    "b":1,
    "c":1,
    "d":1,
    }
print (a["a"], "get element by index")
print (a.keys())
print (a.values())
print (a.items()) #print list of tuples)

a["d"] = "4" # add to dictionary

print( a)
print( type(a))

#################################
# Syntax
#################################

if 1<2:
    print ("tah")
else:
    print ("nie")

var = 100
if var == 200:
    print ("dzvfghdfsh")
    print (var)
elif var == 150:
    print ("gfdhy")
    print (var)

for i in range(1,10):
    print (i)

print (ord("a"))
print (chr(97))

#################################
# zad 0
#################################


help(str)
help(list)

a = "1"
b=2

print (type(int(a)))
print (type(str(b)))

a ="witaj swiecie"
b = a.split()
c=b[::-1]
print (" ".join(c)+"<-------------------")

#################################
# zad 1
#################################

a="she sells sea shells"
b=a.split()
c=b[::-1]
d=" ".join(c)
print (d)

############


h=" ".join(a.split()[::-1])

print (h)


#################################
# zad 2
#################################

Dictionary={
    "abc":2,
    "def":3,
    "ghi":4,
    "jkl":5,
    "mno":6,
    "prs":7,
    "tuw":8,
    "xyz":9
    }
 

t = "Eve has a cat".lower()
text = ""
for litera in t:
    for item in Dictionary.items():
        if litera in item[0]:
            index=item[0].index(litera) + 1
            text+=index *  str(item[1])
print (text)

#################################
# zad 3
#################################

#a = raw_input("enter number")
print (len(set(str(a))))

print (r"\n") #raw string)
if 1<2:
    pass

a=[1,2,3,4,5]
for i in a:
    print (i)
    break
else: # wykonuje sie jak petla zakonczy sie prawidlowo
    print ("elser")
#if {}:
#    print "ok"

#################################
# zad 5
#################################

a="a toyota".lower()
c=a.replace(" ","")
b=c[::-1]
if c==b:
    print ("pali" )
else:
    print( "nie pali")

#################################
# zad 4
#################################


rowne = []
mniejsze = []
wieksze = []

for i in range(1,7):
    for j in range(1,7):
        a = i,j
        if i==j:
            rowne.append(a)
        elif i<j:
            mniejsze.append(a)
        else:
            wieksze.append(a)
            


print (rowne)
x=0
y=0
print (mniejsze)

print (wieksze)

while mniejsze:
    a=mniejsze.pop()
    x+=a[0]
    y+=a[1]
print ("suma mniejszych ", x+y)

while wieksze:
    a=wieksze.pop()
    x+=a[0]
    y+=a[1]
print ("suma wieksze ", x+y)

while rowne:
    a=rowne.pop()
    x+=a[0]
    y+=a[1]
print ("suma rowne ", x+y)



#############################################
# chellange 1
#############################################

tekst = "map"

print (ord("a"))
print (chr(97))
print ("------------------")
b=[]
for i in tekst:
    b+= chr(ord(i)+2)

print( b)


#############################################
# chellange 2
#############################################

tekst = """
@)](+[$*_(]*$[[&@^(_*#(*&!^{+]_%)_)^[}@]#]%#@+^+[%{_*{!)}#$@#)_$!_(!*+#}%%}+$&$[
%&]!{{%*_!*}&)}$**_{*!#%[[#]!](^^$![#[[*}%(_#^^!%))!_^@)@**@}}(%%{#*%@(((]^%^![&
}!)$]&($)@](+(#{$)_%^%_^^#][{*[)%}+[##(##^{$}^]#&(&*{)%)&][&{]&#]}[[^^&[!#}${@_(
#@}&$[[%]_&$+)$!%{(}$^$}* """
print (ord("a"))
print (ord("z"))
print (chr(97))
lista = ""
for x in tekst:
    if ord(x)>= 97 and ord(x)<=122:
        lista+=x

print (lista)


