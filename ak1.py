print("hello world")
flag =True
a=10
b=15
print(flag)
print(a)
print(b)
a="bob"
print(a)
print(type(a))
print(type(flag))
print(10/3)
print(10//3)
print(2**8)
x,y,z="apple","orange","kiwi"
print(x,y,z)
print(5>6 and 5%2==0)
print(2<3 or 2%2==0)
print(not(34<78))

#name=input("Enter ur name")
#print(name)

a=0
b=bool(a)
print(b)
list1=["apple","car",1,4.0,True]
print(list1)
print(list1[1])
list1[1]="dog"
print(list1)
#append() - add element at the end of the list
list1.append("New Item")
print(list1)
#insert(index, item) - insert item at the given index
list1.insert(1,"grapes")
print(list1)
#extend([list]) - Adds elements from another list
list1.extend(["rose","lilly",1,2,3,4,5])
print(list1)
#remove(item) - Removes first occurence
list1.remove(1)
print(list1)
#pop(index) - removes and returns the item at the index(last by default)
list1.pop()
print(list1)
list1.pop(3)
print(list1)
#slice operation
print(list1[2:7])
#clear - removes all the elements in the list
list1.clear()
print(list1)

numbers =[45,23,15,67,87,98,54,33]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(numbers.count(15))




basket =["rose","lilly","jasmine","sunflower"]
basket.sort()
print(basket)
basket.reverse()
print(basket)
print(basket.count("lilly"))
print(basket.index("lilly"))

#Tuples
#tup1=(10,9,8,7)
#print(tup1)
#tuple without parentheses
colors="red","green","blue"
print(colors)
person=("Alice",23,"Engineer")
name,age,profession=person
print(person)
print(name)
print(profession)

tup1=(10,9,8,7)
print(tup1)
print(tup1[2])
print(tup1[-1])
print(len(tup1))#length of the tupple also vsalid in list
print(tup1.count(8))
print(tup1.index(9))

person=("john",25,"Developer")
name,age,profession=person
print(name)
print(age)

my_set ={1,2,3,4}
another_set =set([4,5,6])
print(my_set)
print(another_set)
empty_set={}
my_set.add(5)
print(my_set)
my_set.remove(2)
print(my_set)
my_set.discard(3)
print(my_set)
print(4 in my_set)
print(len(my_set))

a={1,2,3,4,}
b={0,5,7,6,}
print(a|b)
print(a.union(b))
print(a&b)
print(a.intersection(b))
print(a-b)
print(a.difference(b))
print(a^b)
print(a.symmetric_difference(b))
squares ={x**2 for x in range (1,6)}
print(squares)


student ={
    "name":"Alice",
    "age":20,
    "course":"python"
}
person =dict(name="john",age=25,course="python")
print(student)
print(person)
print(student["name"])
print(student.get("age"))
student["age"]=21
student["city"]="Koppal"
print(student)
print(person["name"])
print(person.get("age"))
student.pop("course")
del student["city"]
#student.clear()
#nested dictionary
students ={
    "101":{"name":"ak","grade":"A"},
    "102":{"name":"gk","grade":"B"}
}
print(students["101"]["name"])
print(students["102"]["name"])
print(type(students))
tuple1 =(1,2)
tuple2 =(3,4)
print(tuple1+tuple2)
print(tuple1*3)
print(tuple2*2)





