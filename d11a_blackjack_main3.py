from d11b_blackjack_art import logo
from random import choice


def winner(player):
    """
    tells who the winner is; ends the game
    (since this is an ide where i am not able to restart the game by clearing the console,
    the user has to manually start another game manually
    :param player: user / dealer
    """
    print(f"{player.title()} wins!")
    print("Click the run button to play Blackjack once again")
    exit(0)


def deal_card():
    """
    this functions uses the list of cards below to return a random card
    :return: a random card from the deck
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return choice(cards)


def calculate_score(deck_of_cards):
    """
    tells the score of the player based on their cards
    checks for the case where score is above 21 and whether user has ace or not
    :param deck_of_cards: player's cards
    :return: player's score
    """
    score = sum(deck_of_cards)

    # checking for blackjack
    if score == 21 and len(deck_of_cards) == 2:
        score = 0

    # if score > 21: replacing points of all ace cards of 11 with 1
    if 11 in deck_of_cards:
        if score > 21:
            deck_of_cards.remove(11).append(1)
            if sum(deck_of_cards) > 21:
                print("User scored more than 21 but has ace card(s) while ace counts as 1 instead of 11")
                winner('Dealer')

    elif 11 not in deck_of_cards and sum(deck_of_cards) > 21:
        print("User scored more than 21 but has no ace card(s) in the deck")
        winner('Dealer')

    return score


def compare(user_cards, computer_cards):
    if sum(user_cards) > sum(computer_cards):
        print("User has more points than dealer")
        winner('User')
        exit(0)

    elif sum(user_cards) < sum(computer_cards):
        print("Dealer has more points than User")
        winner('Dealer')
        exit(0)

    else:
        print("User and dealer have scored the same amount of points\nIts a tie!!")
        exit(0)


def computer_turn(computer_cards):
    while calculate_score(computer_cards) < 17:
        computer_cards.append(deal_card())
    return computer_cards


def user_turn(user_cards, computer_cards):
    # if either has blackjack - score = 0, game ends
    if calculate_score(user_cards) == 0:
        print("User has a blackjack!")
        winner('User')

    elif calculate_score(computer_cards) == 0:
        print("Dealer has a Blackjack")
        winner('Dealer')

    # if user scores > 21, user wins
    elif calculate_score(user_cards) > 21:
        print("User scored more than 21")
        winner('Dealer')

        # game continues if user draws another card. else, it ends
        another_card = input("Do you want to draw another card?\nPress 'y' or 'n': ").lower()
        if another_card == 'y':
            user_cards.append(deal_card())
            user_turn(user_cards, computer_cards)

        elif another_card == 'n':
            # get back here
            computer_turn(computer_cards)

    elif calculate_score(user_cards) < 21:
        print()

    return user_cards


def game_contents():
    user_cards = []
    computer_cards = []

    user_cards.append(deal_card())
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

    print(f"Player has {user_cards} and user scores {calculate_score(user_cards)}")
    print(f"Dealer has {computer_cards} and computer scores {calculate_score(computer_cards)}")
    computer_cards.append(deal_card())

    user_cards = user_turn(user_cards, computer_cards)
    computer_cards = computer_turn(computer_cards)

    if sum(computer_cards) > 21:
        print("Dealer has scored over 21")
        winner('Dealer')

    else:
        compare(user_cards, computer_cards)


# game begins here
game_contents()
