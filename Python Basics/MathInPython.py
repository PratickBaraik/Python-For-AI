"""
Maths in python provides access to the mathematical functions defined by the C standard.
These function cannot be used with complex numbers.
"""

# importing requried module for maths operations in python
import math

# maths.ceil() function in python
# it returns the ceiling of x, the smallest integer greater than or equal to x
print("math.ceil() function")
var1 = math.ceil(6.7) # result: 7
print("var1:", var1)

# math.floor() function in python
# it rounds numbers down to the nearest integer
print("math.floor() function")
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
print("math.copysign() function")
var1 = math.copysign(2, -1)
print("var1:", var1)

var2 = math.copysign(1.7, -2)
print("var2:", var2)

#math.fabs() function in python
# results absolute value of a number passed
print("math.fabs() function")
var1 = math.fabs(-1.23) # if (-ve) result = (+ve)
print("var1:", var1)
var2 = math.fabs(3.22) # if (-ve) result = (+ve)
print("var2:", var2)

# math.factorial() function in python
print("math.factorial() function")
var1 = 5
var2 = math.factorial(var1) # result: 120
print("var2:", var2)

# math.fmod() function in python
print("math.fmod() function")
var1 = math.fmod(2, 6)
print("var1:", var1)

# math.frexp() function in python
# returns the mantissa and exponent of x as the pair (m, e)
# m is float and e is an integer such that x = m * 2 ** e exactly
print("math.frexp() function")
var1 = math.frexp(4)
print("var1:", var1) # result: (m: 0.5, e: 3)

"""
math.fsum() function in python
returns an accurate floating point sum of values in the iterable.
avoid loss of precision by tracking multiple intermediate partial sums
the algo's accuracy depends on IEEE-754 arithmetic guarantees and the typical case usses extended precision addition and may occasionally double-round an intermediate sum causing it to be off in its least signigicant bit.
"""
print("math.fsum() function")
myList1 = [10, 20, 30, 40, 50]
var1 = math.fsum(myList1)
print("sum in var1:", var1)

myList2 = [1.5, 2.4, 7.9, 4.3]
var2 = math.fsum(myList2)
print("sum in var2:", var2)

# math.gcd() function in python
# returns the largest common divisor that divides the numbers without a remainder
print("math.gcd() function")
var1 = math.gcd(21, 4)
print("GCD:", var1)

var2 = math.gcd(20, 5)
print("GCD:", var2)

# math.isClose() function in python
# this method checks whether two values are close to each other, or not. 
print("math.isClose() function")
print("It is close:", math.isclose(1.233, 1.644))
print("It is close:", math.isclose(1.233, 1.233))
print("It is close:", math.isclose(1.233, 1.24))
print("It is close:", math.isclose(8.77, 8.770000007))

# math.isfinite() function in python
# return true if a value is neither an infinity nor a NaN, and false otherwise.
print("math.isfinite() function")
print("100:", math.isfinite(100))
print("0.0:", math.isfinite(0.0))
print("-10.78", math.isfinite(-10.78))
print("78.10", math.isfinite(+78.10))
print("math.inf:", math.isfinite(math.inf)) # using math.inf function, its uses is as follows (+ve)
print("-math.inf", math.isfinite(-math.inf)) # (-ve)
print("float(nan):", math.isfinite(float("nan"))) # nan aka Not A Number
print("float(inf)", math.isfinite(float("inf"))) # inf: any infinite value (+ve)
print("float(-inf)", math.isfinite(float("-inf"))) # inf: any infinte value (-ve)

# math.inf() function in python
# returns true if a value is a positive or negative infinity, and false otherwise
# this function is equivalent to float('inf')
# not need to mention examples for this

# math.isnan() function in python
# return true if a value is NaN (not a number), and false otherwise.
print("math.isnan() function")
print("100:", math.isnan(100))
print("0.0:", math.isnan(0.0))
print("-10.78", math.isnan(-10.78))
print("78.10", math.isnan(+78.10))
print("math.inf:", math.isnan(math.inf)) # using math.inf function, its uses is as follows (+ve)
print("-math.inf", math.isnan(-math.inf)) # (-ve)
print("float(nan):", math.isnan(float("nan"))) # nan aka Not A Number
print("float(inf)", math.isnan(float("inf"))) # inf: any infinite value (+ve)
print("float(-inf)", math.isnan(float("-inf"))) # inf: any infinte value (-ve)

# math.isqrt() function in python
# returns the integer square root of the non-negative integer.
print("math.sqrt() function")
var1 = math.sqrt(5)
var2 = math.sqrt(10)
var3 = math.sqrt(70)
var4 = math.sqrt(12)
print("Square root of 5:", var1)
print("Square root of 10:", var2)
print("Square root of 70:", var3)
print("Square root of 12:", var4)

# math.lcm() function in python
# return the least common multiple of the specified integer arguments.
# print("LCM of 5, 10, 20, 30:", math.lcm(5, 10, 20, 30))
# print("LCM of 7, 21, 63, 35:", math.lcm(7, 21, 63, 35))
# require proper initialization (not working this way)

# math.ldexp() function in python
# if used as math.ldexp(n, m) -> returns n * (2 ** m)
print("math.ldexp() function")
print(math.ldexp(8, 10))
print(math.ldexp(2, 7))
print(math.ldexp(3.4, 4))

# math.modf() function in python
# return the fractional integer parts of a number, both results carray the sign of number and are floats
print("math.modf() function")
print(math.modf(2.1))
print(math.modf(3))

# math.nextafter(x, y, steps=1) function in python
# return the floating-point value 'steps' steps after x towards y
# if x is equal to y, return y, unless steps is zero.
# print("math.nextafter() function")
# print(math.nextafter())
# need to find an alternative for this (not working)

# math.perm() function in python
# does the permutation operation
#  nPr = n! / (n - r)!, r <= n and if r > n, it results 0
# print("math.perm() function")
# print(math.perm(2, 7))
# not working this way

# math.prod() function in python
# calcuate the product of all the elements in the input iterable. Default start value is 1.
# print("math.prod() function")
# print("Product of 2, 3, 4:", math.prod(2, 3, 4))
# not working

# math.remainder() function in python
# return the IEEE 754-style remainder of x with respect to y.
print("math.remainder() function")
print(math.remainder(6, 3))

# continue after some times