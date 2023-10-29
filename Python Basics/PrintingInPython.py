# normal print statement
print("hello world")

# new line in print statement
print("Pratick")
print("\n")
print("Baraik")

# multiple new line in print statement
print("Pratick")
print(4 * "\n")
print("Baraik")

# string concatenation in print statement
string1 = "I"
string2 = "am"
string3 = "python"
string4 = "developer"
# print without whitespaces
print(string1 + string2 + string3 + string4)
# print with whitespaces
print(string1 + " " + string2 + " " + string3 + " " + string4)

myNumber = 100
prefixStatement = "I have"
postfixStatment = "bucks"
# type casting is necessary to print the different datatypes 
print(prefixStatement + " " + str(myNumber) + " " + postfixStatment) # using str() function to change myNumber which is integer type into string type

# use of type() function to print the type of data stored 
print(type(myNumber))
print(type(string1))

# use of f-strings for string concatenation
print(f'I have {myNumber} bucks')

# use of positional arguments to concatenate string
print('My wallet contains', myNumber, 'bucks')

# print none constant
print(None)