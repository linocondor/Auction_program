from replit import clear
import figures

print(figures.logo)
print("Welcome to the auction")

people = {}
other_biders = True
while other_biders == True:
    name = input("What is your name? ")
    bid = input("What is your bid? ")
    continue_b = input("Are there other biders? (yes/no) ")

    people[name] = bid

    if continue_b == "yes":
        other_biders = True
        clear()
    elif continue_b == "no":
        other_biders = False

max_bid = []
person_won = []
for person in people:

    for i in range(0, len(people)):
        for personss in people:
            if people[person] > people[personss]:
                max_bid = people[person]
                person_won = person

print(f"{person_won} win , with a bid of {max_bid}")
