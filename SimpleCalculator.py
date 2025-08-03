# A simple program to perform a mathematical operation on two numbers.

# Use a try-except block to handle potential errors, such as non-numeric input.
try:
    # Get the first number from the user and convert it to a floating-point number.
    num1 = float(input("Please enter the first number: "))
    
    # Get the second number from the user and convert it to a floating-point number.
    num2 = float(input("Please enter the second number: "))
    
    # Get the mathematical operator from the user.
    operator = input("Please enter an operator (+, -, *, /): ")

    # Initialize a variable to store the result.
    result = 0.0

    # Use an if-elif-else statement to perform the correct operation.
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        # Handle the edge case of division by zero.
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            # Exit the program or break out of the conditional logic.
            exit()
        result = num1 / num2
    else:
        # If the operator is not recognized, print an error message.
        print("Error: Invalid operator entered.")
        # Exit the program or break out of the conditional logic.
        exit()

    # Print the final result 
    print(f"{num1} {operator} {num2} = {result}")

except ValueError:
    # This block will execute if the user enters non-numeric input.
    print("Error: Invalid input. Please enter valid numbers.")
