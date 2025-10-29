# a=[1,2,3]
# b=[1,2,3]
# print(id(a))
# print(id(b))
# print(a is b)

# x=0
# while x < 10:
#     print(x)
#     x += 1

# def lower_triangular(n):
#     for i in range(n):
#         for j in range(i + 1):
#             print("*", end=" ")
#         print()
        
# name = input("name : ")
# age = int(input("age: "))
# # price = float(input("price: "))

# print("my name is", name , "and my age is", age)

# base = float(input("enter base of trainagle: "))
# height = float(input("enter height of traiangle : "))
# area = 1/2*base*height
# print("Area of traingle is : ", area)
 
# a=int(input("enter side of square: "))
# print("area=", a * a)

# a = float(input("enter one value: "))
# b = float(input("enter second value: "))
# print("average=", a+b/2)

# a = int(input("enter one value: "))
# b = int(input("enter second value: "))
# if(a>=b):
#     print(True)
# else:
#     print(False)
    
# str= "Hello Prenjel"
# print(str.replace("e", "a"))
# print(str.find("n"))

# a = input("enter your name: ")
# print("length of your name is" , len(a))

# a = int(input("Enter you age: "))
# if (a>=18):
#     print("Eligible to vote")
# else:
#     print("Not eligible to vote ")
    
# a=int(input("enter marks of student: "))
# if (a>=90):
#     print("Student got Grade A")
# elif(a>=80 and a<90):
#     print("Student got Grade B")
# elif(a>=70 and a<80):
#     print("Student got Grade C")
# else:
#     print("Student got Grade D")
    
# a = int(input("Enter any number: "))
# if (a%2 == 0):
#     print("Number is even")
# else:
#     print("Number is odd")

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# if(a>=b and a>=c):
#     print("a is greater")
# elif(b>=a and b>=c):
#     print("b is greater")
# else:
#     print("c is greater")
    
# a = int(input("Enter any number: "))
# if (a%7 == 0):
#     print("Number is multiple of 7")
# else:
#     print("Number is not multiple of 7")

# i = 1
# while i<=4:
#     print("Hello Guys")
#     i+=1
# print(i)


# i = 1
# while i <= 10:
#     print(8*i)
#     i += 1

# num = [4,78,45,9,22,100,88,69]
# x=69
# i = 0
# while i<len(num):
#     if (num[i] == x):
#         print("found at idx",i)
#     else:
#         print("finding ")
#     i += 1
    
# i=1
# while i<=20:
#     print(i)
#     if (i == 12):
#         break
#     i+=1
# print("End of Choice")

# num=(1,5,7,9,56,100,45,69,78,100)

# x = 100
# i = 0
# while i<len(num):
#     if(num[i]==x):
#         print("length of idx", i)
#     else:
#         print("finding")
#     i+=1
    
# i = 0
# while i<=10:
#     # print(i)
#     if (i == 5):
#         i +=1
#         continue
#     print(i)
#     i +=1
    
    
# i = 0
# while i<=20:
#     if (i%2 == 0):
#         i+=1
#         continue
#     print(i)
    # i +=1
    
# i = 0
# while i<=10:
#     print(i)
#     i += 1

# n=int(input("Enter number you want to print table of: "))
# for i in range(1,11):
#     print(n * i)
    
# n = 5
# fac = 1
# for i in range(1, n+1):
#     fac *= i
# print("Factorial=", fac)

# t = (1,5,7,9,4)
# t = t + (8,)
# print(t)

# b = 1,2,'three'
# print(type(b))

# fruitlist = ('apple', 'banana', 'orange')
# app,ban,ora= fruitlist
# print(ban)
# # print(ban)

# f= open("demo.txt", "a")
# f.write("\nI want to be proud of myself.")
# print(f)
# # line1 = f.readline()
# # print(line1)

# # line2 = f.readline()
# # print(line2)

# f.close()

# f = open("demo.txt", "r+")
# f.write("okauy")
# f.close()

# f = open("demo.txt","a")
# data = f.write("\nIt is true.")
# print(f)

# with open("demo.txt","r") as f:
#     data = f.read()
#     print(data)
    
# import os 
# os.remove("demo.txt")

# f = open("practice2.txt","w")
# data = f.write("Hi everyone \nWe are learning file I/O \nusing java. \nI like programming in Java. ")

# word = ("learning")
# with open("practice2.txt","r") as f:
#     data =f.read()
#     if(data.find(word) != -1):
#         print("Found")
#     else:
#         print("Not Found")
# new_data = data.replace("Java", "Python")
# print(new_data)

# def cal_sum(a,b):
#     sum = a+b
#     print(sum)
#     return sum 

# cal_sum(89,1)

# info = {
#     "name" : "Pranjal",
#     "age" : 23,
#     "subjects" :  {
#         "hindi" : 56,
#         "eng" : 78,
#         "math" : 87
#         }
# }

# print(info.items())

# d = {"name" : "pranjal" , "okay" : "789" }
# d.clear()
# print(d.get("name"))
# print(d["name"])

# d.update({"city" : "jodhpur"})
# print(d)

# d.popitem()
# print(d)

# def avg_num(a,b,c):
#     sum = a+b+c
#     avg = sum/2
#     print(avg)
#     return avg 

# avg_num(12,24,36)

# city = ["delhi","noida","udaipur","jaipur"]
# def calc_len(city):
#     for items in city:
#         print(items, end=" ")
# calc_len(city)
# print()

# def calc_fac(a):
#     fact = 1
#     for i in range(1, a+1):
#         fact *=i
#     print(fact)
# calc_fac(10)


