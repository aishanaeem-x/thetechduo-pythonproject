def aisha():
    print("Smart Calculator")

    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1-4): ")

    if choice == "1":
        print("Result:", x + y)
    elif choice == "2":
        print("Result:", x - y)
    elif choice == "3":
        print("Result:", x * y)
    elif choice == "4":
        if y != 0:
            print("Result:", x / y)
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid choice")

import random

def shanzeh():
    number = random.randint(1, 50)
    attempts = 0
    print("\nGuess the number between 1 and 50!")

    guess = 0
    while guess != number:
        guess = int(input("Your guess: "))
        attempts += 1

        if guess < number:
            print("Too low")
        elif guess > number:
            print("Too high")

    print("Correct! You guessed it in", attempts, "tries.")

def main():
    print("MAIN MENU")
    print("1. Smart Calculator")
    print("2. Guessing Game")

    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        aisha()
    elif choice == "2":
        play = "yes"
        while play.lower() == "yes":
            shanzeh()
            play = input("Play again? (yes/no): ")
    else:
        print("Invalid choice")



main()