# creating an empty set
group1 = set()
print(type(group1))

# creating a set from a list
list = ["Jihed", "Berlim", "Isabella", "Costa", "Jihed"]
print(list)

group2 = set(list)
print(group2)

# creating a set with values
group3 = {"Fulano", "Ciclano", "Beltrano", "Coisa"}
print(group3)

# adding an element (add)
group3.add("Negócio")
print(group3)

# removing elements present in another set (difference_update)
group1 = {"Mega Drive", "Super Nintendo", "Playstation"}
group2 = {"Playstation", "Nintendo 64", "Sega Saturn", "Dreamcast"}

print(f"The first set contains {group1}")
print(f"The second set contains {group2}")

group1.difference_update(group2)
print(f"The first set contains {group1}")

# removing a specific element from the set (remove)
group1 = {"Mega Drive", "Super Nintendo", "Playstation"}
print(group1)

group1.remove("Mega Drive")
print(group1)

# removing a specific element from the set (discard)
group1.discard("Super Nintendo")
print(group1)

group1.discard("Super Nintendo")
print(group1)