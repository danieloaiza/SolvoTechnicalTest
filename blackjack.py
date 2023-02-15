"""
Deck class
Contains the complete deck for the blackjack game
"""
class Deck():
    def __init__(self):
        self.deck = self.create_deck()
        
    def __str__(self):
        return f'The complete deck is: {self.deck}'
        
    def updateDeck(self, updatedDeck):
        self.deck = updatedDeck
        
    def create_deck(self):
        cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        cardsType = ["H", "D", "C", "S"]
        self.completeDeck = []
        for cType in cardsType:
            for elem in cards:
                card = [elem, cType]
                self.completeDeck.append(card)
        return self.completeDeck
    
    
print(Deck())