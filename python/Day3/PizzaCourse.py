print("welcome to the python pizzz deliveries!")
size = input("What size pizza do you want? S, M, L ")
pep = input("Do you want to add peperonni? Y or N ")
che = input("Do you want to add cheese? Y or N ")
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

if pep == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if che == "Y":
    bill += 1

print(f"your total bill amount is {bill}")