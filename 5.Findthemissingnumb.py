#listeyi hazırlama
import random

my_list = [i for i in range(0, 21)]
random.shuffle(my_list)

#1. yol
remove_list = random.sample(my_list, 6)

print(my_list)
print(remove_list)

for i in remove_list:
    my_list.remove(i)

#2.yol
#del my_list[0:6]

print(my_list)





#1.çözüm
my_list = [15, 13, 11, 16, 5, 3, 19, 2, 6, 12, 1, 8, 4, 10, 17]

missing_list = []
for i in range(0, 21):
    if i not in my_list:
        missing_list.append(i)

print(f"Listemiz içerisinde {len(missing_list)} tane sayı eksiktir. Eksik olan sayılar {missing_list}")






#2.çözüm
my_list = [15, 13, 11, 16, 5, 3, 19, 2, 6, 12, 1, 8, 4, 10, 17]

my_set = {i for i in range(0,21)}

difference_set = my_set - set(my_list)
print(f"Listemiz içerisinde {len(difference_set)} tane sayı eksiktir. Eksik olan sayılar {difference_set}")
