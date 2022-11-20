import random

my_list = [i for i in range(0, 100)]

random.shuffle(my_list)
print(my_list)

remove_list = random.sample(my_list, 1)
print(remove_list)

