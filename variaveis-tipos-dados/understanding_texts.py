firstText = "This text has no line breaks. It also has no indentation."
print(firstText)

secondText = "This text has a line break \nhere. However, here we have a \ttab."
print(secondText)

thirdText = "this text is FORMATTED"

print(thirdText.capitalize())
print(thirdText.upper())
print(thirdText.lower())
print(thirdText.startswith("thi")) #There is a difference between uppercase and lowercase.
print(thirdText.endswith("D")) #There is a difference between uppercase and lowercase.
print(thirdText.count("t")) #There is a difference between uppercase and lowercase.
print("is" in thirdText)
print(thirdText.replace("this", "those"))
print(thirdText) #The variable is not changed