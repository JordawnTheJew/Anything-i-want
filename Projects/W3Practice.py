#Python Comments 
#Py has no syntax for multiline comments so a "#" is required for each line

"""This is a 
multi-line
comment contained 
in multiline string"""

#print ("Hello world")

#"CREATING VARIABLES"

#x = 5
#y = "John"
#print(x)
#print(y)
 
#"Change variable type"
#x = 4    # x is of type int 
# x = "Sally" # x is now part of str
#print(x)

#Casting:
"""
x = str(3)  # x will be '3'
y = int(3)  # y will be 3
z = float(3) # z will be 3.0

print (type(x))
print (type(y))
print (type(z))
"""
"""
#strign variables can be declared via single or double qoutes
x = "John"
# is the same as
x = 'John'

#Variable names are case-sensitive, A will not overwrite a
a = 4
A = "Caiah"
"""

#VARIABLE NAMES:

# Start with an underline character or a letter, Cannot start witha number, Only contain alphanumeric and underscorse A-z, 0-9, _
#GOOD 
"""
myvar = "Gabs"
my_var = "Payge"
_my_var = "Caiah"
myVar = "Alayna"
MYVAR = "Isaac"
myVar2 = "Dani"

#BAD

2myvar = "Elizabeth"
my-var = "Ian"
my var = "Dustin"


print(my_var)
"""
"""
#Multi word variable names

myVariableName = 'John' #"Camel Case"

MyVariableName = 'John' #"Pascal Case"

my_variable_name = "John" #"Snake Case"

"""

"""
# many values to any variables
x, y, z = "banana", "banana shake", "banana pancake"
print (x)
print(y)
print(z)
#one value for x's variables
d = b = c = "Banana popsicle"
print(d)
print(b)
print(c)
#Unpack a collection
BananaProducts = ["Banana Lollipop","Banana Bread", "Banana Candy"]
b, a, n = BananaProducts
print(b)
print(a)
print(n)
"""
"""
#Output Variables

x = "awesome"
print("Python is " + x)

a = "Python is "
b = "awesome"
c = a + b

print(c)

x = 5
y = 5
print (x + y)

x = 50
#y = "Doe"
print(x + y)
"""

#Global Variables
"""
#Variable outside funtion
x ="awesome"

def myfunc():
    print("python is " + x)

myfunc()
"""
#Variable inside Function
"""
x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("python is " + x)
"""
"""
#Global Variable created inside funtion
x = 'awesome'

def myfunc():
    global x 
    x = "fantastic"

myfunc()

print("python is " + x) 
"""
"""
#DATA TYPES
#Text Types: str
#Numeric Types: int, float , complex
#Sequence Types: list,, tuple, range
#Mapping Type: dict
#Set Types: set, frozenset
#Boolean type: bool
#Binary Types bytes, bytearray, memoryview
"""

#"type() Function"
"""
x=5
print(type(x))
"""

#"Setting Data Types"
"""
x="Hello World"                     str
x=20                                int
x=2.50                              float
x=1j                                complex
x= [1,2,3]                          list
x= (1,2,3)                          tuple
x=range(6)                          range
x= {"name" : "John", "age" : 36}    dict
x={"apple","banana","cherry"}       set
x= frozenset({"apple", "banana", "cherry"} ) frozenset
x=true                              bool
x=b"hello"                          bytes
x=bytearray(5)                      bytearray
x=memoryview(bytes(5))              memoryview
"""

#PYTHON NUMBERS

# x=1 int
# y=2.8 float
# z=1j  complex

print(type(x))
