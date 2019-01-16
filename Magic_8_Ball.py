### A basic Magic 8 Ball program ###
### - Lognasmeow - ###

import random

answers = ["Yeah, probably", "HA nope!", "Unlikely", "Totally!", "I wouldn't count on it",
           "I wouldn't bet money on that", "Uhh, maybe", "That'll happen tomorrow",
           "Ha, as if", "Perhaps", "IDK", "I think it's possible", "Why don't you ask me later",
           "No", "Of course", "Like fo sho", "It's likely"]
question = ""       # question asked by the user
yesNo = ""          # for the program to loop at user's will

print("Welcome to Magic 8 Ball!")
while yesNo == "y" or yesNo == "Y" or yesNo == "":
    print("Ask the all-knowing mystical ball a question and it will answer you!: ")
    print("")
    input(question)
    print(answers[random.randint(0, len(answers) - 1)])
    print("")
    print("Would you like to ask another question? (y/n): ")
    yesNo = input()
    while yesNo != "y" and yesNo != "Y" and yesNo != "n" and yesNo != "N":      # in case something irrelivant is typed
        print("Please enter either 'y' or 'n': ")
        yesNo = input()
    if yesNo == "n" or yesNo == "N":
        break
    yesNo = ""          # resetting to nothing, otherwise 'y'/'Y' is stuck in place