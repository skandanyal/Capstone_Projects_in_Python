from d11b_blackjack_art import logo
from random import choice


def score_of(deck):
    """
    Takes in the deck and returns the score
    :param deck: deck of cards
    :return: score of the deck
    """
    return sum(deck)


def start_game():
    """
    Asks the player if he wants to start a new game
    :return: the decision of the player
    """
    decision = input(f"Do you want to play Blackjack?\nType 'y' for yes and 'n' for no: ").lower()
    return decision


def winner(player):
    """
    Prints out a line saying that the input is the winner and redirects to start_game
    :param player: player/dealer - whomever is getting judged
    :return: player mentioned here wins
    """
    print(f"{player} wins!")
    # remove later
    print("def winner")


def blackjack(player, deck):
    """
    checks whether the player's deck of cards contains a blackjack already
    :param player: player/dealer - whomever is being judged
    :param deck: player's/dealer's deck of cards
    :return: if yes, winner is declared
    """
    if score_of(deck) >= 21 and len(deck) == 2:
        print(f"{player} has a blackjack!")
        # remove later
        print("def blackjack")
        winner(f"{player}")


def final_bit(player_deck, dealer_deck):
    while score_of(dealer_deck) < 17:
        dealer_deck.append(choice(av_cards))

    if score_of(dealer_deck) > 21:
        print(f"Dealer scored higher than 21")
        # remove later
        print("def final_bit 1")
        winner('Player')

    else:
        if score_of(player_deck) > score_of(dealer_deck):
            print(f"Player has scored higher than dealer")
            # remove later
            print("def final_bit 2")
            winner('Player')

        elif score_of(player_deck) == score_of(dealer_deck):
            print(f"Dealer and Player have scored equal points\nIt's a tie!")
            # remove later
            print("def final_bit 3")

        elif score_of(player_deck) < score_of(dealer_deck):
            print(f"Dealer has scored higher than player")
            # remove later
            print("def final_bit 4")
            winner('Dealer')


def recursive_bit(player_deck, dealer_deck):
    """
    *sigh*
    :return:
    """
    player_decision = ''

    while player_decision != 'n':
        player_decision = input("Do you want to draw another card?\nType 'y' for yes and 'n' for no: ")

        if player_decision == 'y':

            player_deck.append(choice(av_cards))
            print(f"The player has {player_deck}\nPlayer's score is {score_of(player_deck)}")
            print(f"The dealer has {dealer_deck[0]}")

            # check player and dealer's deck of cards for blackjack
            blackjack('Player', player_deck)
            blackjack('Dealer', dealer_deck)

            if score_of(player_deck) > 21:
                if 11 not in player_deck:
                    print(f"Player's score is above 21 and does not have an ace")
                    # remove later
                    print("def recursive_bit 1")
                    winner("Dealer")

                else:
                    for cards in player_deck:
                        if cards == 11:
                            player_deck.remove(11)
                            player_deck.append(1)

                    if score_of(player_deck) > 21:
                        # remove later
                        print("recursive_bit 2")
                        winner("Dealer")

                    else:
                        continue

if __name__ == "__main__":
    play_again = True
    while play_again:
        if start_game() == 'y':
            print(logo)
            player_deck, dealer_deck = [], []

            # available cards = av_cards
            av_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

            player_deck.append(choice(av_cards))
            player_deck.append(choice(av_cards))
            dealer_deck.append(choice(av_cards))

            print(f"The player has {player_deck}\nPlayer's score is {score_of(player_deck)}")
            print(f"The dealer has {dealer_deck}\nDealer's score is {score_of(dealer_deck)}")

            dealer_deck.append(choice(av_cards))

            recursive_bit(player_deck, dealer_deck)
            final_bit(player_deck, dealer_deck)
            print("\n\n")

        elif start_game() == 'n':
            print("Thanks for playing Blackjack!")
            play_again = False

    exit(0)
