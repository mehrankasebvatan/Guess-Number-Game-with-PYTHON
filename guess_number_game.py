import random

name = input("Enter your name : ")
print("Hello , " , name , ". Welcome to guess number game . ")

smaller_number = int(input("Choose smaller number : "))
bigger_number = int(input("Choose bigger number : "))

number = int(random.randint(smaller_number , bigger_number))

print("Alright , Lets start .")
guess = int(input("Now guess a number between that 2 numbers you chosen : "))
count = 1

while guess != number :
    count += 1
    if guess < number :
        print("Too low !")
    else :
        print("Too high !")
    guess = int(input("new guess : "))
    
print(name , " , You are the smarter human in all the world ! ")
print ("You can guess the number with" , count , "try ! ")
