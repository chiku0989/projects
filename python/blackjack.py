#importing libs
import random

  
#Declaring Global var
suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two': 2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}
playing = True


#CLASSES

#creating a Card class

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank + " of " + self.suit

#creating a Deck class which will contain 52 instance of Card class

class Deck:
    def __init__(self):
        self.all_cards= []
        for suit in suits:
            for rank in ranks:
                current_card = Card(suit,rank)
                self.all_cards.append(current_card)
    
    def __str__(self):
        deck_comp =''
        for card in self.all_cards:
            deck_comp+= '\n' + card.__str__()
        return deck_comp

    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal(self):
        single_card = self.all_cards.pop()
        return single_card

#Creating a Hand class which will hold the cards from deck

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        
        if card.rank == 'Ace':
            self.aces +=1;
        
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

#creating a chip class

class Chips:
    def __init__(self,total = 100):
        self.total = total
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
        
    def lose_bet(self):
        self.total -= self.bet

#END OF CLASSES 





#USER-DEFINE FUNCTIONS

#f1 this funcion takes bet from the user 
def take_bet(chips):
    while True:
        
        try :
            chips.bet = int(input("How many chips would you like to bet : "))
        except :
            print("Sorry, Please provide integer")
        else:
            if(chips.bet > chips.total):
                print(f"Sorry, your bet cannot exceed {chips.total}")
            else:
                break
#f2   this function will deal one card from the deck
#and it will all that card to player's or dealer's hand         
def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

#f3 asks user if they want to hit or stand
def hit_or_stand(deck,hand):
    global playing
    
    while True:
        x = input('Hit or Stand? Enter h or s : ')
        
        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print("Player Stands Dealer's turn")
            playing = False
        else:
            print("Sorry, I did not understand that")
            continue
        break
        
#f4 it shows 1 card of dealer and all the cards of user
def show_some(player,dealer):
    #shows dealer's card
    print("\nDealer's Hand : ")
    print("First Card Hidden!: ")
    print(dealer.cards[1])
    
    #shows player's card 
    print("\nPlayer's Hand")
    for card in player.cards:
        print(card)
        
#f5 shows all the cards of dealer and player
def show_all(player, dealer):
    #shows Dealer's all card
    print("\nDealer's Hand")
    for card in dealer.cards:
        print(card)
    
    print(f"Value of Dealer's hand is : {dealer.value}")
        
    #shows player's card
    print("\n Player's Hand")
    for card in player.cards:
        print(card)
        
    print(f"Value of Player's Hand is : {player.value}")
    
#f6 this function will be call when player's hand is >21
def player_busts(player,dealer,chips):
        print("Player Bust!")
        chips.lose_bet()
    
#f7 this function will be called when player's hand > dealer's hand
def player_wins(player,dealer,chips):
        print("Player Wins!")
        chips.win_bet()

#f8 this function will be called when dealer's hand > 21
def dealer_busts(player,dealer,chips):
        print("Player Wins! Dealer busted")
        chips.win_bet()
#f9 this function will be called when dealer's hand > player's hand 
def dealer_wins(player,dealer,chips):
        print("Dealer Wins!")
        chips.lose_bet()
# f10 this function will be used if there is a tie among dealer and player       
def push(player,dealer):
    print("Dealer and player tie !PUSH")

#END OF USER-DEFINE FUNCTIONS

###GAME LOGIC###
while True:
    
    #opening statement
    print("Hello, Welcome to BlackJack!")
    
    #create a deck
    deck = Deck()
    deck.shuffle()
    
    #creating player hand and dealing cards
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    #creating dealer hand and dealing cards 
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    #giving player chips to bet
    player_chips = Chips()
    
    #taking bet from player 
    take_bet(player_chips)
    
    #showing few cards
    show_some(player_hand,dealer_hand)
    
    while playing:
        
        #asking hit or stand
        hit_or_stand(deck,player_hand)
        
        #showing cards
        show_some(player_hand,dealer_hand)
        
        #if player's hand exceeds 21 then run player_busts() and break out of loops
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
            
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
            
        show_all(player_hand,dealer_hand)
        
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
            
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
            
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
            
        else:
            push(player_hand,dealer_hand)
        
    print(f"\n Player's total chips are : {player_chips.total}")
    
    new_game = input("would you like to play again? Y/N : ")
    
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thank you for playing")
        break
        