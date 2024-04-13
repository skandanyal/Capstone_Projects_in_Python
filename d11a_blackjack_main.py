from d11b_blackjack_art import logo
from random import choice
import os


def check_blackjack(user, deck):
    if (deck[0] == 11 and deck[1] == 10) or (deck[0] == 10 and deck[1] == 11):
        print(f"{user} has a blackjack! {user} wins!\n")
        exit(0)
    else:
        None


def score_of(cards_list):
    sum_of_cards = 0
    for card in cards_list:
        sum_of_cards +=  cards_list[card]
    return sum_of_cards


def recursive_part(player_card, dealer_card):
    player_score, dealer_score = check_for_blackjack_and_score(player_card, dealer_card)

    # check's if the player's score is above 21 and if there is an ace in the deck or not and decided whether the game proceeds or not
    decision(player_score, player_card)

    new_card = input(f"Do you want to draw another card?\nPress 'y' for yes and 'n' for no: \n")
    if new_card == 'y':
        player_card.append(choice(cards))
    else:
        return player_score, dealer_score

    return recursive_part(player_card, dealer_card)


def decision(player_score, player_card):
    # is the player's score > 21?
    if player_score > 21:

        # is there an ace in the deck?
        for card in player_card:
            if card == 11:

                # if the ace counts as a 1 instead of 11, is the player's score still > 21?
                player_score -= 10
                if player_score > 21:
                    print(f"Player's score is above 21\nDealer wins!\n")
                    exit(0)
                else:
                    break

            # no ace in the deck
            else:
                print(f"Player's score is above 21\nDealer wins!\n")
                exit(0)


def deal_1(player_card, dealer_card):
    """
    this function executes the following steps:
    1. player has received two face up opening cards with his score
    2. dealer has received one face up card with his score
    3. dealer receives more cards until his score exceeds 17, but his updated score isn't shown to the player
    """

    # pick out two cards to the player, one for the dealer
    player_card.append(choice(cards))
    player_card.append(choice(cards))
    dealer_card.append(choice(cards))

    # display the cards and the score
    print(f"Your cards are {player_card}\nYour current score is {score_of(player_card)}\n")
    print(f"Dealer's first card is {dealer_card}\nDealer's current score is {score_of(dealer_card)}\n")

    # give the second card to the dealer
    dealer_card.append(choice(cards))

    player_score, dealer_score = check_for_blackjack_and_score(player_card, dealer_card)

    return player_score, dealer_score


def check_for_blackjack_and_score(player_card, dealer_card):
    # check if either the player or the dealer has a blackjack
    check_blackjack("Player", player_card)
    check_blackjack("Dealer", dealer_card)

    # update the dealer's score to above 17
    while score_of(dealer_card) < 17:
        dealer_card.append(choice(cards))
        score_of(dealer_card)

    # returns the scores of both player and the dealer
    return score_of(player_card), score_of(dealer_card)


def game_begins():
    """
    this function asks the user whether he wants to begin the game of blackjack or not
    if yes:
        the previous screen is erased and the game begins from the absolute beginning
    elif no:
        the game stop at wherever it is
    else:
        game_begins()
    """

    decision = input(f"Do you want to play a game of Blackjack?\nPress\n'y' for yes or\n'n' for no: \n")

    if decision == 'y':
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        deal_1(player_card, dealer_card)
    elif decision == 'n':
        exit(0)
    else:
        game_begins()


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_card = []
dealer_card = []

print(logo)

# game begins by asking whether the player wants to play the game or not
game_begins()

player_score, dealer_score = recursive_part(player_card, dealer_card)

if dealer_score > 21:
    print(f"Dealer's score is above 21\nPlayer wins!\n")
else:
    if player_score < dealer_score:
        print("Dealer scored more than player\nDealer wins!\n")
    elif player_score == dealer_score:
        print(f"Dealer and the player have the same score\nIts a tie!\n")
    else:
        print(f"Player scored more than dealer\nPlayer wins!\n")