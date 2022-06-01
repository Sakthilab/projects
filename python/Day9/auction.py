import os
from art import logo

print(logo)

def result(data):
    winner  = ""
    highest_bid = 0
    for bid in data:
        price = data[bid]
        if price > highest_bid:
            highest_bid = price
            winner = bid
    print(f"The winner is {winner} with a bid od ${highest_bid}")

auction = {}
finished = False

while not finished:
    name = input("what is your name: ")
    bid = int(input("What is your bid: $"))
    auction[name] = bid
    should_continue = input("Are there are any other bidders? Type 'yes' or 'no'. ").lower()
    if should_continue == "no":
        finished = True
        result(auction)
    elif should_continue == "yes":
        os.system('cls')













