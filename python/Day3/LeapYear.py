from asyncio.windows_events import NULL


print("----Leap Year Calculator------")
year = int(input("please enter the year you want to calculate: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not Leap year")
    else:
        print("Leap Year")
else:
    print("Not Leap Year")
