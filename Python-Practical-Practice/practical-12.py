numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))

if numerator % denominator == 0:
    print(f"{numerator} is divisible by {denominator}")
else:
    print(f"{numerator} is not divisible by {denominator}")
