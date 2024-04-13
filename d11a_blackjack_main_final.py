from d11b_blackjack_art import logo
from random import choice

cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def winner(player):
    print(f"{player.title()} wins!")
    print("Thank you for playing Blackjack!")
    exit(0)


def calculate_score(deck):
    """
    function to calculate the score of the given deck
    :param deck: deck of cards
    :return: score of the deck
    """
    score = sum(deck)
    # check for blackjack
    if score == 21 and len(deck) == 2:
        score = 0

    # check for ace
    if 11 in deck and score > 21:
        deck.remove(11)
        deck.append(1)
        score = sum(deck)

    return score


def deal(deck):
    """
    function to add a random card to the given deck
    :param deck: deck to which a card is added
    :return: updated deck
    """
    return deck.append(choice(cards))


def compare_scores(user_score, dealer_score, user_deck):
    """
    Calculates the score and declares the winner as per the socres
    :param user_score: user's score
    :param dealer_score: dealer's score
    :param user_deck: user's deck
    :return: winner
    """
    if user_score == 0:
        if dealer_score == 0:
            print("It is a tie")

        print("User has Blackjack")
        winner('Player')

    elif dealer_score == 0:
        print("Dealer has Blackjack")
        winner('Dealer')

    elif user_score < 21:
        if dealer_score > 21:
            print("Dealer has scored more than 21 and User has scored less than 21")
            winner('User')

        elif dealer_score < 21:
            if user_score > dealer_score:
                print("User has scores more than Dealer")
                winner('User')

            elif user_score < dealer_score:
                print("Dealer has scored more than User")
                winner('Dealer')

            else:
                print("It is a tie!!")

    elif user_score > 21:
        if 11 not in user_deck:
            print("User scored above 21 with no ace card")
            winner('Dealer')

        elif 11 in user_deck and calculate_score(dealer_deck) > 21:
            print("User scored over 21 with ace counted as 1")
            winner('Dealer')

        elif 11 in user_deck and calculate_score(dealer_deck) <= 21:
            user_turn(user_deck, dealer_deck)


def play_blackjack():
    """
    main gameplay of blackjack consisting of user's and computer's turn
    rem user plays first, dealer plays next, scores are compared after both have picked their cards
    :return: nothing
    """
    print(logo)

    user_deck, dealer_deck = [], []
    for _ in range(2):
        deal(user_deck)
        deal(dealer_deck)

    return user_deck, dealer_deck


def dealer_turn(user_deck, dealer_deck):
    user_score = calculate_score(user_deck)
    dealer_score = calculate_score(dealer_deck)
    while 0 < dealer_score < 17:
        deal(dealer_deck)
        dealer_score = calculate_score(dealer_deck)

    # printing final scores and cards before comparing the score
    for _ in range(1):
        print(f"User has {user_deck}, user's final score is {user_score}")
        print(f"Dealer has {dealer_deck}, dealer's final score is {dealer_score}")

    compare_scores(user_score, dealer_score, user_deck)


def user_turn(user_deck, dealer_deck):
    user_score = calculate_score(user_deck)
    dealer_score = calculate_score(dealer_deck)

    print(f"User has {user_deck}, user's current score is {calculate_score(user_deck)}")
    print(f"Dealer's first card is {dealer_deck[0]}")

    # exit cases:
    # check for blackjack
    if user_score == 0 or dealer_score == 0:
        compare_scores(user_score, dealer_score, user_deck)

    # score > 21 and ace card
    elif user_score > 21:
        compare_scores(user_score, dealer_score, user_deck)

    elif user_score <= 21:
        new_card = input("Do you want to draw another card?\nPress 'y' or 'n': ")
        if new_card == 'n':
            dealer_turn(user_deck, dealer_deck)

        elif new_card == 'y':
            deal(user_deck)
            user_turn(user_deck, dealer_deck)

    return user_score, dealer_score, user_deck


if __name__ == '__main__':
    _ = input("Press enter to start the game")
    user_deck, dealer_deck = play_blackjack()
    user_score, dealer_score, user_deck = user_turn(user_deck, dealer_deck)
    dealer_turn(user_deck, dealer_deck)
