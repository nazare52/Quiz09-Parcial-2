# Sergio Andrade Nieves
def fibonacci(n):
 if n == 0:
  return 0
 if n == 1:
  return 1
 f1 = 0
 f2 = 1
 f = 0
 for t in range(n-1):
  f = f1+f2
  f1 = f2
  f2 = f
 return f

print(fibonacci(5))