# def curr_converter(usd_val):
#     inr_value = usd_val*83
#     print(usd_val, "USD =", inr_value, "INR")
# curr_converter(78)

# def show(n):
#     if (n==0):
#         return 
#     print(n)
#     show(n-1)
# show(10)

# def fact(n):
#     if (n == 1 or n == 0):
#         return 1
#     return fact(n-1)*n  
# print(fact(5))

# def sum(n):
#     print(n)

# class car():
#     car = "okay"
#     def __init__(self):
#         print("Is this a good example?")
# #     color = "black"
# #     brand = "range rover"
# #     speed = "78km/h"
# # Car1 = car()
# # print(Car1.brand, Car1.speed, Car1.color)
# c1= car()

# class student:
#     def __init__ (self, name, marks):
#         self.name = name
#         self.mark = marks
#         print("adding new database ")
# s1 = student("karan")
# print(s1.name)
# s2= student(48)
# print(s2.marks )

# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
        
#     @staticmethod
#     def hello():
#         print("Hello VS Code")
        
#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val 
#         print("Hello", self.name, "your average score is: ", sum/3 )
        

# s1= student("Pranjal Soni", [78,98,100])
# s1.get_avg()
# s1.hello()

# class account():
#     def __init__(self,balance,acc_number):
#         self.balance = balance
#         self.acc_number = acc_number
        
#     def credit(self,amount):
#         self.balance += amount
#         print("Rs.", amount, "was credited")
#         print("total balance=", self.get_balance())
    
#     def debit(self,amount):
#         self.balance -= amount
#         print("Rs.", amount, "was debited")
#         print("total balance=", self.get_balance())
    
#     def get_balance(self):
#         return self.balance


# acc1= account(100000, 1489)
# # print(acc1.balance)
# # print(acc1.acc_number)
# acc1.debit(1000)
# acc1.credit(500)
# acc1.salary(4000)

# class student():
#     def __init__(self,name):
#         self.name= name
# s1 = student("Pranjal")
# print(s1.name)
# del s1.name
# print(s1.name)

# class car:
#     color = "Black"
#     @staticmethod 
#     def start():
#         print("Car has started..")
#     def stop():
#         print("Car has stopped...")
        
# class ToyotaCar(car):
#     def __init__(self,name):
#         self.name = name
# car1 = ToyotaCar("Fortuner")
# car2 = ToyotaCar("Ox")
# # print(car2.color)s
# print(car1.start())
        
# class student:
#     name = "Pranjal"
# s1= student()
# print(s1.name)

# class student:
#     college_name= "JIET"
#     def __init__(self, name,marks):
#         self.name= name 
#         self.marks=marks
#         print("adding new Database...")
        
# s1= student("Pranjal", 100)
# print(s1.name, s1.marks,s1.college_name)

# import copy
# l1= [1,8, [0.6,0.2], 7, 'Python']

# # l2= copy.copy(l1)
# # print(l2)
 
# # employee = {'name': "Shree", 'id': 1008, 'salary': 8000}
# # print(employee.items())
# # for i in employee.items():
# #     print(i)

# # for i in range(10, 0, -1):
# #     print(i)
    
# # scores = [2,45,102,4,9,12,45,90,1,0,1,200]
# # total = 0
# # for scores in scores:
# #     total =  total + scores
# # print(f"Total scores is  {total}")

# # highest  = scores[0]
# # for score in scores:
# #     if score > highest:
# #         highest = score
# # print(f"Highest score is {highest}")

# # num = 25
# # while num>=9:
# #     print(num)
# # #     num -= 2
    
# # import random
# # # print(random.random())
# # # print(random.randint(10,54))
# # # print(random.choice(scores))
# # print(random.shuffle(scores))

# # x = int(input("Enter a number: "))
# # for x in range (1,x):
# #     for j in range (1,x+1):
# #         print("x", end=" ")
# #     print()

# # import random
# # print("Welcome to the Rolling Dice Simulator!")
# # while True:
# #     choice = input(" To begin with game press 'Enter' or to exit press 'q': ")
# #     if choice == 'q':
# #         print("Thanks for playing! Goodbye.")
# #         break
# #     elif choice == '': 
# #         number = random.randint(1,6)
# #         print(f"You chose number {number}")
# #     else:
# #         print("Invalid input. Please try again.")
        
# # city = ["Jodhpur", "Indore","Jaipur", "Kota", "Udaipur", "Jalore"]
# # counter = 0
# # output = []
# # for city in city :
# #     if city.startswith('J') :
# #         counter = counter + 1
# #         output.append(city)
# # print(counter)
# # print(output)

# num = 1
# print("Wecome to the guessing number game. Guess a secret number between 1 to 50. \nYou have 10 attempts")
# secret_number = 35

# attempts = 10

# while num <=10:
#     print(f"You have {attempts} attempts reamining. ")
#     user_number = int(input("Enter the number you guessed: "))
#     if user_number == secret_number :
#         print("Wohho! You guessed correct number.")
#         break
#     else:
#         if user_number < secret_number:
#             higher_or_lower = "higher"
#         else:
#             higher_or_lower = "lower"
#         print(f"Your guess is wrong. Try {higher_or_lower} number.")

#     num += 1
#     attempts -= 1 
# print("GAME OVERRR! ")

# def check_div(num):
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("odd")
#     print(check_div)
#     return(check_div)
# check_div(1795255)

# def avg_num(a,b):
#     sum = a+b
#     avg_num = sum/2
#     print(avg_num)
#     return(avg_num)
# avg_num(8,2)

l1 = [4,78,56,100,78,65]
def calc_len(l1):
    
    print(len(l1))
    print(l1)
calc_len(l1)


