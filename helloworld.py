#Exercise: write a single line command explaining everything
#This program prints a greeting
print("Hello! Ajith Python???")

"""
Exercise: write a multi line comment
This is a multi line command
"""

#Exercise : Create variables for your name and age, then print them
name = '1lice'
age =15
print(f"name is {name} and its type is {type(name)} and age is {age}")
y=float(age)
print(f"y is {y} and its type is {type(y)}")
print(age==y)

#Exercise: create variables for two numbers and print their sum
num1=1.23
num2=3
sum=num1+num2
print("sum:",sum)

#Exercise: Arithmetic operations
x=7
y=3
print(f"x+y = {x+y} and x*y = {x*y}")
print(f"{x}//{y}={x//y}")
import time,datetime
print(datetime.date.today())
#Date 5-20-2026
ls=[1,2,23,3,34,434,34,'ljdfnhwh']
for i in ls:
    print(i,end=' = ')
print()
a= range(15)
for i in a:
    if i>6:
        print(i)
l=[i for i in a if i>6]
print(l) if 1>0 else print(l)

na='sai sujith'
"""
while(1):
    if input()=='z':
        break
    else:
        print("Po Ra!!!")
"""
i=0
while(i<18):
    print(i)
    i+=1

#sum of even numbers:
t=0
for i in range(1,15):
    if i%2==0:
        t+=i
print(t)

secret=7
guess=0
cnt=1
while guess !=secret and cnt<=3:
    guess=int(input(f"ENter the number between 1 and 10:"))
    if guess==secret:
        print("Yahoo!!!")
        break
    elif guess>secret:
        print("Guess too high")
    else:
        print("Guess too low")
    cnt+=1
#Give four inputs and do +/-/*/%/ / / < />/==
a=int(input("ENter the number(int or float):"))
b=int(input("ENter the number(int or float):"))
c=int(input("ENter the number(int or float):"))
d=int(input("ENter the number(int or float):"))

print('Addition:')
print(f"a+b = {a+b}\na+c ={a+c}\na+d={a+d}\nb+c={b+c}\nb+d={b+d}\nc+d={c+d}\n")

print('Subtraction')
print(f"a-b = {a-b}\na-c ={a-c}\na-d={a-d}\nb-c={b-c}\nb-d={b-d}\nc-d={c-d}\n")

print('Multiplication')
print(f"a*b = {a*b}\na*c ={a*c}\na*d={a*d}\nb*c={b*c}\nb*d={b*d}\nc*d={c*d}\n")

print('Division')
print(f"a/b = {a/b}\na/c ={a/c}\na/d={a/d}\nb/c={b/c}\nb/d={b/d}\nc/d={c/d}\n")

print('Modulo Division')
print(f"a//b = {a//b}\na//c ={a//c}\na//d={a//d}\nb//c={b//c}\nb//d={b//d}\nc//d={c//d}\n")


# small(1-10) medium (10-100) large(>100)
sml = int(input("ENter the number:"))

if sml<10:
    print('small')
elif sml>=10 and sml<100:
    print('medium')
else:
    print('large')
"""
def function_name(parameters):
    statemnts
    return soemthing
    
"""


