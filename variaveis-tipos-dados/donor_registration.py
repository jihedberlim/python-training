#NAME
#WEIGHT
#HEIGHT
#AGE
#MEETS MINIMUM WEIGHT FOR DONATION
#MEETS MINIMUM AGE FOR DONATION
from datetime import date

print("Blood donor registration")
nameDonor = input("Please enter your full name: ")
weightDonor = float(input("Please enter your weight: "))
heightDonor = float(input("Please enter your height: "))
birthDateDonor = input("Please enter your birth date: ")

currentAgeDonor = date.today().year - int(birthDateDonor)
minWeightDonor = weightDonor > 50
minAgeDonor = weightDonor >= 16

textOutput = f"\tNAME: {nameDonor}\n\tWEIGHT: {weightDonor} kg\n\tHEIGHT: {heightDonor} cm\n\tAGE: {currentAgeDonor} years old\n\tMEETS MINIMUM WEIGHT FOR DONATION: {minWeightDonor}\n\tMEETS MINIMUM AGE FOR DONATION: {minAgeDonor}"

print(textOutput)
