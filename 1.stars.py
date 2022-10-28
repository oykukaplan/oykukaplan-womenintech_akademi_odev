number = 5
for i in range(1, number + 1):
  print(" "(number-i) +" "*i )



number = 5
for x in range(0, number + 1):
    for j in range(1, (number + 1 - x)):
        print("* ", end=" ")
    print()