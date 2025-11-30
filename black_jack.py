class Cards:

    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"    

class Deck:

    def __init__(self):
        self.cards = [Cards(suit, rank) for suit in Cards.suits for rank in Cards.ranks]
    
    def shuffle(self):
        import random
        random.shuffle(self.cards)
    
    def deal_card(self):
        return self.cards.pop() if self.cards else None

class Hand:

    def __init__(self):
        self.hand =[]

    def add_card(self, card):
        self.hand.append(card)

    def get_hand_value(self):
        total = 0
        for card in self.hand:
            if card.rank in ("Jack", "Queen", "King"):
                total += 10
            elif card.rank == "Ace":
                total += 11
            else: 
                total += int(card.rank)
        return total

    def is_bust(self):
        return self.get_hand_value() > 21

class Player(Hand):

    def __init__(self, starting_balance):
        super().__init__()
        self.balance = starting_balance
        self.current_bet = 0
    
    def place_bet(self, bet_value):
        self.current_bet = bet_value

    def win_bet(self):
        self.balance += self.current_bet
        self.current_bet = 0

    def lose_bet(self):
        self.balance -= self.current_bet
        self.current_bet = 0





class Dealer(Hand):

    def __init__(self):
         super().__init__()




class Game:

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        starting_balance = int(input("How much do you want to start with? $"))
        self.player = Player(starting_balance)
        self.dealer = Dealer()

    def play(self):
    print(f"Welcome to Blackjack!\nYour current balance is ${self.player.balance}")
    
    # Place Bet
    bet_value = int(input("How much do you want to bet? $"))
    self.player.place_bet(bet_value)
    
    # Deal Cards
    self.player.add_card(self.deck.deal_card())
    self.dealer.add_card(self.deck.deal_card())
    self.player.add_card(self.deck.deal_card())
    self.dealer.add_card(self.deck.deal_card())
    
    # Show cards
    print(f"\nYour cards: {self.player.hand[0]} and {self.player.hand[1]}")
    print(f"Total: {self.player.get_hand_value()}")
    print(f"\nDealer shows: {self.dealer.hand[0]} and ??")

    # Hit or Stand
    count = 3
    while player.get_hand_value() <= 21:
        hit_or_stand = input("Hit or Stand")
        if hit_or_stand == "Hit" or "hit":
            self.player.add_card(self.deck.deal_card())
            print("You got a {self.player.hand[{count}]})
            count +=1
            if player.get_hand_value() >= 21:
                

                    


        
    









