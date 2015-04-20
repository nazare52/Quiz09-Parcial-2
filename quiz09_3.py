# Sergio Andrade Nieves
def superpower(a,b):
 i = 1
 for t in range(b):
  i = i*a
 return i

x = "{} to the power of {} is {}"
print (x.format(4,2,superpower(4,2)))
print (x.format(3,4,superpower(3,4)))