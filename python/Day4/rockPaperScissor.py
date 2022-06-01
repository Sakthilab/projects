import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock, paper, scissors]

choice = int(input('what do you choose? Type 0 for \"rock\", 1 for \"paper\", 2 for \"scissors\". \n'))
if choice >= 3 or choice < 0:
    print("you have entered invalid number, you lose!")
else:
    print(game[choice])
    comp_choice = random.randint(0,2)
    print(f"computer choose:")
    print(game[comp_choice])

    if  choice == 0 and comp_choice == 2:
        print("you win")
    elif comp_choice == 0 and choice == 2:
        print("you lose")
    elif choice == comp_choice:
        print("match draw")
    elif comp_choice > choice:
        print("you lose")
    elif choice > comp_choice:
        print("You win")
    elif choice == 1 and comp_choice == 2:
        print("you lose")
    elif choice >= 3 or choice < 0:
        print("you have entered invalid number, you lose!")




