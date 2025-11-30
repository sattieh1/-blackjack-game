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
        while True:
            hit_or_stand = input("Hit or Stand")
            if hit_or_stand.lower() == "hit":
                self.player.add_card(self.deck.deal_card())
                print(f"You got a {self.player.hand[-1]}")
                print(f"Total: {self.player.get_hand_value()}")
            if hit_or_stand.lower() == "stand":
                print("Let see what the dealer has!")
                break
            if self.player.is_bust():
                print("BUST! You went over 21!")
                break    
        # Dealer wins or dealer shows card
        if self.player.is_bust():
            self.player.lose_bet()
            print(f"The Dealer won, and your new balance is {self.player.balance}")
            #Cashout()  
        else:
            print(f"Dealer has a {self.dealer.hand[-1]}") #show second card
            print(f"Dealer's Total: {self.dealer.get_hand_value()}")
            while self.dealer.get_hand_value() < 17:
                self.dealer.add_card(self.deck.deal_card())
                print(f"Dealer got a {self.dealer.hand[-1]}")
                print(f"Dealer's Total: {self.dealer.get_hand_value()}")
                if self.dealer.is_bust():
                    print("The Dealer is BUST")
                    break
            #Who won?        
            if self.dealer.is_bust():
                print("Player Won")
                self.player.win_bet()
                print(f"Your balance is now {self.player.balance}")
            else:
                print(f"The dealer has a value of{self.dealer.get_hand_value()} and player has a value of {self.player.get_hand_value()}")
                if self.player.get_hand_value() > self.dealer.get_hand_value():
                    print("Player Won")
                    self.player.win_bet()
                    print(f"Player balance is now {self.player.balance}")
                elif  self.player.get_hand_value() < self.dealer.get_hand_value():
                    print("Dealer Won")
                    self.player.lose_bet()
                    print(f"Player balance is now {self.player.balance}")
                else:
                    print("It's a Tie")
                    print(f"Player balance is now {self.player.balance}")   

game = Game()
game.play()
               






            

            
                

                    


        
    









