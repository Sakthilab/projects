import random
name_string = input("Enter everybody\'s name, seprated by a coma. ")
name_list = name_string.split(', ')
print(name_list)
l = len(name_list)
p = random.randint(0, l-1)

bill = name_list[p]
print(f"{bill}, is going to pay the bill")