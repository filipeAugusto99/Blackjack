from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player = []
computer = []

should_continue = True

while should_continue:
    want_to_play = input("Do you want to play a game of Blackjack? \
Type 'y' or 'n': ")
    sum_choices = 0

    if want_to_play == "n":
        should_continue = False
    elif want_to_play == "y":
        print("\n" * 100)
        print(logo)

        for choice in range(2):
            choices_player = random.choice(cards)
            player.append(choices_player)

        for choice in player:
            sum_choices += choice

        choice_computer = random.choice(cards)
        computer.append(choice_computer)

        print(f"Your cards: {player}, current score: {sum_choices}")
        print(f"Computer's first hand: {computer}")

