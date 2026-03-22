# String comparison example
a = "apple"
b = "Apple"

# Compare the two strings
print(a == b)  # This will print: False

# Explanation
if a == b:
    print("Strings are equal.")
else:
    print("Strings are NOT equal because Python compares them case-sensitively.")
    print(f"ord('a') = {ord('a')}, ord('A') = {ord('A')}")
