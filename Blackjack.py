
import random

class Card:
  card_rank=["A░", "2░","3░","4░","5░","6░","7░","8░","9░","10","J░","Q░","K░"]
  card_suit_image=['♠', '♥', '♣', '♦', '░']
  
  line_top=   '┌─────────┐\t'
  line_middle='│░░░░░░░░░│\t'
  line_rank_left= '│░'
  line_rank_right= '░░░░░░│\t'
  line_suit_left=  '│░░░░'
  line_suit_right= '░░░░│\t'
  line_bottom='└─────────┘\t'

  def __init__(self, value):
    # Can't really do error checking of value here, assume value is within 0 and 51
    # The proper way of implementing this is with raising an exception when value is out of range
    self.card_value=value

  def get_suit_image(self):
    return self.card_suit_image[self.card_value//13]

  def get_value(self):
    # This is specific to the implementation of BJ
    # To keep it simple for the students, don't use inheritance here, but technically, inheritance is needed 
    # because interpretation of a card value is game specific
    # maybe just let the BJ_hand implement value of a card
    # This method only returns a value from 0-12 indicating "A" - "K"
    return self.card_value%13

  def get_rank_image(self):
    return self.card_rank[self.card_value%13]

  def print_card(self, show_back=False):
    # prints the poker card
    for line in self.get_card_image(show_back):
      print(line)

  def get_card_image(self, show_back=False):
    # returns the card's text, line by line
    # can be used by the caller to print multiple cards line by line
    ct=[]
    ct.append(self.line_top)
    ct.append(self.line_middle)
    ct.append(self.line_middle if show_back else \
      self.line_rank_left+self.get_rank_image()+self.line_rank_right)
    ct.append(self.line_middle if show_back else \
      self.line_suit_left+self.get_suit_image()+self.line_suit_right)
    ct+=[self.line_middle]*3
    ct.append(self.line_bottom)
    return ct

class Card_Deck:
  def __init__(self):
    # What to do about jokers?  
    # Currently not implemented
    # How would they be implemented?  
    self.__create_new_deck__()

  def __create_new_deck__(self):
    self.cards_dealt=[]
    self.cards=[Card(i) for i in range(52)]
      
  def shuffle(self):
    self.__create_new_deck__()
    random.shuffle(self.cards)

  def deal_card(self):
    # returns a Card object if the deck is empty returns None
    if len(self.cards):
      self.cards_dealt.append(self.cards.pop(0))
      return self.cards_dealt[-1]
    else:
      return None
    
  def get_cards_remaining(self):
    return len(self.cards)

class BJ_Hand:
  # This class implements a hand of BJ cards with following functionality
  #   1. printing the cards out
  #   2. Computes the hand's total value, whether the hand is a bust, etc
  card_value=[1,2,3,4,5,6,7,8,9,10,10,10,10]

  def __init__(self, cards=None):
    self.cards_in_hand=[] if cards is None else cards

  def print(self, col_size=2, cover_first_card=False):
    # prints the entire hand horizontally, how many cards across? 
    if len(self.cards_in_hand)==0: return
    # Let's build a 2D list of card text images, the rows contain each card's 
    # text
    ct=[]
    for i,c in enumerate(self.cards_in_hand):
      ct.append(c.get_card_image(i==0 and cover_first_card))
    for x in range(8):
      for y in range(len(self.cards_in_hand)):
        if(len(self.cards_in_hand) - 1 == y):
          print(ct[y][x])
        else:
          print(ct[y][x], end = "   ")
      
  def score(self):
    # returns the value of the entire hand
    cv=[self.card_value[c.get_value()] for c in self.cards_in_hand]
    score=sum(cv)
    if cv.count(1): # there's at least an Ace in the hand
      score+=10 if score+10<=21 else 0
    return score

  def is_bust(self):
    # returns True/False whether the hand is a bust
    return True if self.score()>21 else False

  def get_num_cards(self):
    return len(self.cards_in_hand)

  def add_card(self, card):
    self.cards_in_hand.append(card)

class BJ_Game:
  def __init__(self):
    # create the card deck and shuffle it
    self.deck=Card_Deck()
    self.deck.shuffle()

  #Total states: 5

  # State 0: Initial state
  #   Deal cards to the player and the dealer
  #   Display the cards of the player and the dealer
  #   Check if player has Blackjack (A and 10 cards) then goto state 3


  # State 1: Player plays Blackjack
  # Stay in this state until 3 conditions:
  #    i. the player stays (decides not to take another card)
  #    ii. the player busts (went over 21)
  #    iii. the card deck is empty when the player hits
  #    iv. check for 5 card Charlie
  #    *** I'll let you figure out what states to transition to ***


  # State 2: Dealer plays Blackjack
  # Stay in this state until the following conditions:
  #    i. dealer keeps hitting until reaching score of 17
  #    ii. dealer goes bust
  #    iii. the card deck is empty when the dealer hits


  # State 3: Check winner
  #    i. Computes the scores of each player and dealer
  #    ii. Prints who won the game
  #    iii. Ask if the player wants to play again
  #    iv. If the player wants to play then goto state 0
  #          else goto state 4

  # State 4: ending game clean up
  #    If the card deck was empty when the player or dealer hits, then
  #       print "Card deck is empty, Game Over!"
  #       otherwise just print "Game Over!"
  #    exit the program
  
  def play(self):
    state=0
    while True:
      if state==0:
        if self.deck.get_cards_remaining()>=4:
          self.player=BJ_Hand()
          self.dealer=BJ_Hand()
          for i in range(2):
            self.player.add_card(self.deck.deal_card())
            self.dealer.add_card(self.deck.deal_card())
          print("Player's Hand: ")
          self.player.print()
          print("Dealer's Hand: ")
          self.dealer.print(cover_first_card=True)
          state=3 if self.player.score()==21 else 1 # set to state=3 if player has a blackjack in hand
        else:
          print("Not enough cards, only", self.deck.get_cards_remaining(), "card(s) left in the deck.")
          state=4
      elif state==1:
        # player plays blackjack
        stay = input("Hit or stay? h/s")
        if stay == "s":
          state = 2
        elif self.deck.get_cards_remaining() > 1:
          self.player.add_card(self.deck.deal_card())
          self.player.print()
          if self.player.is_bust():
            state = 3
          if self.player.get_num_cards() == 5:
            state = 3
        else:
          print("Not enough cards")
          state = 4
        pass
      
      elif state==2:
        while self.dealer.score() <= 17:
          if self.deck.get_cards_remaining() > 1:
            self.dealer.add_card(self.deck.deal_card())
          else:
            print("Not enough cards")
            state = 4
        # Dealer plays
        state = 3
        pass

      elif state==3:
        # display score and check bust or not
        # prompt for continue game or quit
        print("Player's Hand: ")
        self.player.print()
        print("Dealer's Hand: ")
        self.dealer.print(cover_first_card=False)
        if self.player.is_bust():
          print("Bust! Dealer wins!")
        elif self.player.get_num_cards() == 5:
          print("5 card charlie! Player wins!")
        elif self.player.score() == self.dealer.score:
          print("Tie!")
        elif self.dealer.is_bust():
          print("Dealer Busts! Player wins!")
        elif self.player.score() > self.dealer.score():
          print("Player wins!")
        else:
          print("Dealer wins!")
        continue_or_quit = input("Do you want to keep playing? y/n")
        if continue_or_quit == "y":
          state = 0
        else:
          state = 4

      elif state==4:
        # End of the game
        print("Game Over!!!")
        break


game=BJ_Game()
game.play()
