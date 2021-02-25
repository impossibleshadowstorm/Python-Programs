from math import*
import math

n = 24.98
print("DEMONSTRATION OF CEIL IS::")
#print(n.__ceil__())
#print(math.ceil(n))
print(ceil(n))

n = 24.89
print("DEMONSTRATION OF FLOOR IS::")
#print(n.__floor__())
#print(math.floor(n))
print(floor(n))

n = 24.98
print("DEMONSTRATION OF ROUND IS::")
#print(n.__round__())
print(round(n))

n = -89.098
print("DEMONSTRATION OF ABS AND FABS IS::")
#print(abs(n))
#print(fabs(n))
print(math.fabs(n))

n = 9
print("DEMONSTRATION OF FACTORIAL IS::")
#print(factorial(n))
print(math.factorial(n))

print("DEMONSTRATION OF LCM AND GCD IS::")
#print(lcm(10, 5, 15))
print(math.lcm(15, 10, 30))
#print(gcd(10, 5, 15))
print(math.gcd(10, 5, 15))

array = [2, 2, 3, 4, 5]
tuple = (10, 20)
seqence = range(1, 10)
print("DEMONSTRATION OF PROD IS::")
print(math.prod(array, start=10))
print(math.prod(array, start=2))
print(math.prod(tuple, start=10))
print(math.prod(tuple, start=2))

print("DEMONSTRATION OF REMAINDER IS::")
print(remainder(4, 3))
print(math.remainder(5, 9))
