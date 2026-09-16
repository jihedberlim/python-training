lists = [7, 11, 7.9, "Test"]

# inserting new elements into the list
lists.insert(5, "insertion test")
lists.append("insertion test at the end of the list")

# showing entire list
print(lists)

# showing element by index
print(lists[2]) #3rd element
print(lists[-1]) #last element
print(lists[0:3]) #among these elements

#
for value in lists:
    print(value)

#removing items from the list
lists.pop()
print(lists)
lists.remove(11)
print(lists)

#finding the size of a list
print(len(lists))