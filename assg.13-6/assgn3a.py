#3;1 create the list with user defined input
print("enter the list of items")
list=[ ]
x=input("1")
y=input("2")
z=input("3")
print("the list is")
list=[x,y,z]
print(list)
print("\n")


#Q2 add the following list to the upper created list
# ['google','apple','facebook','microsoft','tesla']
L2=['google','apple','facebook','microsoft','tesla']
print(L2)
print(list.extend(L2))
print(list)
print("\n")

#Q3 count the no.of times object occur
 print(list.count(1))

Q4 create the list with no. and sort it in ascending order
list=[1,3,2,6,5]
print(list)
print(list.sort( ))
print(list)

 Q5 enter two array nd merge them nd save them, in another variable
A=[1,2,3]
print(A)
B=[ 6,4,5]
print(B)
print(A.sort())
print(A)
print(B.sort())
print(B)
C=(A,B)
print(C)
C=A+B
print(C


#Q:6 stack nd queue
print("stack")
l1=["my","new","list"]
print(l1)
l1.append("of")
print(l1)
l1.append("python")
print(l1)
print(l1.pop())
print(l1)
print(l1.pop())
print(l1)
print("\n")
print("queue")
l2=["easy","is","python",]
print(l2)
l2.reverse()
print(l2)
print(l2.pop())
print(l2)

#Q:7 count the even and odd no.
l3=[1,2,3,4]
print(l3)
even=0:
odd=0:
for no. in l3:
	if(number%2==1):
		odd=odd+1
	if(number%2==0):
		even=even+1
print("number of evenis:",even)
print("number of odd is :,odd")