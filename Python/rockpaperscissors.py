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
        try:
            player = int(player)
            if player in (1, 2, 3):
                return player
        except ValueError:
            pass
        print("Oops ! I didn't understand that. Please enter 1, 2 or 3.")

def result(player, computer):
    print("1...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("3 !")
    time.sleep(0.5)
    print("Computer threw {0}!".format(names[computer]))
    global player_score, computer_score

    if player == computer:
        print("Tie game.")
    else:
        if rules[player] == computer:
            print("Your victory has been assured.")
            player_score += 1
        else:
            print("The computer laughs as you realise you have been powned lol.")
            computer_score += 1

def play_again():
    pass

def scores():
    pass

if __name__ == '__main__':
    start()