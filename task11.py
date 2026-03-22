# List of numbers
numbers = [10, 20, 30, 40, 50]

# Check membership using 'in' and 'not in'
try:
    print("20 in numbers:", 20 in numbers)       # True if 20 is in the list
    print("60 in numbers:", 60 in numbers)       # True if 60 is in the list
    print("30 not in numbers:", 30 not in numbers)  # True if 30 is NOT in the list
except Exception as e:
    print("An error occurred:", e)
