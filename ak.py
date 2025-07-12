#object orieanted programming
#instance
# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
   
#     def greet(self):
#         print(f"Hello {self.name} of age {self.age}")

# a = person("Alice",29)#object
# print(a.name)
# a.greet()
# b = person("Akash",20)
# print(b.name)
# b.greet()

# class car:
#     def __init__(self,brand,color,year):
#         self.brand= brand
#         self.color= color
#         self.year= year
#     def drive(self):
#         print(f"Brand of the car {self.brand} of color {self.color} and year of {self.year}")
# a = car("BMW","white",2025)#object
# # print(a.name)
# a.drive()
# # inheritance
# class Father:
#     def fatherwealth(self):
#         print("papa ka paisa")

# class Mother:
#     def hobbies(self):
#         print("multiple inheritance")

# class Akash(Father,Mother):
#     def salary(self):
#         print("Earned on my own")

# f = Father()
# c = Akash()
# c.salary()
# c.hobbies()
# c.fatherwealth()
# f.fatherwealth()


# class Vehicle:
#     def __init__(self,brand):
#         self.brand = brand 

# class car(Vehicle):
#     def __init__(self,brand,model):
#         super().__init__(brand)
#         self.model= model
    
# c= car("BMW","auto")#object
# print(c.brand,c.model)

# #polymorphism
# class Bird:
#     def sound(self):
#         print("chirp")

# class Cat:
#     def sound(self):
#         print("Meow")

# sparrow = Bird()
# sparrow.sound()
# kitten = Cat()
# kitten.sound()

# #method overriding
# class Parent:
#     def show(self):
#         print("parent's method")

# class Child(Parent):
#     def show(self):
#         print("child's method")
# obj = Child()
# obj.show()

# #operator overloading
# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def __add__(self,other):
#         return Point(self.x+other.x ,self.y+other.y)

# p1 = Point(2,3)
# p2 = Point(3,4)
# p3 = p1+p2
# print(p3.x,p3.y)

# class Student:
#     def __init__(self, name , roll):
#         self.name = name
#         self.roll = roll

#     def __eq__(self, other):
#         return self.roll == other.roll
    
# s1 = Student("Alice", 101)
# s2 = Student("Bob", 101)
# s3 = Student("Camen", 102)
# print(s1 == s2)
# print(s1 == s3)

# class Book:
#     def __init__(self, title , page):
#         self.title = title
#         self.page  = page
#     def __add__(self,other):
#         return (self.page+other.page)
# p1 = Book("sss",320)
# p2 = Book("abc",100)

# print(p1+p2)

# #Encapsulation
# # access specifiers
# class Protected:
#     def __init__(self):
#         self._age = 30 #protected attribute _age

# class Sub(Protected):
#     def display_age(self):
#         print(self._age)#protected member accesible in subclass

# obj = Sub()
# obj.display_age()

# class Bankacc:
#     def __init__(self,balance):
#         self.__balance = balance#balance is private
#     def deposit(self,amount):
#         self.__balance+=amount
#     def get_balance(self):
#         return self.__balance

# acc = Bankacc(1000)
# acc.deposit(500)
# print(acc.get_balance())        
# #Abstraction
# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def start_engine(self):
#         pass

# class Car(Vehicle):
#     def start_engine(self):
#         print("Car engine started")

# class Bike(Vehicle):
#     def start_engine(self):
#         print("Bike engine started")

# c = Car()
# c.start_engine()
# b = Bike()
# b.start_engine()
                

# #Exception handling
# try: 
#     num = int(input("Enter a number:"))
#     x=10/num
# except ZeroDivisionError:
#     print("Canot divide by 0")
# except ValueError:
#     print("Please enter valid number")
# else:
#     print("Success")
#     print(x)
# age = int(input("Enter your age:"))
# if age<18:
#     raise ValueError("Voter age must be above 18")
# else:
# #     print("Cast your vote")
# try:
#     name = int(input("Enter your name:"))
#     if (name==""):
#          raise ValueError("not be empty enter any value")
# #else:
#    # print("Your:",name),
# except ValueError:
#     print("Error handled ")

# #1.write a programme to find if the given string is a palindrom or not.
# input_text = input("Enter a string: ")

# if input_text == input_text[::-1]:
#   print("is palindrome!")
# else:
#   print("is not palindrome.")
# #2.write a function to find the 2nd largest element of the list without using the sort function.
# def find_second_largest(numbers):
  
#   if not isinstance(numbers, list):
#     raise TypeError("Input must be a list.")
#   if len(numbers) < 2:
#     return None  
  
#   largest = -float('inf')
#   second_largest = -float('inf')

  
#   unique_numbers = []
#   for num in numbers:
#       if num not in unique_numbers:
#           unique_numbers.append(num)
#       if len(unique_numbers) >= 2:
#           break

#   if len(unique_numbers) < 2:
#       return None 

  
#   if unique_numbers[0] > unique_numbers[1]:
#       largest = unique_numbers[0]
#       second_largest = unique_numbers[1]
#   else:
#       largest = unique_numbers[1]
#       second_largest = unique_numbers[0]

  
#   for num in numbers:
#     if num > largest:
#       second_largest = largest
#       largest = num
#     elif num > second_largest and num != largest:
#       second_largest = num

 
#   if second_largest == -float('inf'):
#       return None

#   return second_largest

# # Test cases
# print(f"List [10, 5, 20, 15, 25]: {find_second_largest([10, 5, 20, 15, 25])}") 
# print(f"List [5, 5, 5, 5]: {find_second_largest([5, 5, 5, 5])}") 
# print(f"List [1, 2]: {find_second_largest([1, 2])}") 

#3.create a function that counts the number of vowels in a given string.

# str = input("enter ur name")
# def search_vowels(input_string):
#  vowels = "aeiouAEIOU"  
#  return sum(1 for char in input_string if char in vowels)
# print(search_vowels(str))
#4
def MaxMin(li):
    mi=li[0]
    mx=li[0]
    for i in li:
        if i<mi:
            mi=i
        if i>mx:
            mx=i
    print(mx)
    print(mi)
li=[8,2,4,3,6,1,6]
pr=MaxMin(li)
print(pr)
#5.Design a student and Marks class
class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def display_student_info(self):
        print(f"Name: {self.name}, Roll Number: {self.roll_number}")



class Marks(Student):
    def __init__(self, name, roll_number, sub1_marks, sub2_marks, sub3_marks):
        super().__init__(name, roll_number)  
        self.sub1_marks = sub1_marks
        self.sub2_marks = sub2_marks
        self.sub3_marks = sub3_marks

    def calculate_total_and_average(self):
        total = self.sub1_marks + self.sub2_marks + self.sub3_marks
        average = total / 3
        return total, average

    def display_marks_info(self):
        self.display_student_info()  
        print(f"Subject 1 Marks: {self.sub1_marks}")
        print(f"Subject 2 Marks: {self.sub2_marks}")
        print(f"Subject 3 Marks: {self.sub3_marks}")
        total, average = self.calculate_total_and_average()
        print(f"Total Marks: {total}, Average Marks: {average:.2f}")








