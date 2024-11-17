from random import randint

def area ():
    # this is a sequence i.e. a collcetion of characters
    question1 = "Enter a length:"

    a=int(input(question1))
    b=int(input("Enter a width:"))
    c= a * b
    print("area=",c)
area()

def addition ():
    d=float(input("Enter a decimal number:"))
    e=float(input("Enter another decimal number:"))
    f= d+e
    print("Adition answer=",f)

# this is selection
    if f == 0:
        print("f = 0")
    elif f == 10:
        print("f = 10")
    else:
        print("f is something else")

numberOfQuestion = 3
numerOfTimesAsked = 0

#this is iteration
while numerOfTimesAsked<numberOfQuestion:
    numerOfTimesAsked+=1

    addition()


def usrname ():
    g=input("Please enter your user name:")
    print("Hello:",g)
area()

def usrpasswrd ():
    h=input("Enter a strong multiple character password using symbols and numbers:")
    print("Your password is:",h)
    print("Remember that!")


usrpasswrd()

import random


def dice_game ():
    dice1=randint(1,9)
    dice2=randint(1,9)

    print(dice1,dice2)

dice_game()

















