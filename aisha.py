def smart_calculator():
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

smart_calculator()
