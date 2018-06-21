# 1.create base class animal nas base and made a base class tiger

class animal:
    def animal_attiribute(self):
       print("tiger is carnivore animal")
       print("tiger is national animal")
       print("no. of tiger are decressing continously due to hunting")

class tiger(animal):
    pass
b=tiger()
b.show()
b.display()


#2. find output of following code
class A:
    def f(self):
        return self.g()
    def g(self):
        return 'A'
class B(A):
    def g(self):
        return B
a=A()
b=B()
print (a.f(),b.f())
print(a.g(),b.g())

#3.MAKE CLASSCOP initialise name ge work experience designation. createanotherclass mission which extend the class cop.
# q3 Create a class Cop. Initialize its name, age , work experience and designation. Define methods to add, display and update the following details. Create another class Mission which extends the class Cop. Define method add_mission _details. Select an object of Cop and access methods of base class to get information for a particular cop and make it available for mission.
#
class Cop:

    def __init__(self,cop_name, cop_age, work_experience, designation):
        self.cop_name =cop_name
        self. cop_age =cop_age
        self.work_experience = work_experience
        self.designation = designation

    def display(self):
        print("Details:")
        print(self.cop_name)
        print(self.cop_age)
        print(self.work_experience)
        print(self.designation)

    def update(self,cop_name,cop_age, work_experience, designation):
        self.cop_name =cop_name
        self.cop_age =cop_age
        self.work_experience = work_experience
        self.designation = designation


class Mission(Cop):
    fighter_helicopter = 5
    fighter_tankers = 9

    def add_mission_details(self):
        print("number of fighter helicopter:", self.fighter_helicopter)
        print("number of fighter tankers:", self.fighter_tankers)


cop_name = input(" cop Name:")
cop_age = int(input("cop Age:"))
work_experience = input("Work Experience:")
designation = input("Designation")
a= Mission(cop_name, cop_age, work_experience, designation)
print("")
a.display()
print("")
a.add_mission_details()
print("")
a.update(input("cop Name:"), int(input("cop Age:")), input("Work Experience:"), input("Designation:"))
print("")
a.display()


#4. create class shape. create the method area create class rect.nd sq which inherit shape nd access the method area


class Shape:
    def __init__(self,len, brd):
        self.len = len
        self.brd = brd

    def area(self):
        self.answer = self.len * self.brd


class Rect(Shape):
    def arearect(self):
        print("area of rectangle:", self.answer)


class Square(Shape):
    def areasq(self):
        print("area of square:", self.answer)


len = int(input("enter the len:"))
brd = int(input("enter the brd:"))
c = Rect(len, brd)
b = Square(len, brd)
if len == brd:
    b.area()
    b.areasquare()
else:
    c.area()
    c.arearect()