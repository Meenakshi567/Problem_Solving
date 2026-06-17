def convert_and_count():
    try:
        # Read the decimal integer from the user
        decimal_input = input("Enter a decimal number: ")
        num = int(decimal_input)
        
        # Numbers less than or equal to 0 will not have 1's in standard binary
        if num <= 0:
            print("invalid input")
            return
        
        # Convert decimal to binary string and remove the '0b' prefix
        binary_str = bin(num)[2:]
        
        # Count the total number of 1s
        count_of_ones = binary_str.count('1')
        
        # Final output check
        if count_of_ones == 0:
            print("invalid input")
        else:
            print(f"Binary equivalent: {binary_str}")
            print(f"Count of 1's: {count_of_ones}")
            
    except ValueError:
        # Handles any non-integer text inputs safely
        print("invalid input")

if __name__ == "__main__":
    convert_and_count()
