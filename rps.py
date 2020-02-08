#!/usr/bin/env python3

import random


"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("Rock, paper, scissors? > ").lower()
            if move in moves:
                return move


class ReflectPlayer(Player):
    def __init__(self):
        self.next_move = random.choice(moves)

    def move(self):
        return self.next_move

    def learn(self, my_move, their_move):
        self.next_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        self.next_move = "rock"

    def move(self):
        return self.next_move

    def learn(self, my_move, their_move):
        my_move_index = moves.index(my_move)
        next_move_index = (my_move_index + 1) % 3
        self.next_move = moves[next_move_index]


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score1 = 0
        self.score2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")

        if beats(move1, move2):
            self.score1 += 1
            print("** PLAYER ONE WINS **")
        elif beats(move2, move1):
            self.score2 += 1
            print("** PLAYER TWO WINS **")
        else:
            print("** TIE **")

        print(f"Score: Player One {self.score1}, Player Two {self.score2}\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("\nGame start!\n")

        for round in range(3):
            print(f"Round {round} of 3:")
            self.play_round()

        while self.score1 == self.score2:
            print("Game cannot end in a tie, entering sudden death overtime")
            self.play_round()

        print(
            f"Final Score: Player One {self.score1}, Player Two "
            f"{self.score2}\n"
        )

        if self.score1 > self.score2:
            print("** PLAYER ONE IS THE CHAMPION **")
        elif self.score2 > self.score1:
            print("** PLAYER TWO IS THE CHAMPION **")

        print("Game over!\n")


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
