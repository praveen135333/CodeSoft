import random

def game():
    winCount = 0
    lossCount = 0
    drawCount = 0
    option = ["rock","paper","scissor"]
    winRules = {
        "scissor":"paper",
        "rock":"scissor",
        "paper":"rock"
    }
    print("-----Rock, Paper & Scissor Game-----")
    while True:
        userChoice = input("Enter your choice: ")
        botChoice = random.choice(option)
        print(f"Computer choice: {botChoice}")
        if botChoice == userChoice:
            print("Draw")
            drawCount=drawCount+1
        else:
            if winRules[userChoice] == botChoice:
                print("Congrats! You won.")
            else:
                print("You lose!")
                winCount=winCount+1
        playAgain = input("Do you want to play again(y/n)?\t")
        if playAgain == "y":
            continue
        elif playAgain == "n":
            print(f"Total no. of matches: {winCount+lossCount+drawCount}\ntotal wins: {winCount}\ttotal loses: {lossCount}\tdraw: {drawCount}")
            break
        else: 
            print("Wrong choice!")
            break
game()