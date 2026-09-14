numberFactorial = int(input("Please enter a number: "))
factorial = numberFactorial

for value in range(1, numberFactorial, 1):
    factorial = factorial * value

print(f"The factorial of {numberFactorial} is {factorial}")