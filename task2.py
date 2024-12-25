
def calculator():
    print("Welcome to the Simple Calculator!")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter the number corresponding to the operation (1/2/3/4): ")

    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice! Please restart the calculator and try again.")
        return

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    if choice == '1':
        result = num1 + num2
        operation = "+"
    elif choice == '2':
        result = num1 - num2
        operation = "-"
    elif choice == '3':
        result = num1 * num2
        operation = "*"
    elif choice == '4':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
        operation = "/"

    print(f"\nResult: {num1} {operation} {num2} = {result}")

calculator()
