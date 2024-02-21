def is_armstrong(number):
    num_str = str(number)
    order = len(num_str)
    sum_of_digits = sum(int(digit) ** order for digit in num_str)
    return number == sum_of_digits

# Example
number = int(input("Enter a number: "))
if is_armstrong(number):
    print(f"{number} is an Armstrong number")
else:
    print(f"{number} is not an Armstrong number")
