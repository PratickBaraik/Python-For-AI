"""
Maths in python provides access to the mathematical functions defined by the C standard.
These function cannot be used with complex numbers.
"""

# importing requried module for maths operations in python
import math

# maths.ceil() function in python
# it returns the ceiling of x, the smallest integer greater than or equal to x
var1 = math.ceil(6.7) # result: 7
print("var1:", var1)

# math.floor() function in python
# it rounds numbers down to the nearest integer
var2 = math.floor(6.3) # result: 6
print("var2:", var2)

"""
facing problem here 
TODO: Use correct inclusion of math.comb()
# math.comb() function in python
# returns the number of ways to choose the k items from n items without repetition and without order aka combination of mathematics
numberOfItems = 10
numberOfPossiblities = 5
var1 = math.comb(numberOfItems, numberOfPossiblities)
print("var1:", var1)
"""

# math.copysign() 
# return a float with the magnitude of x but the sign of y
# if a platform supports signed zeros, copysign() returns -1.0
var1 = math.copysign(2, -1)
print("var1:", var1)

var2 = math.copysign(1.7, -2)
print("var2:", var2)

#math.fabs() function in python
# results absolute value of a number passed
var1 = math.fabs(-1.23) # if (-ve) result = (+ve)
print("var1:", var1)
var2 = math.fabs(3.22) # if (-ve) result = (+ve)
print("var2:", var2)

# math.factorial() function in python
var1 = 5
var2 = math.factorial(var1) # result: 120
print("var2:", var2)

# math.fmod() function in python
var1 = math.fmod(2, 6)
print("var1:", var1)

# math.frexp() function in python
# returns the mantissa and exponent of x as the pair (m, e)
# m is float and e is an integer such that x = m * 2 ** e exactly
var1 = math.frexp(4)
print("var1:", var1) # result: (m: 0.5, e: 3)

"""
math.fsum() function in python
returns an accurate floating point sum of values in the iterable.
avoid loss of precision by tracking multiple intermediate partial sums
the algo's accuracy depends on IEEE-754 arithmetic guarantees and the typical case usses extended precision addition and may occasionally double-round an intermediate sum causing it to be off in its least signigicant bit.
"""
myList1 = [10, 20, 30, 40, 50]
var1 = math.fsum(myList1)
print("sum in var1:", var1)

myList2 = [1.5, 2.4, 7.9, 4.3]
var2 = math.fsum(myList2)
print("sum in var2:", var2)

# math.gcd() function in python
# returns the largest common divisor that divides the numbers without a remainder
var1 = math.gcd(21, 4)
print("GCD:", var1)

var2 = math.gcd(20, 5)
print("GCD:", var2)

# TODO: math.isClose() function in python

# 