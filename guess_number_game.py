from os import truncate
import random


def is_valid_continue_input(user_input):
    if user_input in ['y', 'Y', 'n', 'N']:
        return True
    return False


def get_continue_input():
    while True:
        continue_input = input("Do you want to continue? [y/n] : ")
        if is_valid_continue_input(continue_input):
            return continue_input


def main():
    name = input("Enter your name : ")
    print("Hello , ", name, ". Welcome to guess number game . ")

    smaller_number = int(input("Choose smaller number : "))
    bigger_number = int(input("Choose bigger number : "))

    number = int(random.randint(smaller_number, bigger_number))

    print("Alright , Lets start .")
    guess = int(input("Now guess a number between that 2 numbers you chosen : "))
    count = 1

    while guess != number:
        count += 1
        if guess < number:
            print("Too low !")
        else:
            print("Too high !")

        user_continue_input = get_continue_input()
        if user_continue_input in ['n', 'N']:
            break

        guess = int(input("new guess : "))

    if guess == number:
        print(name, " , You are the smarter human in all the world ! ")
        print("You can guess the number with", count, "try ! ")
    else:
        print("Game over ! ")
        print("Number is ", number)


main()
