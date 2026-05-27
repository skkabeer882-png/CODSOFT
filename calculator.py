# simple calculator

def calculator():

    # input numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # choosing operation
    operator = input("Enter operation (+, -, *, /): ")

    # calculating using match-case
    match operator:

        case '+':
            print("Result:", num1 + num2)

        case '-':
            print("Result:", num1 - num2)

        case '*':
            print("Result:", num1 * num2)

        case '/':
            if num2 == 0:
                print("Division by zero not allowed")
            else:
                print("Result:", num1 / num2)

        # invalid operation
        case _:
            print("Invalid choice")


# function calling
calculator()
