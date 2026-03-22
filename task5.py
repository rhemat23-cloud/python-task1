

def main():
    try:
        # Calculations
        result1 = 25 + 10       # Addition
        result2 = 50 - 20       # Subtraction
        result3 = 8 * 5         # Multiplication
        result4 = 100 / 10      # Division (float result)
        result5 = 10 % 3        # Modulus (remainder)
        result6 = 2 ** 4        # Exponentiation (power)
        result7 = 20 // 3       # Floor division (integer result)

        # Printing results
        print("25 + 10 =", result1)
        print("50 - 20 =", result2)
        print("8 * 5 =", result3)
        print("100 / 10 =", result4)
        print("10 % 3 =", result5)
        print("2 ** 4 =", result6)
        print("20 // 3 =", result7)

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()

