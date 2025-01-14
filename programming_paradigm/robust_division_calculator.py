# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """Performs division and handles errors like division by zero and non-numeric input."""
    try:
        # Convert inputs to floats
        num = float(numerator)
        denom = float(denominator)
        
        # Attempt division
        result = num / denom
        return f"The result of the division is {result:.2f}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Please enter numeric values only."
