#Imports Random module
import random

#Creates Global Variables and needed lists
continuePlaying = "yes"
gameOptions = ["rock", "paper", "scissors"]

#Main Game Loop
while continuePlaying == "yes":

    #Troubleshooting Loop that prevents bad answers
    while True:
        # Allows user to pick their chosen option
        playerGameChoice = str(input("Rock, Paper, or Scissors?"))
        playerGameChoice = playerGameChoice.lower()
        print("You chose " + playerGameChoice + ".")

        #If statement that makes sure the answer is valid
        if (playerGameChoice != "paper" and playerGameChoice != "rock" and playerGameChoice != "scissors"):
            print("Your previous answer is invalid. Please choose Rock, Paper, or Scissors.")
        #Ends the loop after the answer is valid
        else:
            break


    #Generates a random number to choose an option and references the list at the top
    computerRandomInt = random.randint(0, 2)
    computerChoice = gameOptions[computerRandomInt]
    print("The computer chose " + computerChoice + ".")

    #Executes if both choices are the same
    if playerGameChoice == computerChoice:
        print("You tied.")

    # Executes if player chooses rock
    if playerGameChoice == "rock":
        if computerChoice == "paper":
            print("You lost.")
        elif computerChoice == "scissors":
            print("Congratulations, you won.")

    # Executes if player chooses paper
    elif playerGameChoice == "paper":
        if computerChoice == "scissors":
            print("You lost.")
        elif computerChoice == "rock":
            print("Congratulations, you won.")

    #Executes if player chooses scissors
    elif playerGameChoice == "scissors":
        if computerChoice == "rock":
            print("You lost.")
        elif computerChoice == "paper":
            print("Congratulations, you won.")

    #Loop that asks the user if they want to continue
    while True:
        # Allows user to pick their chosen option
        continuePlaying = str(input("Would you like to play again?"))
        continuePlaying = continuePlaying.lower()
        #If statement that makes sure answer is valid
        if (continuePlaying != "yes" and continuePlaying != "no"):
            print("Your previous answer is invalid. Please choose Yes or No.")
        else:
            break
