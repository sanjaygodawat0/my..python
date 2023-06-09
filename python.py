# python all keyword and source code 


# and	    as	        assert  break
# class	    continue	def	    del
# elif	    else	    except	nonlocal
# False	    finally	    for 	from
# global    if	        import	in

# is	    lambda	    None	not
# or	    pass	    print	raise
# return    True	    try	    while
# with	    yield	


# one by one all keyword using
# -------------------------------------------------------------------------------


# 1.using 'and' keyword

print(9!=10 and 9==10)#false
print(9!=10 and 9==9)#true
print(9!=10 and 9==10 and 4<10)#false


# output
    # false
    # true
    # false


# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------


# 2. using 'as' keyword

import keyword as pyKey
print(pyKey.kwlist)

output
    # ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------

# 3.using 'assert' keyword 

assert 4==4 #No Exception
assert 4==5 #AssertionError Exception Occured

# output
#     Traceback (most recent call last):
#   File "<string>", line 2, in <module>
# AssertionError

# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------



# 4.using 'break' keyword skip ------------------------------------------------------------



# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

# 5.using 'class' keyword

class myClass:
    def func():
        print("Hello")

myClass.func()

#output
    #Hello


# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------


# 6.using 'continue' keyword

a = 0
while(a < 10):
    if(a == 5):
        print("skipped value of a is ", a)
        a = a + 1
        continue
    print("value of a is ", a)
    a = a + 1

# output
    # value of a is  0
    # value of a is  1
    # value of a is  2
    # value of a is  3
    # value of a is  4
    # skipped value of a is  5
    # value of a is  6
    # value of a is  7
    # value of a is  8
    # value of a is  9

# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------


# 7.using 'def' using 

def func(a):
    print("Value of a is", a)

func(5)

# output
    # Value of a is 5

# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------


# 8.using 'del' keyword

list = [1, 4, 3, 5, 7]
del list[2]
print(list)

# output
    # [1, 4, 5, 7]
    # missing 3 q ki 3 index number 2  par tha 

# del ke alava hum remove ka use bhi use kr skte h 
# example : using 'remove'

list = [1, 4, 3, 5, 7]
list.remove(3)
print(list)

# output
    # [1, 4, 5, 7]

# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------


# 9.using 'elif' keword 
# less than and grater than program using python 

a = 11

if(a < 10):
    print("a is less than 10")
elif(a > 10):
    print("a is greater than 10")
else:
    print("a is equal to 10")

# output
    # a is greater than 10

# -------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------

# 10.using 'else' keyword
# odd even program usnig python
a = 11

if(a%2==0):
    print("Number is even.")
else:
    print("Number is odd.")

# output
    # Number is odd.
    
# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------


# 11.using 'except' keyword

try:
    a
except ZeroDivisionError:
    print("Divided by zero Error")
except NameError:
    print("a is not found")


# output
    # a is not found

# -------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------

# 12.using 'nonlocal' keyword

# // without nonlocal 

ar = 2
def mainFunc():
    var = 5
    def subFunc():
        var = 10
        print("subFunc : ", var)

    subFunc()
    print("mainFunc : ", var)

mainFunc()
print("global : ", var)

# output
    # subFunc :  10
    # mainFunc :  5
    # global :  2

# /////////////////////////////////////////////////////

# with nonlocal

var = 2
def mainFunc():
    var = 5
    def subFunc():
        nonlocal var
        var = 10
        print("subFunc : ", var)

    subFunc()
    print("mainFunc : ", var)

mainFunc()
print("global : ", var)

# Output :
#     subFunc :  10
#     mainFunc :  10
#     global :  2

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------

# 13. using 'False' using 

print(False == 0)
print(4 == 5)

# Output :
#     True
#     False

# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

# 14.using 'finally' keyword

try:
    a
except NameError:
    print("NameError Exception occured")
finally:
    print("Always executed")

# Output :
# NameError Exception occured
# Always executed

# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------

# 15. using 'for' keyword 

list = ["Rakesh", "Ramesh", "Suresh"]
for n in list:
    print(n)

