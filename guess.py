import random

r1= random.randint(1,10)
print(r1)

def guess() :

    h1= int(input("Guess a Number Between 1-10"))
    if(h1!=r1) :
        if(h1>r1) :
            print("Guess Lower")
            h1= int(input("Guess a Number Between 1-10"))
            guess2()

        if(h1<r1) :
            print("Guess Higher")
            h1= int(input("Guess a Number Between 1-10"))
            guess2()
    
        if(h1==r1) :
            print("Congratulations You Won") 

def guess2() :

    h1= int(input("Guess a Number Between 1-10"))
    if(h1!=r1) :
        if(h1>r1) :
            print("Guess Lower")
            h1= int(input("Guess a Number Between 1-10"))
            guess()

        if(h1<r1) :
            print("Guess Higher")
            h1= int(input("Guess a Number Between 1-10"))
            guess()
    
        if(h1==r1) :
            print("Congratulations You Won") 

guess()