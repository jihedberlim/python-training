calories = []
answerUser = ""

while answerUser.upper() != "NO":
    calorie = int(input("How many calories did you consume in this meal? "))
    calories.append(calorie)
    answerUser = input("Would you like to enter the calories for another meal? ")

totalCalories = 0
for calorie in calories:
    print(f"{calorie} calories were consumed in this meal.")
    totalCalories += calorie

averageCalories = totalCalories / len(calories)
print(f"On this day, there was an average consumption of {averageCalories:.2f} calories per meal.")