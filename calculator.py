def calculator(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b != 0:
            return a / b
        else:
            raise ValueError("Cannot divide by zero.")
    else:
        raise ValueError("Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'.")
    
#milll
print(calculator(10, 5, 'add'))        # Output: 15
print(calculator(10, 5, 'subtract'))   # Output: 5
print(calculator(10, 5, 'multiply'))   # Output: 50
print(calculator(10, 5, 'divide'))     # Output: 2.0
