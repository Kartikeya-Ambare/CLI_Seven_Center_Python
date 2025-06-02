import random

# Defining the cards
cards = {
    1:"AH", 2:"2H", 3:"3H", 4:"4H", 5:"5H", 6:"6H", 7:"7H", 8:"8H", 9:"9H", 10:"TH", 11:"JH", 12:"QH", 13:"KH",
    14:"AD", 15:"2D", 16:"3D", 17:"4D", 18:"5D", 19:"6D", 20:"7D", 21:"8D", 22:"9D", 23:"TD", 24:"JD", 25:"QD", 26:"KD",
    27:"AC", 28:"2C", 29:"3C", 30:"4C", 31:"5C", 32:"6C", 33:"7C", 34:"8C", 35:"9C", 36:"TC", 37:"JC", 38:"QC", 39:"KC",
    40:"AS", 41:"2S", 42:"3S", 43:"4S", 44:"5S", 45:"6S", 46:"7S", 47:"8S", 48:"9S", 49:"TS", 50:"JS", 51:"QS", 52:"KS",
}

# Global desk to track played cards for each suit
global_desk = {"H": [], "D": [], "C": [], "S": []}
players = {1: [], 2: [], 3: [], 4: []}

def create_shuffled_deck(deck):
    new_deck = deck.copy() #creating a copy of the original desk list to use once more in the new game
    random.shuffle(new_deck)
    return new_deck

def get_cards_distributed(players, shuffled_deck):
    for i in range(1, 5):
        players[i] = []
    
    # Distribute 13 cards to each player i.e. player 1 to player 4
    for i in range(1, 5):
        for _ in range(13):
            if shuffled_deck:
                curr_card = shuffled_deck.pop(0)
                players[i].append(curr_card)
    return players

def display_hand_cards(player_cards, player_num):
    print(f"\nPlayer {player_num}'s cards:")
    for card_num, card_name in player_cards:
        print(f"{card_num}: {card_name}")

def get_card_value(card):
    """Extract the numeric value of a card"""
    # card is now a tuple (number, card_string:Value and Suit attached)
    card_string = card[1] if isinstance(card, tuple) else card
    if card_string[0] == 'A':
        return 1
    elif card_string[0] == 'T':
        return 10
    elif card_string[0] == 'J':
        return 11
    elif card_string[0] == 'Q':
        return 12
    elif card_string[0] == 'K':
        return 13
    else:
        return int(card_string[0])

def get_card_suit(card):
    # card is now a tuple (number, card_string)
    card_string = card[1] if isinstance(card, tuple) else card
    return card_string[1]

def is_valid_move(card, global_desk):
    """Check if a card can be played based on current desk state"""
    suit = get_card_suit(card)
    value = get_card_value(card)
    card_string = card[1] if isinstance(card, tuple) else card
    
    # If no cards played yet, only 7H can be played
    if all(len(suit_cards) == 0 for suit_cards in global_desk.values()):
        return card_string == "7H"
    
    # If this suit hasn't been started, only 7 of that suit can be played
    if len(global_desk[suit]) == 0:
        return value == 7
    
    # If suit has been started, check if card is consecutive
    suit_cards = global_desk[suit]
    played_values = [get_card_value(c) for c in suit_cards]
    min_val = min(played_values)
    max_val = max(played_values)
    
    # Card can be played if it's one higher or one lower than existing range
    return value == min_val - 1 or value == max_val + 1

def get_valid_cards(player_cards, global_desk):
    valid_cards = []
    for card in player_cards:
        if is_valid_move(card, global_desk):
            valid_cards.append(card)
    return valid_cards

def display_desk_state(global_desk):
    print("\n--- Current Desk State ---")
    for suit, cards in global_desk.items():
        if cards:
            cards_sorted = sorted(cards, key=lambda x: get_card_value(x))#Sorting in assesending order of the cards in the respective Suit
            card_strings = [card[1] if isinstance(card, tuple) else card for card in cards_sorted]
            print(f"{suit}: {' '.join(card_strings)}")
        else:
            print(f"{suit}: Empty")
    print("-" * 25)

