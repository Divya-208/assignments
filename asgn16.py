#1. create a button and print hello world on console screen

def display():
    print("hello woorld!")
import tkinter as tk
root=tk.Tk()
b1=tk.Button(root,text="welcome",width=25,fg="red",bg="yellow",command=display)
b1.pack()
root.title('second counts')
b2=tk.Button(root,text='stop',width=25,fg="red",bg="green",command=root.destroy)
b2.pack()

root.mainloop()


#2. wap python programto create a action when the button is click it perform action
def display():
    a=int(input("enter the a no."))
    b=int(input("enter second no."))
    x=a+b

    print("sum is=",x)


import tkinter as tk
root = tk.Tk()
b1 = tk.Button(root,text="hello", width=25,bg="pink",fg="green",command=display)
b1.pack()

root.mainloop()

#3.create a frame wirth any labeltext and two buttons .one to exit and other to change the label to some opther text
import tkinter
from tkinter import *
def display():
    label.config(text="welcome to the world of programing....")
root=Tk()
f1= Frame(root)
f1.pack()
label=Label(root,text="enjoy guys",width=40)
label.pack()
b1=Button(f1,text="pythonlearning",width=30,bg="blue")
b1.pack()
b2=Button(f1,text="java learining",width=30,bg="red",command=display)
b2.pack()



root.mainloop()
#4.wap to take input in gui using tkinter interface in python
from tkinter import *
def input():
    print(e1.get())
    print(e2.get())

root=Tk()
Label(text='FIRST NAME').grid(row=0)
Label(text='last name').grid(row=1,)
e1=Entry(root)
e2=Entry(root)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
b1=Button(text=" press here",width =40,bg="orange",fg="brown",command=input)
b1.grid(row=2,column=1)
root.mainloop()



