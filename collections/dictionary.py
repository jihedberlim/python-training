# Data
# Star Wars - Episode IV - A New Hope, George Lucas, 1977, 7755000000.00
# Creating the dictionary

dictionary = {
    "name": "Star Wars - Episode IV - A New Hope",
    "director": "George Lucas",
    "release year": 1977,
    "box office": 7755000000.00
}

# Displaying the complete dictionary

print(dictionary)

# Displaying the value of a key
print(dictionary["name"])

# Insertion of a new key and value (gender)
dictionary["gender"] = "Space Opera"
print(dictionary)

# keys method
print(dictionary.keys())
for key in dictionary.keys():
    print(key)

# values method
print(dictionary.values())
for value in dictionary.values():
    print(value)

# items method
print(dictionary.items())
for key, value in dictionary.items():
    print(f"{key} | {value}")

# get method
print(dictionary.get("audience"))
print(dictionary.get("name"))

# setdefault method
dictionary.setdefault("audience", 1000)
print(dictionary)