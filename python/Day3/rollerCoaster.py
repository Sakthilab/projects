print("Welcone to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("you can ride the rollercoaster!")
    age = int(input("Enter your age: "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok, Have a free ride") 
    else:
        bill = 12
        print("Adult tickets are $12.")   

    

    photo = input("Do you want to take photo? Y or N, ")
    if photo == 'Y':
        bill += 3

    print(f"your final ticket amount is {bill}")

else:
    print("sorry, you have to grow taller before you can ride.")
