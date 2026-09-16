enemyTeam = [(50, 30), (100, 100), (10, 90), (30, 25)]

# for enemy in enemyTeam:
#     print(enemy)
#     for coordinated in enemy:
#         print(coordinated)
while True:
    x = int(input("Enter the x-coordinate you wish to attack: "))
    y = int(input("Enter the y-coordinate you wish to attack: "))

    if (x, y) in enemyTeam:
        enemyTeam.remove((x, y))
        print("You hit an enemy!")
        break
    else:
        print("You missed!")
print(enemyTeam)
