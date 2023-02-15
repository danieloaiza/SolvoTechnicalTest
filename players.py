import random
import blackjack
"""
Player class
Creates a new player, and gives them two random cards
"""
class Player():
    def __init__(self, deck):
        self.playerCards = self.selectRandomCards(deck)
        
    def __str__(self):
        return f'The player cards are: {self.playerCards}'
    
    def selectRandomCards(self, deck):
        self.selectedCards = []
        for i in range(0, 2):
            self.selectedCards.append(deck.pop(random.randint(0, len(deck)-1)))
        return self.selectedCards
    
testDeck = blackjack.Deck().completeDeck

print(Player(testDeck))

        