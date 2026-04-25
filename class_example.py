# class Person:
#     '''This is a person class'''
#     def __init__(self, fname, lname): # def __init__(a, "Vishal", "Kumar") def __init__ (b, "Ran", "Shyam")
#         self.fname = fname # a.fname = Vishal # b.fname = "Ram"
#         self.lname = lname # a.lname = Kumar b.lname = "Shyam"

#     def greet(self):
#         return (f"Hello from {self.fname} {self.lname}")

# a = Person("Vishal","Kumar")
# b = Person("Ram", "Shyam")

# # print(f'Full Name: {a.fname} {a.lname}')
# # print(f'Full Name: {b.fname} {b.lname}')

# print(b.greet())

# Simple Inheritance
# Base class
# class Parent:
# 	def func1(self):
# 		print("This function is in parent class.")

# # Derived class
# class Child(Parent):
# 	def func2(self):
# 		print("This function is in child class.")


# # Driver's code
# object = Child()
# object.func1()
# object.func2()

# # Python program to demonstrate
# # multilevel inheritance

# Base class


# class Grandfather:

# 	def __init__(self, grandfathername):
# 		self.grandfathername = grandfathername

# # Intermediate class


# class Father(Grandfather):
# 	def __init__(self, fathername, grandfathername):
# 		self.fathername = fathername

# 		# invoking constructor of Grandfather class
# 		Grandfather.__init__(self, grandfathername)

# # Derived class


# class Son(Father):
# 	def __init__(self, sonname, fathername, grandfathername):
# 		self.sonname = sonname

# 		# invoking constructor of Father class
# 		Father.__init__(self, fathername, grandfathername)

# 	def print_name(self):
# 		print('Grandfather name :', self.grandfathername)
# 		print("Father name :", self.fathername)
# 		print("Son name :", self.sonname)


# # Driver code
# s1 = Son('Prince', 'Rampal', 'Lal mani')
# # print(s1.grandfathername)
# s1.print_name()


# # Python program to demonstrate
# # Hierarchical inheritance


# Base class
# class Parent:
# 	def func1(self):
# 		print("This function is in parent class.")

# # Derived class1


# class Child1(Parent):
# 	def func2(self):
# 		print("This function is in child 1.")

# # Derivied class2


# class Child2(Parent):
# 	def func3(self):
# 		print("This function is in child 2.")


# # Driver's code
# object1 = Child1()
# object2 = Child2()
# object1.func1()
# object1.func2()
# object2.func1()
# object2.func3()

# # Python program to demonstrate
# # multiple inheritance

# Base class1
# class Mother:
# 	mothername = ""

# 	def mother(self):
# 		print(self.mothername)

# # Base class2


# class Father:
# 	fathername = ""

# 	def father(self):
# 		print(self.fathername)

# # Derived class


# class Son(Mother, Father):
# 	def parents(self):
# 		print("Father :", self.fathername)
# 		print("Mother :", self.mothername)


# # Driver's code
# s1 = Son()
# s1.fathername = "RAM"
# s1.mothername = "SITA"
# s1.parents()


# Encapsulation

# class Computer:
#     def __init__(self):
#         self.__maxprice = 900

#     def sell(self):
#         print(f"Selling Price - {self.__maxprice}")
    
#     def changeMaxPrice(self, newPrice):
#         self.__maxprice = newPrice

# a = Computer()
# a.sell()

# a.changeMaxPrice(1000)
# a.sell()

# b = Computer()
# b.sell()

# Polymorphisam

# class Bird:
  
#     def intro(self):
#         print("There are many types of birds.")

#     def flight(self):
#         print("Most of the birds can fly but some cannot.")

# class sparrow(Bird):
  
#     def flight(self):
#         print("Sparrows can fly.")

# class ostrich(Bird):

#     def flight(self):
#         print("Ostriches cannot fly.")

# obj_bird = Bird()
# obj_spr = sparrow()
# obj_ost = ostrich()

# obj_bird.intro()
# obj_bird.flight()

# obj_spr.intro()
# obj_spr.flight()

# obj_ost.intro()
# obj_ost.flight()



# from abc import ABC, abstractmethod

# class Payment(ABC):
#     def print_slip(self, amount):
#         print(f'Purchase amount {amount}')
#     @abstractmethod
#     def payment(self, amount):
#         pass

# class CCPayment(Payment):
#     def payment(self, amount):
#         print(f"Credit card payment {amount}")

# class DCPayment(Payment):
#     def payment(self, amount):
#         print(f"Debit card payment {amount}")

# # obj = CCPayment()
# # obj.payment(100)
# # obj.print_slip(100)
# # print(isinstance(obj, Payment))


# obj = DCPayment()
# obj.payment(1000)
# obj.print_slip(1000)
# print(isinstance(obj, Payment))


