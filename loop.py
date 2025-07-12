# #while loop
# i=0
# print(i)
# while i<5:
#     print(i)
#     i+=1

# for j in range(1,5):
#     print("for loop no",j)

# for j in range(1,10,2):#ifstart, end-1,increment
#     print("for loop no",j)  

# for j in range(10,1,-2):
#     print(j)   

# for j in range(1,11):
#     if j==5:
#         break
# print(j)

# for a in range(1,10):
    
#     if a==7:
#         continue
#     print(a)

#     for letter in "words":
#         print(letter)
    
#     for i in range(5):
#         pass #do nothing for now or code to be added late
# psd="Abc"
# for i in range(3):

#     pswd=input("enter ur password:")

#     if (pswd==psd):
#        print("welcome!")
#        break
#     else:
#        print("Access Denied")

# #Functions
# def greet():#defining function
#     print("python if fun")

# greet()#calling the function

# def greet_user(user):
#     print("Hello",user)
# greet_user("charlie")

# #variable length arguments
# # *args: passes tuples as arguments,,**kwargs - to pass dictionary arguments
# def greetTuple(*args):
#     for name in args:
#         print(f"Hello,{name}!")

# greetTuple("Alice","Bob","Charlie")

# def display_info(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}:{value}")
    
# display_info(name="David",college="Pu",profession="Sales")

# def demo(*args,**kwargs):
#     print("Args tuple elements", args)
#     print("Kwargs dictionary elements",kwargs)

# demo(1,2,"apple",name="David",college="Pu",profession="Sales")

# def squareFunc(x):
#     return x**2
# ans=squareFunc(4)
# print(ans)
# print(squareFunc(5))

# #def calc():
# A=int(input("Enter value1:"))
# B=int(input("Enter value2:"))
# operation=input("Enter operation(+-*/**):")
# if operation =="+":
#        print(A+B)
# elif operation =="-":
#         print(A-B)
# elif operation =="*":
#         print(A*B)
# elif operation =="/":
#         print(A/B)
# elif operation =="**":
#         print(A**B)
# else:
# #         print("incorrect")
# x = lambda a: a+10
# print(x(5))
# y=lambda a,b,c : a+b+c
# print(y(2,3,4))

# #modules    
# import math
# print(math.sqrt(144))
# print(math.sqrt(188))
#print(math.pi)


# import random
# print(random.randint(1,10))

# from math import sqrt
# print(sqrt(16))

# import datetime as dt #alias
# print(dt.datetime.now())

# import mymodule
# mymodule.mymodulefunction()


# x=10#global
# def showNum():
#     x=5#local
#     print("Value of x as a local variable",x)
# showNum()
# print("value as a global variable", x)

# f = open("file.txt",'r')  
# content = f.readline()
# print(content)
# content1 = f.readlines()
# for l in content1:
#     print(l)

# text = f.read()
# print(text)

# f = open("file.txt",'w')
# f.write("Hello\n")
# f.write("Goodmorning\n")
# lines = ["line 1\n","line 2\n","line 3\n"]
# f.writelines(lines)
# f.close()

# f = open("file.txt",'a')
# f.write("New Content")
# f.close()
# import os
# print(os.path.exists("file.txt"))
# print(os.path.exists("file2.txt"))
#os.rename("file.txt","newfile.txt")
# os.remove("newfile.txt")

#object oriented programming
#instance





