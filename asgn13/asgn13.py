#1. nsame and handle the exception occured in the following program
try:
    a=3
    if a<4:
        a=a/(a-3)
        print(a)
except Exception:
    print("exception occured")
#error: division by 0 and removed by except Exception.......

#2.name and handle the exception occured in the following program
l=[1,2,3]
print(l[3])
#indexerror:list index out of range
#removed by
l=[1,2,3]
try:
   print("1,2,3")
#  except ZeroDivisionError:
    print("divide by zero")
except IndexError:
     print("index error")
#removed by
#except IndexError

#3.what will be output of following code
#program to depict raising exception
try:
    raise NameError("hi there") #RAISEERROR
#NameError:hi there
except NameError:
    print("an exception")
    raise # to detrmine weather theexception wass raised or not
#4.function which return a/b
def AbyB(a,b):
    try:
        c=((a+b)/(a-b))
    except ZeroDivisionError
        print("a/bresult in 0")
    else:
        print c
#deliver program to test abovefunction
AbyB(2.0,3.0)
AbyB(3.0,3.0)
#wap to show and handle following exception
#1.import error
#2.value error
#3.indexerror
#1.import error


# inner_import_2.7.py
import sys

try:
    from exception import myexception
    except Exception as e:
    print(e)
 
#2.value error
try:
    raise ValueError
    print("hello world")
except Exception:
    print("exception occured")
raise
#3. indexerror
l=[1,2,3]
try:
    print(l[5])
except ZeroDivisionError:
    print("divide by zero")
except IndexError:
    print("index error")
#6.create a userdefined exception AgeTooSmallError()thatwarns theuser when they haveentered age lessthan 18.type code must kep taking input till theuser enters the appro. age no.(lessthan18)

class AgeTooSmallError(Exception):
    pass


try:
    def age():  # age func is defined
        x = int(input("enter your age"))  # age is input
        if x < 18:
            print("you are too small")
            raise AgeTooSmallError("age too small exception")  # exception raised if age less than 18

        else:
            print("****")


    age()  # func is called
except AgeTooSmallError as e:
    print(e)  # depicts age too small error is occured
    age()  # if age less then 18 func called again after raising exception
else:
    print("thereis no exception")