# ======================================================
# LEARNING PYTHON : Functions & Recursions
# ======================================================


# 1. BASIC FUNCTION
# A function taes inouts (parameters) and returns an output.

def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}! Welcome to Python."
print (greet("Anuradha"))
print (greet("dushan"))

# 2. DEFAULT & KEYWORD ARGUMENTS
# Parameters can have default values.
 
def power(base, exponent=2):
    """Raise base to the given exponent (default: square)."""
    return base ** exponent
 
print(power(3))       # 3^2 = 9
print(power(3, 4))    # 3^4 = 81

 # 3. RETURNING MULTIPLE VALUES
# Functions can return more than one value as a tuple.
 
def min_max(numbers):
    """Return the minimum and maximum of a list."""
    return min(numbers), max(numbers)
 
low, high = min_max([4, 1, 9, 2, 7])
print(f"Min: {low}, Max: {high}")