print("Welcome to integer calculator!")

firstValue = int(input("Please enter a number: "))
secondValue = int(input("Please enter another number: "))

# print(type(firstValue))
# print(type(secondValue))

sumValue = firstValue + secondValue
subtractionValue = firstValue - secondValue
multiplicationValue = firstValue * secondValue
divisionValue = firstValue / secondValue

print("The sum is:", sumValue)
print("The sum is: {}".format(sumValue))

print(f'The sum is: {sumValue}')
print(f'The sub is: {subtractionValue}')
print(f'The mult is: {multiplicationValue}')
print(f'The div is: {divisionValue}')
