# showing the data types of python

# normal string data type
var = "Hello python!"
print(type(var)) # type() function to check the type of data type
print(var)

# integer data type
var = 1000 # re-declaring the variable
print(type(var)) # type() function to check the data type
print(var)

# floating point data type
var = 2.1432 # re-declaring 
print(type(var))
print(var) # display the variable data

# complex data type
var = 2j # 'j' denotes that the value is a complex number
print(type(var)) # use of type() function
print(var) # display the data

# list in python
var = ["Google", "Microsoft", "Meta", "Amazon", "SpaceX"]
print(type(var))
print(var)

# tuple in python
var = ("Google", "Amazon", "Goldman Sachs", "PaloAlto") # re-declaring var 
print(type(var))
print(var)

# range in python
var = range(10) # range in python starts with 0
print(type(var))
print(var)

# dictionary in python aka hash map or hash table in other languages
var = {
  "First Name" : "Pratick",
  "Last Name" : "Baraik",
  "Designation" : "Python Dev" 
}
print(type(var))
print(var)

# set or array in python
var = {
  "Pen",
  "Pencil",
  "Paper"
}
print(type(var))
print(var)

# frozenset in python
var = frozenset({
  "Bard",
  "Bing",
  "GPT"
})
print(type(var))
print(var)

# boolean in python
var = False
print(type(var))
print(var)
var = True # re-declared
print(var)

# bytes data type in python
var = bytearray(4) # declaring bytearray
print(type(var))
print(var)

# memoryview data type in python
var = None
print(type(var))
print(var)