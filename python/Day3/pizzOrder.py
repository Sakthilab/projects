print('''  
 ____ 
/    \			
  u  u|      _______    
    \ |  .-''#%&#&%#``-.   
   = /  ((%&#&#&%&VK&%&))  
    |    `-._#%&##&%_.-'   
 /\/\`--.   `-."".-'
 |  |    \   /`./          
 |\/|  \  `-'  /
 || |   \     /  ''')

print("welcome to the python pizzz deliveries!")
size = input("What size pizza do you want? S, M, L ")
bill = 0

if size == "S":
    bill += 15
    pep = input("Do you want pepperoni? Y or N ")
    if pep == 'Y':
        bill += 2
        che = input("Do you want to add cheese? Y or N ")
        if che == 'Y':
            bill += 1
            print(f"Your total bill amount is ${bill}")
        else:
            print(f"Your total bill amount is ${bill}")    
        
    else:
        print(f"Your bill amount is ${bill}")    
    
elif size == "M":
    bill += 20
    pep = input("Do you want pepperoni? Y or N ")
    if pep == 'Y':
        bill += 3
        che = input("Do you want to add cheese? Y or N ")
        if che == 'Y':
            bill += 1
            print(f"Your total bill amount is ${bill}")
        else:
            print(f"Your total bill amount is ${bill}")    
        
    else:
        print(f"Your bill amount is ${bill}") 
else:
    bill += 25
    pep = input("Do you want pepperoni? Y or N ")
    if pep == 'Y':
        bill += 3
        che = input("Do you want to add cheese? Y or N ")
        if che == 'Y':
            bill += 1
            print(f"Your total bill amount is ${bill}")
        else:
            print(f"Your total bill amount is ${bill}")    
        
    else:
        print(f"Your bill amount is ${bill}") 


