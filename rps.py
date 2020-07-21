"""A program that plays the game of Rock, Paper, Scissors.

Usage: rps.py

Attributes:
    MOVES: A list of strs representing possible moves (default: "rock",
        "paper", and "scissors")

Classes:
    Player()
    RandomPlayer()
    HumanPlayer()
    ReflectPlayer()
    CyclePlayer()
    Game()
"""

import random

MOVES = ["rock", "paper", "scissors"]


class Player:
    """Creates a player that always plays 'rock'."""

    def move(self):
        """Returns the move 'rock'

        Returns:
            'rock': A str representing the move rock
        """
        return "rock"

    def learn(self, my_move, their_move):
        """Placeholder for child classes.

        Args:
            my_move: A str representing the calling player's move
            their_move: A str representing the calling player's opponent's move
        """


class RandomPlayer(Player):
    """Creates a player that plays a random move from the MOVES array."""

    def move(self):
        """Returns a random move from the MOVES array.

        Returns:
            A str representing a move from the MOVES array
        """
        return random.choice(MOVES)


class HumanPlayer(Player):
    """Creates a player that is human controllable."""

    def move(self):
        """Returns a move of the human player's choosing.

        Returns:
            move: A str representing a move from the MOVES array chosen by the
                human player
        """
        while True:
            move = input("Rock, paper, scissors? > ").lower()
            if move in MOVES:
                return move


class ReflectPlayer(Player):
    """Creates a player that plays based on the opponent's previous move.

    Attributes:
        next_move: A str representing the player's next move
    """

    def __init__(self):
        """Reflect Player set-up."""
        self.next_move = random.choice(MOVES)

    def move(self):
        """Returns the player's next move.

        Returns:
            self.next_move: A str presenting the players next move
        """
        return self.next_move

    def learn(self, my_move, their_move):
        """Sets the player's next move to their opponent's previous move.

        Args:
            See base class
        """
        self.next_move = their_move


class CyclePlayer(Player):
    """Creates a player that plays 'rock', 'paper', 'scissors', in that order.

    Attributes:
        next_move: A str representing the player's next move
    """

    def __init__(self):
        """Cycle Player set-up."""
        self.next_move = "rock"

    def move(self):
        """Returns the player's next move.

        Returns:
            self.next_move: A str presenting the players next move
        """
        return self.next_move

    def learn(self, my_move, their_move):
        """Sets the player's next move to the next move in the MOVES array.

        Args:
            See base class
        """
        my_move_index = MOVES.index(my_move)
        next_move_index = (my_move_index + 1) % 3
        self.next_move = MOVES[next_move_index]


def beats(one, two):
    """Returns a bool representing if the first arg is the winner.

    Args:
        one: A str representing a player's move
        two: A str representing a player's move

    Returns:
        A bool that is True if one is the winner
    """
    return (
        (one == "rock" and two == "scissors")
        or (one == "scissors" and two == "paper")
        or (one == "paper" and two == "rock")
    )


class Game:
    """Creates a game or rock, paper, scissors played between two players.

    Attributes:
        player1: A Player class representing player 1
        player2: A Player class representing player 2
        score1: An int representing player 1's score
        score2: An int representing player 2's score
    """

    def __init__(self, player1, player2):
        """Game set-up."""
        self.player1 = player1
        self.player2 = player2
        self.score1 = 0
        self.score2 = 0

    def play_round(self):
        """Plays a round of rock, paper Scissors.

        Collects the moves of both players, determines a winner, and then
        displays and updates the score
        """
        move1 = self.player1.move()
        move2 = self.player2.move()
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
        self.player1.learn(move1, move2)
        self.player2.learn(move2, move1)

    def play_game(self):
        """Plays a 3-round game of rock, paper, scissors.

        Plays three rounds of rock, paper scissors, and in the event of a tie
        score, continues to play extra rounds until there is a winner, and then
        displays the final score
        """
        print("\nGame start!\n")

        for rnd in range(3):
            print(f"Round {rnd} of 3:")
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


if __name__ == "__main__":
    COMPUTER_PLAYER = random.choice(
        [Player(), RandomPlayer(), CyclePlayer(), ReflectPlayer()]
    )
    GAME = Game(HumanPlayer(), COMPUTER_PLAYER)
    GAME.play_game()
