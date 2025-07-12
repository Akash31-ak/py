
"""#string
s1='python'
s2="programming"

print(s1)
print(s2)
print(s3)
print(s1[3])
print(s1[-2])
print(s1[1:4])
#common string methods
str1="Alice, in, wonderland"
#lower() -converts string to lower case
print(str1.lower())
#upper() -
#title() -capitalizes each word
#strip() -removes spaces from the start and end of the string
#replace("a","b") -a will be replaced by b
#find("sub") -finds the substring in the string
#count("sub") 
#startswith()
#endswith()
#split()method returns a list where the text between the specified seperator
#becomes the list items
print(str1.split(","))
print(str1.title())
print(str1.replace("Alice","Akash"))
print(str1.find("alice"))
print(str1.count("wonderland"))
print(str1.strip())
print(str1.startswith("A"))
print(str1.endswith("d"))
print("".join(['hello','world']))

name="AK"
roll=35
branch="CSE"
print("My name is",name,"roll no is",roll,"and branch is",branch)
print("My name is "  +name+" roll no is "+  str(roll)+" and branch is " + branch)

#string formatting (available in python)
#f string
print(f"my name is {name} roll no is {roll} and branch is {branch}")
#.format
print("my name is {} roll no is {} and branch is {}".format(name,roll,branch))

print("Good"+"Morning")#concatination
print("ha"*4) #repitition
print("py" in "python")#membership operation(t\f)

#conditional statements
if 20<30:
    print("if block executed")
else:
    print("else block executed")   

result=input("enter ur marks:")
marks=int(result)
if marks>=90:
    print("grade A")
elif marks>=80:
    print("grade B")
elif marks>=70:
    print("grade c")   
elif marks>=60:
    print("grade d")  
else:
    print("grade e")       

age=int(input("enter ur age"))
if age>=18:
    print("you  are eligible to vote")
else:
    print("unable to vote")    """
#while loop
i=0
while i<5:
    print(i)
    i+=1
#for loop
for j in range(1,5):
    print("for loop no",j)
for j in range(1,10,2):#ifstart, end-1,increment
    print("for loop no",j)  

for j in range(10,1,-2):
    print(j)  