# Output :
# Rakesh
# Ramesh
# Suresh

# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------


# 16.using 'from' keyword
# module.py 
def func1():
    print("I am in func1")
def func2():
    print("I am in func2")

# Output :

# //////////////////////////////////////////

# sample.py

from Module import func1
func1()

# Output :
# I am in func1


# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

# 17.using 'global'keyword
# test.1

def func():
    string = "Local Variable"
    print(string)

func()
print(string)

# Output :
# Local Variable
#     print(string)
# NameError: name 'string' is not defined

# test.2

def func():
    global string
    string = "Local Variable"
    print(string)

func()
print(string)

# Output :
# Local Variable
# Local Variable

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# 18.using 'if' keyword

var = 0

if(var == 0):
    print("var is equal to 0")


# Output :
# var is equal to 0

# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------

# 18.using 'import' keyword

import math
print(math.sqrt(16))

# Output :
# 4.0

# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------

# 19.using 'in' keyword

list = [6, 8, 4, 7, 8]
print(7 in list) #True
print(10 in list) #False


# Output :
# True
# False

# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------

# 20.using 'is' keyword

print("one" is "one") #True
print("one" is 1) #False
print("" is "") #True
print("" == "") #True
print([] is []) #False
print([] == []) #True


# Output :
# True
# False
# True
# True
# False
# True

# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------

# 21.using 'lambda' keyword
# normal function
def func(a, b):
    return a * b
print(func(5, 5))

# Output :
# 25

# Anonymous Function

var = lambda a, b: a * b
print(var(5,5))

# Output :
# 25

# --------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------

# 22.using 'none' keyword

print(None == '')
print(None == 0)
print(None == None)
print(type(None))


# Output :
# False
# False
# True
# <class 'NoneType'>

# -----------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------

# 23.using 'not' keyword

print(not(5!=6))  #False
print(not(5!=5))  #True

# Output :
# False
# True

# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------

# 24.using 'or' keyword

print(5!=6 or 5==6)  #True
print(5!=6 or 5==5)  #True
print(5!=6 or 5==6 or 4<6) #True
print(5==6 or 5>6 or 6<6) #False


# Output :
# True
# True
# True
# False

# -----------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------

# 25.using 'pass' keyword

def func(): pass

while 4 < 5:
    pass

# Output :

# -------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------

# 26.using 'raise' keyword

a = 12
b = 10
if a > b:
    raise ValueError("a should be smaller than b")


# Output :
# Traceback (most recent call last):

#     raise ValueError('a should be smaller than b')
# ValueError: a should be smaller than b


# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------

# 27.using 'return' keyword 

def func(a):
    b = a * a
    return b

print(func(5))

# Output :
# 25

# -----------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------

# 28.using 'True' keyword

print(True == 1)
print(False == 0)
print(1 == 1)
print(True + True)

# Output :
# True
# True
# True
# 2

# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

# 29.using 'try' keyword

try:
    a
except NameError:
    print("Value of a is not defined")

# Output :
# Value of a is not defined

# -----------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------

# 30.using 'while' keyword

a = 0
while a < 10:
    print("Value of a is", a)
    a = a + 1

# Output :
# Value of a is 0
# Value of a is 1
# Value of a is 2
# Value of a is 3
# Value of a is 4
# Value of a is 5
# Value of a is 6
# Value of a is 7
# Value of a is 8
# Value of a is 9

# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------

# 31.using 'with' keyword
# without 'with'

file = open("textfile.txt", "w")
file.write("Hello World")
file.close()

#  textfile.txt
# Hello World


# with 'with'

with open("textfile.txt", "w") as file :
    file.write("Hello World")

# textfile.txt
# Hello World

# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------

# 32.using 'yield' keyword 

def func_name():
    yield 5
    yield 10
    yield 15

for y in func_name():
    print(y)

# Output :
# 5
# 10
# 15


# --------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------


# next function ka use yield ki jgh use kya jata 


def func_name():
    yield 5
    yield 10
    yield 15
y = func_name()
print(next(y))
print(next(y))
print(next(y))

# Output :
# 5
# 10
# 15
