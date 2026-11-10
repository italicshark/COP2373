import random


class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
                 'Jack', 'Queen', 'King', 'Ace']
        self.cards = [rank + ' of ' + suit for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()


def show_hand(hand):
    for number, card in enumerate(hand, start=1):
        print(f'{number}. {card}')


def choose_cards():
    while True:
        answer = input('\nEnter card numbers to replace (1-5, separated by commas), or 0 to keep all: ')
        if answer.strip() == '0' or answer.strip() == '':
            return []
        try:
            positions = [int(item.strip()) for item in answer.split(',')]
            if positions and all(1 <= n <= 5 for n in positions) and len(positions) == len(set(positions)):
                return positions
        except ValueError:
            pass
        print('Invalid selection. Enter unique numbers from 1 to 5, such as 1, 3, 5.')


def main():
    deck = Deck()
    deck.shuffle()
    hand = [deck.deal() for _ in range(5)]

    print('=== FIVE-CARD DRAW POKER ===')
    print('\nYour original hand:')
    show_hand(hand)

    positions = choose_cards()
    for position in positions:
        hand[position - 1] = deck.deal()

    print('\nYour final hand:')
    show_hand(hand)
    print(f'\nYou replaced {len(positions)} card(s). Thanks for playing!')


if __name__ == '__main__':
    main()
