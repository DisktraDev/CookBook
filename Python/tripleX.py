import random
import time

MAX_LEVEL = 5

def Game():
    levelDifficulty = 1

    while levelDifficulty <= MAX_LEVEL:
        isLevelComplete = Play(levelDifficulty)
    
    if isLevelComplete:
        levelDifficulty += 1
    
    print("Congratulations !! You beat the game !")

def PrintIntroduction(levelDifficulty):
    print("You are a secret agent breaking into a level ", levelDifficulty, " secure server room")
    print("Enter the correct code to continue")

def Play(levelDifficulty):
    PrintIntroduction(levelDifficulty)

    # Declare 3 number code
    CodeA = 0
    CodeB = 0
    CodeC = 0

    CodeSum = CodeA + CodeB + CodeC
    CodeProduct = CodeA * CodeB * CodeC

    print("+ There are 3 numbers in the code")
    print("+ The codes add-up to: ", CodeSum)
    print("+ The codes multiply to give: ", CodeProduct)
    
    return levelDifficulty

