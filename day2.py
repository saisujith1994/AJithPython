def printing_hello():
    print("Hey World")

def greet_students(name,score):
    print("Hello,",name,"!!")
    print("Your score is ",score)
    if score>=9.0:
        print("well done!!")
    elif score >=8.0:
        print("can do better!!")
    else:
        print("keep practicing!!")
printing_hello()
greet_students("Honey",9.8)
greet_students("Raju",8.8)
greet_students("Mahesh",7.8)
greet_students(score=10.0,name='Sneha')

def adding_num(a,b=2):
        a+b
res=adding_num(3,4)
print(adding_num(7,3),res)

def calculator():
    flag=True
    def addition(a,b):
        return a+b
    def subtraction(a,b):
        return a-b
    def multiplication(a,b):
        return a*b
    def division(a,b):
        return a/b
    while(flag):
        print("calculator")
        print("Enter you choice from the options")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quit")
        c=int(input("Enter your choice:"))
        if c==1:
            a=int(input("Enter your first number:"))
            b=int(input("Enter your second number:"))
            addition(a,b)
        elif c==2:
            a=int(input("Enter your first number:"))
            b=int(input("Enter your second number:"))
            subtraction(a,b)
        elif c==3:
            a=int(input("Enter your first number:"))
            b=int(input("Enter your second number:"))
            multiplication(a,b)
        elif c==4:
            a=int(input("Enter your numerator:"))
            b=int(input("Enter your denominator:"))
            if b==0:
                print("Cannot divide by zero")
            else:
                division(a,b)
        elif c==5:
            flag=False
            return "Closing....."
print(calculator())