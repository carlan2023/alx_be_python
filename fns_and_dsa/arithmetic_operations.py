def perform_operation (num1, num2, operation):
    
    if operation.lower() == 'add':
        result = num1 + num2
        return result
    elif operation == 'subtract':
        result = num1 - num2
        return result
    elif operation == 'multiply':
        result = num1 * num2
        return result
    elif operation == 'divide':
        if num2 != 0:
            result = num1 / num2
            return result
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"