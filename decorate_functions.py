"""
In python,
I can pass functions as arguments
return functions from functions
store functions in variables
"""
def greet():
    print("hello")

def run_func(f):
    f()

def logger(func):
    def wrapper():
        print("Before function")
        result=func()
        print("After function")
        return result
    return wrapper
def say_hi():
    print("hi")
#say_hi=logger(say_hi)
#say_hi()

@logger
def greet():
    print("Gud mrng!!")
greet()
#run_func(greet)