# integer var declaration and initialization
var1 = 10
print("var1:", var1, 'and type:', type(var1))

# initializing and casting into number type using int() function
var1 = int(22.7) # 22.7 is float type originally which is converted into 22 after passing it to int(22.7)
print("var1:", var1, 'and type:', type(var1))

var1 = int("1234") # here "1234" is string which is then converted into integer type
print("var1:", var1, 'and type:', type(var1))

# binary number in python - starts with '0b'
# binary to integer
var1 = int(0b1111) # value of 1111(binary) is 15(decimal)
print("var1:", var1, 'and type:', type(var1))

var1 = int("0b1100", 2) # 1100 is 12 and explicitly declaring that 1100 number has a base 2
print("var1:", var1, 'and type:', type(var1))

# convert integer to binary number
var1 = 5
var2 = bin(var1) # converting 'var1' value to binary value
print("var2:", var2, "and type:", type(var2))
# type(var2) give 'str' because its assuming the whole value '0b101' which is implicitly a string value

# octal number in python - starts with 0O
var1 = 0O100 # '0O100' is octal and its decimal value is 64
var2 = int(var1)
print("var2:", var2, "and type:", type(var2))

# explicit declaration of octal value 
var1 = "0O200" # octal value stored as string
var2 = int(var1, 8)
print("var2:", var2, "and type:", type(var2))

# hexadecimal value in python
# hex to int conversion
var1 = int("0X50EE", 16) # base of hex number is 16 and 0X50EE equals 20718
print("var1:", var1, "and type:", type(var2))

# int to hex conversion 
var2 = hex(20718) # using hex() function to convert integer into hexadecimal
print("var2:", var2, "and type:", type(var2))

# adding binary, octal, decimal, hexadecimal numbers all together
var1 = 100 # decimal number
var2 = 0b100 # binary number 0b100(binary) = 4(decimal)
var3 = 0o100 # octal number 0O100(octal) = 64(decimal)
var4 = 0x100 # hexadecimal number 0X100(hexadecimal) = 256(decimal)

sum = var1 + var2 + var3 + var4
print("Sum:", sum)

# floating point numbers in python
var1 = 10.78
var2 = 0.777
var3 = -57.22
var4 = -67.89
print("var1:", var1, "var2:", var2, "var3:", var3, "var4:", var4)

# scientific notation in python
# 'E' or 'e' helps in scientific notation
# always results in floating point value if not converted to any other type
var1 = 2e5 # result: 2 * 10^5 = 200000.0
print("var1:", var1)
var2 = 2.3E-3 # result: 2.3 * 10^-3 = 0.0023
print("var2:", var2)

# infinity in python
var1 = 5.6e23
print("var1:", var1, "type:", type(var1))
var1 = float("Infinity")
print("var1:", var1, "type:", type(var1)) # var1: 'inf' 
"""
Infinity in python is an abstract concept in python.
Physically, infinitely large number can never be stored in any amount of memory.
A vary large number with 400th power of 10 is represented by Inf.
If you use "Infinity" as argument for float() function, it returns Inf. 
"""

# Not a number in python aka Nan
# It represents any value that is undefined or not representable
var1 = float('Nan')
print("var1:", var1)

# complex number in python
"""
A complex number consists of a real part and an imaginary part, separated by either "+" or "-".
The real part can be any floating point (or itself a complex number) number.
The imaginary part is also a float/complex, but multiplied by an imaginary number.

'i' = iota which is sqrt(-1), complex number: x + yi, where x is the real part and yi is the imaginary part 

Sometimes 'i' can be replaced by 'j' to denote complex number
* python uses 'j' to denote complex number
"""
var1 = 6 + 9j
print("var1:", var1) # result: (6+9j)
print("type:", type(var1))
var2 = 1.9e-2 + 2.8e2J
print("var2:", var2, "type:", type(var2))

# complex() function in python
# two types of complex() functions
# 1st: takes one argument, 2nd: takes two arguments
var1 = complex(6.7) # result: 6.7 + 0J
print("var1:", var1, "type:", type(var1))
var2 = complex(6.7, 3) # result: 6.7 + 3j
print("var2:", var2, "type:", type(var2))
# in sec type of complex() function we can pass two arguments
# first argument is the real part and second argument is the complex part
 
# string to complex
var1 = "7.32+7j"
var2 = complex(var1)
print("var2:", var2, "type:", type(var2))

# explicit presentation of complex number in python using .real and .imag 
var1 = 8+4j
print("var1 real part:", var1.real, "var1 imaginary part:", var1.imag)

# lastly, conjugate in python complex number
var1 = 4-2.8J
print("conjugate of var1:", var1.conjugate()) # result: 4+2.8j