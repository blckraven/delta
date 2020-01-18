from math import *
from sys import exit
from time import sleep

print("\nThis program will solve your quadratic equation\n")
print("###################")
print("#  ax^2 + bx + c  #")
print("###################")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

def quadric_equation(a,b,c):
    if a==0:
        print("It's not a quadratic equation!")
        sleep(3)
        exit(0)
    else:
        delta = b*b - 4*a*c
        if delta < 0:
            print("The equation has no roots!")
            sleep(3)
            exit(0)
        elif delta == 0:
            x = -b / (2*a)
            print("x =", x)
            sleep(5)
            exit(0)
        else:
            x1 = (-b - sqrt(delta)) / (2*a)
            x2 = (-b + sqrt(delta)) / (2*a)
            print("x1 = ", x1, "\tx2 = ", x2)
            sleep(10)
            exit(0)

quadric_equation(a,b,c)