# imports
from art import logo
import random


# ------------------- FUNCTIONS -------------------

# function to compare final scores and display results
def compare_scores(score_player, score_computer, player, computer):
    """Compare scores between player and computer and print the result"""
    
    if score_player > 21:
        print(f"\nYour final hand: {player}, final score {score_player}\n")
        print(f"Computer's final hand {computer}, final score {score_computer}\n")
        print("You went over. You lose :(")
    elif score_computer > 21:
        print(f"\nYour final hand: {player}, final score {score_player}\n")
        print(f"Computer's final hand {computer}, final score {score_computer}\n")
        print("Computer went over. You win :) !!")
    elif score_player == score_computer:
        print(f"\nYour final hand: {player}, final score {score_player}\n")
        print(f"Computer's final hand {computer}, final score {score_computer}\n")
        print("Draw!")
    elif score_player == 21:
        print(f"\nYour final hand: {player}, final score {score_player}\n")
        print(f"Computer's final hand {computer}, final score {score_computer}\n")
        print("Blackjack! You win :) !!")
    elif score_player > score_computer:
        print(f"\nYour final hand: {player}, final score {score_player}\n")
        print(f"Computer's final hand {computer}, final score {score_computer}\n")
        print("You win :) !!")
    else:
        print(f"\nYour final hand: {player}, final score {score_player}\n")
        print(f"Computer's final hand {computer}, final score {score_computer}\n")
        print("You lose :(")


# function that handles the player's turn (draw or pass)
def player_turn(player, computer, cards):
    """Handle player's decision to draw more cards or pass"""
    
    # while True until player decide to stop drawing cards
    while True:
        score_player = sum(player)

        # if player already has blackjack, stop
        if score_player == 21:
            print("You got a BlackJack!!!")
            break

        # ask player to draw or pass
        another_card_or_pass = input("Type 'y' to get another card, type 'n' to pass: ")

        # if player choose to pass, break loop
        if another_card_or_pass == "n":
            break
        # if player choose to draw another card
        elif another_card_or_pass == "y":
            player.append(random.choice(cards))
            score_player = sum(player)

            # check if player went over 21
            if score_player > 21:
                print(f"\nYour final hand: {player}, final score {score_player}")
                print(f"Computer's first card: {computer[0]}")
                print("You went over. You lose :(")
                break
            # otherwise show updated hand
            else:
                print(f"Your cards: {player}, current score: {score_player}")
                print(f"Computer's first card: {computer[0]}")
        else:
            print("Invalid input. Please type 'y' or 'n'.")

    return player, sum(player)


# main game function
def play():
    """Main function to control the Blackjack game"""

    # list of available cards (11 = Ace)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    # empty lists for player and computer
    player = []
    computer = []

    # ensures that repetition will be stopped
    should_continue = True

    # while player want to play
    while should_continue:
        want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

        if want_to_play == "n":
            should_continue = False
        elif want_to_play == "y":
            print("\n" * 100)
            print(logo)

            # deal initial 2 cards to player
            for _ in range(2):
                player.append(random.choice(cards))

            # deal initial 1 card to computer
            computer.append(random.choice(cards))

            score_player = sum(player)
            score_computer = sum(computer)

            print(f"Your cards: {player}, current score: {score_player}")
            print(f"Computer's first hand: {computer}")

            # dealer draws until 17 or more
            while score_computer < 17:
                computer.append(random.choice(cards))
                score_computer = sum(computer)

            # call function that handles player's turn
            player, score_player = player_turn(player, computer, cards)

            # finally compare both scores
            compare_scores(score_player, score_computer, player, computer)

            # reset hands for next game
            player.clear()
            computer.clear()
        else:
            print("Invalid input. Please type 'y' or 'n'.")


# ------------------- RUN GAME -------------------
play()
