import random
import time

rock = 1
paper = 2
scissors = 3

names = {rock: "Rock", paper: "Paper", scissors: "Scissors"}
rules = {rock: scissors, paper: rock, scissors: paper}

player_score = 0
computer_score = 0

def start():
    print("Let's play a game of Rock, Paper, Scissors")
    while game():
        pass
    scores()

def game():
    player = move()
    computer = random.randint(1, 3)
    result(player, computer)
    return play_again()

def move():
    while True:
        player = raw_input("\nRock = 1\nPaper = 2\nScissors = 3\nMake a move: ")

def result():
    pass

def play_again():
    pass

def scores():
    pass

if __name__ == '__main__':
    start()