import math
import tkinter

def calculator():
    get_sign = input("Welcome the calculator please enter the function you want to do? ")
    
    if get_sign == '+':
        a, b = input("Enter a two value: ").split() 
        a = float(a)
        b = float(b)
        result = add(a,b)
        print(f"{result}")

    elif( get_sign == "-"):
        a, b = input("Enter a two value: ").split() 
        a = float(a)
        b = float(b)
        result = sub(a,b)
        print(f"{result}")

    elif(get_sign == "*"):
        a, b = input("Enter a two value: ").split() 
        a = float(a)
        b = float(b)
        result = multiply(a,b)
        print(f"{result}")

    elif get_sign == "/":
        a, b = input("Enter a two value: ").split() 
        a = float(a)
        b = float(b)
        result = divide(a,b)
        print(f"{result}")
    else:
        print("Not the correct sign please try again")
        calculator()


    



def add(x, y):
    result = x + y
    return result
def sub(x,y):
    result = x - y
    return result
def multiply(x,y):
    result = x * y
    return result
def divide(x, y):
    result = x / y
    return result

calculator()
