from collections import OrderedDict
from random import shuffle
import numpy as np

class Card:

    def __init__(self, name, card) -> None:
        self.name = name
        self.KmH = card['Km/h']
        self.hp = card['hp']
        self.kmH0_100 = card['0 - 100 km/h']
        self.cc = card['cc']
        self.cilindros= card['cilindros']
        self.kg = card['kg']

    def modifyPower(self):
        pass

class Player:

    def __init__(self, name) -> None:
        self.name = name
        self.cards = OrderedDict()
        self.points = 0
        self.turn_round = 0

    def viewCards(self):
        for key in self.cards:
            print(f'''
CARD #{key}
#{self.cards[key].name}:
Km/h:           {self.cards[key].KmH}
HP:             {self.cards[key].hp}
0 - 100 km/h:   {self.cards[key].kmH0_100}
CC:             {self.cards[key].cc}
Cilindros:      {self.cards[key].cilindros}
Kg:             {self.cards[key].kg}

#################################
''')
    
    def selectCard(self):
        op0 = int(input('Select the card # you want to use: '))
        card = self.cards[op0]
        self.cards.pop(op0)
        print(f'''

PLAYER {self.name}:
#{card.name}#####################
1 - Km/h:           {card.KmH}
2 - HP:             {card.hp}
3 - 0 - 100 km/h:   {card.kmH0_100}
4 - CC:             {card.cc}
5 - Cilindros:      {card.cilindros}
6 - Kg:             {card.kg}
#################################
''')    
        op1 = int(input(f'Select the information in the card {card.name} to play: ')) if self.turn_round == 0 else op0
        return(card.__dict__[list(card.__dict__.keys())[op1]])
 
class GameSet:

    def __init__(self, *args) -> None:
        self.names = args[0]
        self.round = 0
        self.players = OrderedDict()
        self.turn = OrderedDict()

    def setPlayers(self, cards):
        nRest = len(cards)%len(self.names)
        nCards = int((len(cards)-nRest)/len(self.names))
        cards_random = list(range(nCards*2))
        shuffle(cards_random)
        players_cards_random = np.array_split(cards_random, len(self.names))
        for n in range(len(self.names)):
            self.players[n] = Player(self.names[n])
            self.players[n].turn_round = n
            playerCards = OrderedDict()
            for p,i in enumerate(players_cards_random[n]):
                playerCards[p] = Card(list(cards.keys())[i], cards[list(cards.keys())[i]])
            
            self.players[n].cards = playerCards  

    def setTurn(self, n, value):
        self.turn[self.names[n]] = value

    def verifyCards(self):
        winner = max(self.turn, key=self.turn.get)
