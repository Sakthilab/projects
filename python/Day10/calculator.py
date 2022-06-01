from art import logo
import os

def add(n1, n2):
    return n1+n2

def sub(n1, n2):
    return n1-n2

def mul(n1, n2):
    return n1*n2

def div(n1, n2):
    return n1/n2

operations  = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div    
}

def calculator():
    print(logo)
    n1 = int(input("What's the first number? "))
    for i in operations:
            print(i)
    choice = True

    while choice:
        op = input("pick an operation : ")    
        n2 = int(input("What's the next number? "))    
        calc = operations[op]
        result = calc(n1, n2)
        print(f"{n1} {op} {n2} = {result}")
        c=input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, or type 'q' to exit: ")
        if  c == "y":
            n1 = result
        elif c == "n" :
            os.system('cls')          
            calculator()
        else:
            choice = False

calculator()