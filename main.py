import random as rand

suits = ["S", "C", "H", "D"]
rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    
def get_card():
    return rand.choice(rank) + rand.choice(suits)

def get_hand():
    return [get_card() for _ in range(5)]

def print_hand(hand):
    for i, card in enumerate(hand):
        print(str(i+1) + ": " + card)

def get_cards_to_replace():
    result = [-1]
    try:
        str_to_replace = input("Enter the positions of the cards you want to replace, separated by commas, or hit enter.\n")
        str_to_replace = "".join(str_to_replace.split())
        if str_to_replace:
            result = list(map(int, str_to_replace.split(",")))
        else:
            result = []
    except ValueError:
        print("Sorry, I didn't understand that! Try again.")
    return result

def get_ranks(hand):
    ranks = [rank.index(card[:-1]) for card in hand]
    ranks.sort(reverse=True)
    return ranks

def decide_winner(hand, dealer_hand):
    player_high_cards = get_ranks(hand)
    dealer_high_cards = get_ranks(dealer_hand)
    for check_fn in check_fns:
        if check_fn(hand):
            if not check_fn(dealer_hand):
                return "player"
            else:
                return "player" if player_high_cards > dealer_high_cards else "dealer"
        elif check_fn(dealer_hand):
            return "dealer"
    if player_high_cards > dealer_high_cards:
        return "player"
    elif dealer_high_cards > player_high_cards:
        return "dealer"
    else:
        return "tie"
    
def poker():
    hand = get_hand()
    dealer_hand = get_hand()
    print("Your hand is:")
    print_hand(hand)
    arr_to_replace = [-1]
    while arr_to_replace and not all(1 <= i <= 5 for i in arr_to_replace):
        arr_to_replace = get_cards_to_replace()
    for i in arr_to_replace:
        hand[i-1] = get_card()
    print("Your new hand is:")
    print_hand(hand)
    print("The dealer's hand is:")
    print_hand(dealer_hand)
    winner = decide_winner(hand, dealer_hand)
    if winner == "player":
        print("Congratulations! You win!")
    elif winner == "dealer":
        print("Oh no! The dealer won this round.")
    else:
        print("It's a tie!")

def get_value(card):
    return card[:-1]

def get_numeric_value(card):
    return rank.index(card[:-1]) + 2

def get_suit(card):
    return card[-1:]
    
# ---------------------------------------------
# You don't need to change anything above here.
# ---------------------------------------------

def is_pair(hand):
    # To determine if we have a pair, we need to look at just the values of the cards,
    # and check if any of the values appear more than once. To do this, we'll first
    # get all of the values using get_value() and put them in their own array, then
    # check how many times each value in that array appears using .count().
    
    card_values = []
    int_i = 0 # Initialize our counter
    while int_i < len(hand): # Loop over each value in the hand array using a while loop
        card = hand[int_i] # Get the next element of hand
        card_value = get_value(card) # Get the value of the card
        card_values.append(card_value) # Add the value to our values list
        int_i += 1 # Increment our counter

    for value in card_values: # Loop over each value in our values array using a for loop
        # We don't need to declare a counter, because the for loop will automatically
        # set value to each item in card_values, one at a time. If you're not sure what
        # that means, try adding a print statement that prints value inside the loop.
        count_result = card_values.count(value) # Count appearances of value
        if count_result > 1: # If we have 2 or more of the same value
            return True # Then there's a pair! And so we can return True.

    return False # OUTSIDE the for loop. Once we've looped over every value, if none of
                 # them have a count that's greater than 1, that means we can't have a
                 # pair, since a pair would have a count of 2. So since there are no
                 # pairs, we return False.
        

def is_two_pairs(hand): # Extra credit
    return False

def is_three_of_a_kind(hand):
    # Replace this code with working code! Should return either True or False based on the hand.
    return False

def is_straight(hand): # Extra credit.
    return False

def is_flush(hand):
    # Replace this code with working code! Should return either True or False based on the hand.
    return False

def is_full_house(hand): # Extra credit.
    return False

def is_four_of_a_kind(hand):
    # Replace this code with working code! Should return either True or False based on the hand.
    return False

def is_straight_flush(hand): # Extra credit.
    return False

# ---------------------------------------------
# You don't need to change anything below here.
# ---------------------------------------------
check_fns = [is_straight_flush, is_four_of_a_kind, is_full_house, is_straight, is_flush, is_three_of_a_kind, is_two_pairs, is_pair]

if __name__ == "__main__":
    poker()
