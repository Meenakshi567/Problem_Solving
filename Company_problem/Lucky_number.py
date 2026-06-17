def main():
    # Read the car number as a string
    car_str = input("Enter the car no:")
    
    try:
        car_no = int(car_str)
        
        # Check if the number is a positive 4-digit integer
        if 1000 <= car_no <= 9999:
            # Compute the sum of the digits
            digit_sum = sum(int(digit) for digit in car_str)
            
            # Check divisibility rules
            if digit_sum % 3 == 0 or digit_sum % 5 == 0 or digit_sum % 7 == 0:
                print("Lucky Number")
            else:
                print("Sorry its not my lucky number")
        else:
            print(f"{car_str} is not a valid car number")
            
    except ValueError:
        # Handles any non-numeric inputs
        print(f"{car_str} is not a valid car number")

if __name__ == "__main__":
    main()
