# THREADS


#Create a threading process
import threading
from threading import Thread
import time

def display():
    print("Wait for 5 sec\n")
    time.sleep(5)
    print("It was slept for 5 sec")

t1 = Thread(target=display)
t1.start()
t1.join()
print("\n00000000000000000000000000000\n")






#Make a thread that prints number
import threading
from threading import Thread
import time
def display():
    for x in range(1,11):
        print(x)
        time.sleep(1)

t2=Thread(target=display)
t2.start()
t2.join()
print("\n############\n")






#Make a list that has 3 elements.
import threading
from threading import Thread
import time
def display(l):
    for x in l:
        print(x)
        time.sleep(1)

l=[2,34,6,9,12]
t3=Thread(target=display,args=(l,))
t3.start()
t3.join()
print("\n&&&&&&&&&&&&&&&&\n")





#Call factorial function using thread.
import threading
from threading import Thread
import time
import math
def fact():
     fact=1
     for x in range(1,num+1):
         fact=fact*x
     print("Fact of ",num,"is",fact)

num=int(input("Enter any  number"))
t4=Thread(target=fact)
t4.start()