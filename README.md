# CLI_Seven_Center_Python
CLI based Seven_center or commenly known as badam satti card game.
# Badam Satti Card Game
### A Python implementation of the classic Badam Satti card game for 4 players. This is a sequential card-laying game where players must strategically play cards in consecutive order to be the first to empty their hand.

## Table of Contents

### Game Overview,Rules,Installation,How to Play,Game Features,Code Structure,Functions Overview,Example Gameplay

## Game Overview
### Badam Satti is a traditional card game played with a standard 52-card deck among 4 players. Each player receives 13 cards, and the objective is to be the first player to play all their cards by following specific sequence rules.

## Rules

### Starting the Game: The game must begin with the 7 of Hearts (7H)
### Initial Moves: After 7H is played, players can play:

#### 6H or 8H (consecutive to 7H)
#### Any 7 of other suits (7D, 7C, 7S)


### Sequence Play: Cards must be played in consecutive order within each suit
### Valid Moves: A card can only be played if it's one value higher or lower than the existing range in that suit
### Winning: First player to play all their cards wins
### Skipping: If a player has no valid moves, their turn is skipped

## Installation
### Prerequisites

#### Python 3.6 or higher
#### No external dependencies required (uses only built-in libraries)

### Setup

#### Download the badam_satti.py file
#### Ensure Python is installed on your system
#### Run the game from command line

#### bash: python badam_satti.py
## How to Play

#### Game Start: Run the program and cards will be automatically distributed
#### Turn-based Play: Players take turns in order (Player 1 → 2 → 3 → 4 → 1...)
### Making Moves:

#### View your cards and valid moves
### Enter the number corresponding to the card you want to play
#### Type 'quit' to exit the game

#### Game End: Game ends when a player plays all their cards

## Sample Turn Interface
#### Player 1's turn
#### --- Current Desk State ---
#### H: 7H
#### D: Empty
#### C: Empty
#### S: Empty

#### Player 1's cards:
#### 1: AH
#### 5: 5H
#### 8: 8H
#### ...

#### Valid cards you can play:
####  5: 5H
####  8: 8H
#### Enter the number of the card you want to play (or 'quit' to exit):

## Game Features

#### Automatic Card Distribution: Random shuffling and fair distribution of 13 cards per player
#### Smart Validation: Only valid moves are allowed based on current game state
#### Visual Game State: Clear display of current desk state and player hands
#### Turn Management: Automatic turn rotation and skip handling
#### Win Detection: Automatic detection of winning conditions
#### Error Handling: Robust input validation and error messages

## Code Structure
### Data Structures

#### cards: Dictionary mapping card numbers (1-52) to card representations
#### global_desk: Tracks played cards for each suit (H, D, C, S)
#### players: Dictionary storing each player's current hand

### Card Representation
#### Cards are represented as tuples: (card_number, card_string)

#### Example: (1, "AH") represents Ace of Hearts
#### Card strings: A=Ace, T=10, J=Jack, Q=Queen, K=King

## Functions Overview
#### create_shuffled_deck(): Creates and shuffles a copy of the deck
#### get_cards_distributed():Distributes 13 cards to each of 4 players
#### display_hand_cards():Shows a player's current cards
#### get_card_value():Extracts numeric value from card (A=1, T=10, etc.)
#### get_card_suit():Extracts suit from card (H, D, C, S)
#### is_valid_move():Validates if a card can be legally played
#### get_valid_cards():Returns list of playable cards for current player
#### display_desk_state():Shows current state of played cards
#### player_turn():Handles individual player's turn logic
#### badam_satti():Main game loop and flow control

## Example Gameplay
### Game Initialization
#### Welcome to Badam Satti!
#### Rules:
#### 1. Game starts with 7 of Hearts (7H)
#### 2. After 7H, you can play 6H, 8H, or any 7 of other suits
#### 3. Cards must be played in sequence (consecutive values)
#### 4. First player to finish all cards wins!

#### CARDS DISTRIBUTED
#### Player 1: 13 cards
#### Player 2: 13 cards
#### Player 3: 13 cards
#### Player 4: 13 cards

#### Game starts with Player 2 (has 7 of Hearts)
#### Mid-Game State
#### --- Current Desk State ---
#### H: 6H 7H 8H 9H
#### D: 7D
#### C: Empty
#### S: Empty

#### Player 3's cards:
#### 15: 2D
#### 23: TD
#### 41: 2S
#### ...

#### Valid cards you can play:
####   15: 2D (if 3D-6D range allows)
####   23: TD (if 8D-9D range allows)

### Technical Notes
#### Memory Efficient: Uses list operations and dictionary lookups for optimal performance
#### Input Validation: Handles invalid inputs gracefully with clear error messages
#### Modular Design: Well-separated functions for easy maintenance and testing
#### Game State Management: Consistent tracking of all game elements

### Troubleshooting
#### Common Issues

#### "Invalid card number": Ensure you're entering a number from the valid cards list
#### "No valid moves": Your turn will be automatically skipped
#### Game stuck: All players stuck scenario is handled with draw declaration

### Exit Options

#### Type 'quit' during your turn to exit
#### Use Ctrl+C for immediate termination