# Sergio Andrade Nieves
def triangulo(n):
 c = 0
 for t in range(n):
  c += 1
  print ("T"*c)
 for t in range(n):
  print ("T"*c)
  c -= 1

triangulo(6)