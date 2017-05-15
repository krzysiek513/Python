#!/usr/bin/env python
b = 2
a = 1
if a > b:
	print (b)
else:
	print (a)
	
c = 2

if a > b and a > c:
	print (a)
elif c == b:
	print ("C i B rowne")
else:
	print (b)

imiona = [ "zbychu", "rychu", "zdzisiu" ]
print (imiona)
imiona[1] = "rychu2"
print (imiona[1])
print (len(imiona))
imiona.append("Renata")
print (imiona)

l = ['a', 'b', 'c']
s = '.'
print (s.join(l))
