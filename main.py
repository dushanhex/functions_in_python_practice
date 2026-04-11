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

# ── 4. RECURSION BASICS 
# A recursive function calls ITSELF with a smaller problem.
# Every recursive function needs:
#   (a) A BASE CASE  — when to stop
#   (b) A RECURSIVE CASE — calling itself with a simpler input
 
def countdown(n):
    """Count down from n to 1, then say Liftoff!"""
    if n <= 0:                  # base case
        print("🚀 Liftoff!")
    else:
        print(n)
        countdown(n - 1)        # recursive case
 
countdown(5)
 # ── 5. FACTORIAL 
# factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
 
def factorial(n):
    """Return n! using recursion."""
    if n == 0 or n == 1:        # base case
        return 1
    return n * factorial(n - 1) # recursive case
 
print(f"5! = {factorial(5)}")   # 120
print(f"0! = {factorial(0)}")   # 1

# ── 6. FIBONACCI SEQUENCE
# Each number is the sum of the two before it: 0 1 1 2 3 5 8 …
 
def fibonacci(n):
    """Return the nth Fibonacci number."""
    if n <= 0:
        return 0                           # base case
    if n == 1:
        return 1                           # base case
    return fibonacci(n - 1) + fibonacci(n - 2)  # recursive case
 
print("Fibonacci sequence (first 8 terms):")
print([fibonacci(i) for i in range(8)])   # [0,1,1,2,3,5,8,13]

# ── 7. BINARY SEARCH (recursion on a sorted list) 
# Efficiently find an item by repeatedly halving the search range.
 
def binary_search(arr, target, low=0, high=None):
    """Return the index of target in sorted arr, or -1 if not found."""
    if high is None:
        high = len(arr) - 1
 
    if low > high:              # base case: not found
        return -1
 
    mid = (low + high) // 2
 
    if arr[mid] == target:      # base case: found it!
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)  # search right
    else:
        return binary_search(arr, target, low, mid - 1)   # search left
 
sorted_list = [2, 5, 8, 12, 16, 23, 38, 45]
print(f"Search for 23 → index {binary_search(sorted_list, 23)}")  # 5
print(f"Search for 10 → index {binary_search(sorted_list, 10)}")  # -1