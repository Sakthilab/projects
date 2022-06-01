print("welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("how much tip would you like to give? 10, 12, or 15? "))
p = int(input("How many people to split the bill? "))
t= (tip / 100) * bill + bill
share = t / p
print(f"Each person should pay ${round(share, 2)}")