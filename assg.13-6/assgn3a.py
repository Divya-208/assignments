# q;1 create the list with user defined input
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
['google','apple','facebook','microsoft','tesla']
L2=['google','apple','facebook','microsoft','tesla']
print(L2)
print(list.extend(L2))
print(list)
print("\n")

#Q3 count the no.of times object occur
print(list.count(1))

#Q4 create the list with no. and sort it in ascending order
list=[1,3,2,6,5]
print(list)
print(list.sort( ))
print(list)

 #Q5 enter two array nd merge them nd save them, in another variable
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
print(C)



