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
