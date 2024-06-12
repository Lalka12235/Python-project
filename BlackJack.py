import random
global card
card = 0
x = 0
c = 0
d = 0


def start(a:int):
    global card
    start_1 = input('Enter start \n' )
    if start_1 == 'start':
         for i in range(1,2):
             card += random.randint(1, 11)
             if card <= 21:
                print(f'Your cards: {card} ')
    else:
        print('Error')

def bot(c):
    global card
    c = 'start'
    if c == 'start':
        for i in range(1, 2):
            card += random.randint(1, 11)
            if card <= 21:
                print(f'Enemy cards: {card} ')
    else:
        print('Error')



while card == 21 or card < 20 or card > 21:
    def hit(add):
        global card
        add = 0
        hit_1 = input('Enter add to add points and no add to skip a move \n')
        if hit_1 == 'add':
            add = random.randint(1, 11)
            card += add
            print(f'Your cards: {card}')
        elif hit_1 == 'no add':
            print(f'Your cards: {card}')


    def bot_play(bot):
        global card
        bot = 0
        if card <= 16:
            bot_1 = 'add'
        elif card >= 17:
            bot_1 = 'no add'
        if bot_1 == 'add':
            add = random.randint(1, 11)
            card += add
            print(f'Enemy cards: {card}')
        elif bot_1 == 'no add':
            print(f'Enemy cards: {card}')


    def end(endless):
        global card
        if card == 21:
            print('You win')
        elif card < 21:
            if bot_play(card) < card:
                print('You win')
            elif bot_play(card) > card:
                print('you lose')
            elif bot_play(card) == card:
                print('Draw')
        elif card > 21:
            print('You lose')


    start(x)
    hit('add' or 'no add')
    bot_play(c)
    hit('add' or 'no add')
    bot_play(c)
    hit('add' or 'no add')
    bot_play(c)
    end(d)
    break