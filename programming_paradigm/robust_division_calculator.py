def safe_divide(numerator, denominator):
    """
    Safely divide two numbers with error handling.
    Returns a string message with the result or error description.
    """
    try:
        # Convert inputs to float
        num = float(numerator)
        den = float(denominator)

        # Try division
        result = num / den
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."