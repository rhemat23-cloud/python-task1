
# Given word
word = "Python"

# Validate that the word has enough characters
if len(word) < 3:
    print("The word is too short to extract the required letters.")
else:
    # Extract letters using indexing
    first_letter = word[0]      # First letter (index 0)
    third_letter = word[2]      # Third letter (index 2)
    last_letter = word[-1]      # Last letter (index -1)

    # Print results
    print("First letter:", first_letter)
    print("Third letter:", third_letter)
    print("Last letter:", last_letter)
