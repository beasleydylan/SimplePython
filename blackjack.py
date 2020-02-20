import random
class Deck():
    def __init__(self):
        self.spades = ['A','K','Q','J','10','9','8','7','6','5','4','3','2','1']
        self.hearts = ['A','K','Q','J','10','9','8','7','6','5','4','3','2','1']
        self.clubs = ['A','K','Q','J','10','9','8','7','6','5','4','3','2','1']
        self.diamonds = ['A','K','Q','J','10','9','8','7','6','5','4','3','2','1']
        self.suits = {'spades':self.spades, 'clubs':self.clubs, 'diamonds':self.diamonds, 'hearts':self.hearts}
    def deal(self):
        suit = random.choice(list(self.suits))
        card = random.choice(self.suits.get(suit))
        self.suits.get(suit).pop(self.suits.get(suit).index(card))
        lis = [suit, card]
        return lis
    def all_cards(self):
        lis = list(self.suits.values())
        for i in lis:
            print(i)
    def shuffle(self):
        self.spades = ['A','K','Q','J','10','9','8','7','6','5','4','3','2']
        self.hearts = ['A','K','Q','J','10','9','8','7','6','5','4','3','2']
        self.clubs = ['A','K','Q','J','10','9','8','7','6','5','4','3','2']
        self.diamonds = ['A','K','Q','J','10','9','8','7','6','5','4','3','2']
        self.suits = {'spades':self.spades, 'clubs':self.clubs, 'diamonds':self.diamonds, 'hearts':self.hearts}
        print('Deck is shuffled.')
class Hand():
    def __init__(self):
        self.str1 = ''
        self.faces = ['K', 'Q', 'J']
    def get_hand(self, lis):
        self.str1 = ''
        for i in lis:
            self.str1 += i[1] + " of " +i[0] + " "
        return self.str1
    def value_of_hand(self, lis):
        tot = 0
        value = False
        for i in lis:
            if i[1] in self.faces:
                tot += 10
            elif i[1] == 'A':
                value = True
            else:
                tot += int(i[1])
        if value:
            if (tot + 11) > 21:
                tot += 1
            else:
                tot += 11
        return tot
class Monies():
    def __init__(self):
        self.monies = 0
    def get_monies(self):
        return self.monies
    def set_monies(self, x):
        if x == 0:
            x = int(input('How much money do you want? Needs to be greater than or equal to $25: '))
        while x < 25:
            x = int(input("Number does not fit requirements, try again: "))
        self.monies = x
    def bet(self, bet):
        self.monies -= bet
def hit_me(lis):
    lis.append(deck.deal())
    hand.value_of_hand(lis)
    return hand.get_hand(lis)
def bust(lis):
    value = hand.value_of_hand(lis)
    if value > 21:
        return 0
    else:
        return 1
deck = Deck()
hand = Hand()
monie = Monies()
endGame = False
x = 0
monie.set_monies(x)
while not endGame:
    deck.shuffle()
    dealer = [deck.deal(),  deck.deal()]
    player = [deck.deal(),  deck.deal()]
    print("Welcome to blackjack. The goal is to get 21, or as close as you can. If you go over you bust, and lose the hand.")
    x = input('You must bet $25 on each hand, and entry fee is up to you. Are you ready to play? ')
    if x.lower() == 'yes':
        print('Gucci lets play.')
    else:
        endGame = True
        break
    if monie.get_monies() - 25 == 0:
        print('This is your last round, if no money left will be prompted for more.')
    monie.bet(25)
    print(f'This is your total monies: {monie.get_monies()}')
    print(hand.get_hand(player))
    player_value = hand.value_of_hand(player)
    print(f'Value of your hand is {player_value}')
    print(f'This is dealer hand: {dealer[0][1]} of {dealer[0][0]}')
    hit = 'yes'
    bust1 = bust(player)
    count = 0
    while hit == 'yes' and count != 3:
        hit = input('Would you like another card, or stay? Type yes or no: ')
        if hit.lower() == 'no':
            break
        else:
            hit_me(player)
        bust1 = bust(player)
        if bust1 == 0:
            print(hand.get_hand(player))
            print(f'Value of your hand is {hand.value_of_hand(player)}')
            hand.get_hand(player)
            print('You bust dealer wins.')
            bust1 = True
            break
        print(hand.get_hand(player))
        print(f'Value of your hand is {hand.value_of_hand(player)}')
        count += 1
    bust1 = bust(player)
    if count == 3:
        x = input('You won, five cards is auto win! Play again?')
        value = monie.get_monies() + 50
        monie.set_monies(value)
        print(monie.get_monies())
        if x == 'no':
            endGame = True
        break
    if bust1 == 0:
        get = input('You lost. Play again? Type yes or no ')
        value = monie.get_monies() + 50
        monie.set_monies(value)
        print(monie.get_monies())
        if get == 'yes':
            endGame = False
        else:
            endGame = True
        continue
    name = False
    counter = 2
    while hand.value_of_hand(player) > hand.value_of_hand(dealer):
        hit_me(dealer)
        bust1 = bust(dealer)
        counter+=1
        if counter == 5 and bust1 == 1:
            x = input('Dealer won with max of 5 cards. Play again?')
            monie.set_monies(value)
            print(monie.get_monies())
            if x.lower() == 'no':
                endGame = True
            else:
                name = True
            break
        elif bust1 == 0:
            print(hand.get_hand(dealer))
            x = input('The dealer bust and you won! Play again? ')
            value = monie.get_monies() + 50
            monie.set_monies(value)
            print(monie.get_monies())
            if x.lower() == 'no':
                endGame = True
            else:
                name = True
        print(f'Dealers cards are: {hand.get_hand(dealer)}')
        print(f'Value of dealer hand is {hand.value_of_hand(dealer)}')
    if endGame or name:
        continue    
    if hand.value_of_hand(player) == hand.value_of_hand(dealer):
        print(hand.get_hand(dealer))
        print(f'Value of dealer hand is {hand.value_of_hand(dealer)}')
        print(hand.get_hand(player))
        print(f'Value of your hand is {hand.value_of_hand(player)}')
        x = input('It was a tie, play again? ')
        value = monie.get_monies() + 25
        monie.set_monies(value)
        print(monie.get_monies())
        if x == 'no':
            endGame = True
    else:
        print(hand.get_hand(dealer))
        print(f'Value of dealer hand is {hand.value_of_hand(dealer)}')
        x = input('You lost! Play again? ')
        if x == 'no':
            endGame = True
    if monie.get_monies() == 0:
        x = input('You are out of money. If you want to play again type yes or no: ')
        if x.lower() == 'yes':
            monie.set_monies(0)
            endGame = False
        else:
            endGame = True
            print('Play again soon!')