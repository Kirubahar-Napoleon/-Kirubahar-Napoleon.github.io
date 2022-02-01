import random
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': [11]}


class carddeck():
    suits = ('\u2665','\u2660','\u2663','\u2666')
    face = ('2','3','4','5','6','7','8','9','10','J','Q','K','A')

    def __init__(self):
        self.deck = []
        for suit in self.suits:
            for face in self.face:
                card = face+suit
                self.deck.append(card)

    def __str__(self):
        return 'Deck of card is' + f'{self.deck}'

    def shuffledeck(self):
        random.shuffle(self.deck)
        return self.deck

class player:

    def __init__(self,name,amount):
        self.name = name
        self.amount = amount
        self.hand = []
    
    def credit(self,val):
        self.amount = self.amount + val

    def debit(self,val):
        self.amount = self.amount - val
        if self.amount > 0:
            return True
    
    def playercards(self,card):
        self.hand.append(card)
    
    def __len__(self):
        return len(self.hand)

    def __del__(self):
        print("Thanks for Playing! \n  Have a nice day ahead \n Bye Bye !!!")

class comp:
    def __init__(self):
        self.comphand = []
    
    def compcards(self,card):
        self.comphand.append(card)
    
    def __len__(self):
        return len(self.comphand)


def wincheck():
    compvalue = 0
    playervalue = 0

print ('Hi There! Thanks for playig our game')
name = input('Please tell us your name ')

bet = int(input('How much would you like to bet'))

d = carddeck()
c = comp()
p = player(name,bet)
print(d)
print(d.shuffledeck())
