# Sergio Andrade Nieves
def distancia(x1,y1,x2,y2):
 import math
 b = x2-x1
 h = y2-y1
 b2 = b**2
 h2 = h**2
 d2 = b2+h2
 d = math.sqrt(d2)
 return d
 
t = distancia(0,0,10,10)
print (t)