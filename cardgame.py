from random import shuffle

suite = "H D S C".split()
rank = "2 3 4 5 6 7 8 9 10 J K Q A".split()

class deck:
    def __init__(self):
        self.allcrads = [(s,r) for s in suite for r in rank]

    def shuflle_deck(self):
        print("SHUFLLING THE DECK OF CARDS")
        shuffle(self.allcrads)

    def distribute(self):
        print("Spliting Deck")
        return (self.allcrads[:26],self.allcrads[26:])

class hand:
    def __init__(self,cards):
        self.cards = cards

    def add_card(self,card):
        print("Adding a card to deck")
        self.cards.extend(card)

    def remove_card(self):
        return self.cards.pop()

class Player:
    def __init__(self,name,hand):
        self.name = name
        self.hand = hand
    def play_card(self):
        card = self.hand.remove_card()
        print("{} card to played {}".format(card,self.name))
        return card

    def war(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return war_cards
        else:
            for i in range(3):
                war_cards.append(self.hand.remove_card())
            return war_cards

    def remaining(self):
        return len(self.hand.cards) != 0
######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

# Use the 3 classes along with some logic to play a game of war!
deck = deck()
deck.shuflle_deck()
name = input("You name: ")
half1,half2 = deck.distribute()

player_com = Player('computer',hand(half1))
player_user = Player(name,hand(half2))

war_count = 0
round = 0
while(player_com.remaining() and player_user.remaining()):

    print("It is time for a new round!")
    print("Here are the current standings: ")
    print(player_user.name+" count: "+str(len(player_user.hand.cards)))
    print(player_com.name+" count: "+str(len(player_com.hand.cards)))
    print("Both players play a card!")
    print('\n')

    round += 1

    card_user = player_user.play_card()
    card_com =  player_com.play_card()

    #comparison
    table_card = []
    table_card.append(card_com)
    table_card.append(card_user)

    if (card_com[1] == card_user[1]):
        war_count += 1
        print('WAR')

        table_card.extend(player_user.war())
        table_card.extend(player_com.war())

        if rank.index(card_com[1]) < rank.index(card_user[1]):
            player_user.hand.add_card(table_card)
        else:
            player_com.hand.add_card(table_card)

print('Rounds were '+ str(round))
print('Wars were ' +str(war_count))
