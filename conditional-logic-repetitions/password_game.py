secret_answer = ""
attempts = 0

while secret_answer != "python":
    secret_answer = input("Please enter your secret answer: ")
    attempts += 1

print("The correct answer was typed!")
print(f"It took {attempts} attempts to find the secret answer: {secret_answer}.")