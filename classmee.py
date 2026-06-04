class Person():
    def __init__(c,age):
        print("this is a constructor")
        c.age=age
    def age_me(c):
        print(f"age:{c.age}")

P=Person(23)
P.age_me()

#Encapsulation: TV Remote (buttons and motherboard)
#Inheritance:
#Polymorphism
#Abstraction