############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.



#
# Imports
#
import random
from art import logo
import os

#
# Global variables
#


#
# Private functions
#

# clearConsole
def clearConsole():
    """
    Clears console.
    """
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

# Printlogo
def PrintLogo():
    """
    Prints blackjack game logo.-
    """
    print(logo)

# dealCard
def dealCard():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

# calculateScore
def calculateScore(cards):
    """
    Takes a list of cards and calculates the score
    """
    #  Check for a blackjack (a hand with only 2 cards: ace + 10) 
    # and return 0 instead of the actual score. 0 will represent a 
    # blackjack in our game.
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    #  Check for an 11 (ace). If the score is already over 21, remove 
    # the 11 and replace it with a 1. You might need to look up append() 
    # and remove().
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    # Return the calculation
    return sum(cards)

# compareScores
def compareScores(userScore, dealerScore):
    """
    Takes two different scores and compares them.-
    """
    # Both losers
    if userScore > 21 and dealerScore > 21:
        return "You both went over. You losers 😤"
    # Draw
    if userScore == dealerScore:
        return "Draw 🙃"
    # Dealer blackjack
    elif dealerScore == 0:
        return "Lose, opponent has Blackjack 😱"
    # User blackjack
    elif userScore == 0:
        return "Win with a Blackjack 😎"
    # User loser
    elif userScore > 21:
        return "You went over. You lose 😭"
    # Dealer loser
    elif dealerScore > 21:
        return "Opponent went over. You win 😁"
    # User > Dealer
    elif userScore > dealerScore:
        return "You win 😃"
    # Dealer > User
    else:
        return "You lose 😤"

# BlackJackGame
def BlackJackGame():
    """
    Whole blackjack game takes place here
    """
    # Print logo
    PrintLogo()
    # Deal cards
    userCards = []
    dealerCards = []
    for _ in range(2):
        userCards.append(dealCard())
        dealerCards.append(dealCard())
    # Game Over
    isGameOver = False

    # Start playing
    while not isGameOver:
        # Calculate scores
        userScore = calculateScore(userCards)
        dealerScore = calculateScore(dealerCards)
        # Print info to the user
        print(f"   Your cards: {userCards}, current score: {userScore}")
        print(f"   Dealers's first card: {dealerCards[0]}")
        print('\n')

        # Check:
        #   User Score == 0
        #   Dealer Score == 0
        #   User Score >= 21
        if userScore == 0 or dealerScore == 0 or userScore > 21:
            # Game Over
            isGameOver = True
        # Keep playing
        else:
            # Ask to draw another card
            dealNewCard = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            # Deal
            if dealNewCard == "y":
                userCards.append(dealCard())
            # No deal
            else:
                isGameOver = True
    # Let the dealer play. Draw cards unitl dealerScore > 17
    while dealerScore != 0 and dealerScore < 17:
        # Deal new card
        dealerCards.append(dealCard())
        # Compute score
        dealerScore = calculateScore(dealerCards)

    # Print new info and compare
    print(f"   Your final hand: {userCards}, final score: {userScore}")
    print(f"   Computer's final hand: {dealerCards}, final score: {dealerScore}")
    print(compareScores(userScore, dealerScore))
    print('\n')
    print('\n')

#
# main
#
if __name__ == "__main__":
    # Clear 
    clearConsole()
    # Keep playing
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        # Clear
        clearConsole()
        # Call game
        BlackJackGame()
    #
    clearConsole()
        