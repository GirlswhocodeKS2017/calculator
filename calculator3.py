#!/usr/bin/python

""" User input is going to be a aritmatic expression """

def add(n1,n2):
    return float(n1)+float(n2)

def sub(n1,n2):
    return float(n1)-float(n2)

def multiply(n1,n2):
    return float(n1)*float(n2)

def divide(n1,n2):
    if int(n2) == 0:
        print("cannot divide by zero")
        exit(0)
    else:
        return float(n1)/float(n2)

def power(n1,n2):
    return float(n1)**float(n2)

def sqrt(n):
    return float(n)**(0.5)


def main():

    """ Must separate everything by a space because regex is beyond the scope
    of this class and it makes negative numbers easier."""
    
    start_up = """\n \n     Welcome to my Calculator. Enter q to quit: \n 
    All entries must be separated by whitespace. \n """
    print(start_up)
    contin = True
    while contin:
        expression = input("")
        exp = expression.split() # Split by whitespace. Makes neg nums easier
        if len(exp) == 1:
            if exp[0].startswith('sqrt'):
                ## Assumes input is sqrt(x)
                num = exp[0][5:-1]
                print(sqrt(num))
            elif exp[0] == 'q': ## to quit the while loop
                contin == False
                exit(0)
        else:
        
            if exp[1] == '+':
                print(add(exp[0],exp[2]))
                
            elif exp[1] == '-':
                print(sub(exp[0],exp[2]))
        
            elif exp[1] =='*':
                print(multiply(exp[0],exp[2]))
        
            elif exp[1] =='/':
                print(divide(exp[0],exp[2]))
        
            elif exp[1] == '^':
                print(power(exp[0],exp[2]))
                   
            else:
                print("I need to write more code")
    
    return


if __name__ == "__main__":
    main()