def player_turn(player_num, players, global_desk):
    
    player_cards = players[player_num]
    
    if not player_cards: #Player's cards have ended and have no cards in his hands, hence returuning true indicating player has won the game
        return True
    
    print(f"\n{'='*50}")
    print(f"Player {player_num}'s turn")
    print(f"{'='*50}")
    
    display_desk_state(global_desk) #Displying the current deck status meaning which cards are present on the deck as of current player's turn
    display_hand_cards(player_cards, player_num)
    
    valid_cards = get_valid_cards(player_cards, global_desk)#Getting the valid cards to play, eg if previos player played 7H then if current plyaer has 8H or 6H cards in his hands, then these cards come under the valid cards
    
    if not valid_cards:
        print(f"Player {player_num} has no valid moves! Skipping turn.")#Skipping the turn as no valid cards to play currentlt to the current user
        return False
    
    print(f"\nValid cards you can play:")
    for card_num, card_name in valid_cards:
        print(f"  {card_num}: {card_name}")# Printing the the valid moves
    
    while True:
        try:
            choice = input(f"\nEnter the number of the card you want to play (or 'quit' to exit): ").strip()#inputing the number form the valid input from the user
            
            if choice.upper() == 'QUIT':
                return "quit"
            
            try:
                card_number = int(choice)
                selected_card = None
                for card_num, card_name in valid_cards:
                    if card_num == card_number:
                        selected_card = (card_num, card_name)
                        break
                
                if selected_card:
                    
                    player_cards.remove(selected_card)#Removing the card from the current player's hand 
                    suit = get_card_suit(selected_card)#retriving the house i.e. the house,clover,spades or diamond
                    global_desk[suit].append(selected_card)#Appending the selected card in there respective house or suit
                    print(f"Player {player_num} played {selected_card[1]} (#{selected_card[0]})")#Printing the valid Selected card and number of that card 
                    
                    if not player_cards:# Checking if the current player has more cards to play or not, if not has, then the player has won the game
                        return True
                    return False
                else:
                    print("Invalid card number! Please choose from the valid cards list.")
            except ValueError:
                print("Please enter a valid number or 'quit'.")
        except KeyboardInterrupt:
            print("\nGame interrupted!")
            return "quit"

def badam_satti(players):
    current_player = 1
    
    for player_num, player_cards in players.items():#Retriving the key i.e. player number and value i.e. the player holding the cards currently
        for card_num, card_name in player_cards:
            if card_name == "7H": #Finding if the current player's card contains the 7 of Hearts which is necessay card to start the game
                current_player = player_num
                print(f"\nGame starts with Player {player_num} (has 7 of Hearts)")
                break
            else:
                continue
        break
    
    game_running = True
    while game_running:
        result = player_turn(current_player, players, global_desk)#Retriving boolean value from the Player's turn function
        
        if result == "quit":
            print("Game ended by user.")
            return None
        elif result == True:
            print(f"\n🎉 Player {current_player} wins! 🎉")
            return current_player
        
        # Move to next player
        current_player = (current_player % 4) + 1
        
        # Check if all players are out of moves (shouldn't happen in normal game)
        all_stuck = True
        for player_num in range(1, 5):
            if players[player_num] and get_valid_cards(players[player_num], global_desk):
                all_stuck = False
                break
        
        if all_stuck:
            print("All players are stuck! Game ends in a draw.")
            return None


'''Start of the main Program'''

print("Welcome to Badam Satti!")
print("Rules:")
print("1. Game starts with 7 of Hearts (7H)")
print("2. After 7H, you can play 6H, 8H, or any 7 of other suits")
print("3. Cards must be played in sequence (consecutive values)")
print("4. First player to finish all cards wins!")
    
    # Create and shuffle deck
deck = []
for num, card in cards.items():
    deck.append((num, card))
    
shuffled_deck = create_shuffled_deck(deck)
    
    # Distribute cards
players_cards = get_cards_distributed(players, shuffled_deck)
    
print("\n" + "="*50)
print("CARDS DISTRIBUTED")
print("="*50)
for player, hold_cards in players_cards.items():
    print(f"Player {player}: {len(hold_cards)} cards")
    
 # Start the game
winning_player = badam_satti(players_cards)
    
if winning_player:
    print(f"\nFinal Result: Player {winning_player} is the winner!")
else:
    print("\nGame ended without a winner.")