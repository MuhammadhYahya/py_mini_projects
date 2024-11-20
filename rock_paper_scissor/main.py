import random

ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'
emojis = { ROCK: '🗿', SCISSORS: '✂️', PAPER: '📃' }
choices = ('r','p','s')

while True:
    user_input = input('Rock, paper, or scissors? (r, p, s): ').lower()
    if user_input not in choices:
        print('invalid input 😕')
        continue

    comp_choices=random.choice(choices)

    print(f'you chose {emojis[user_input]}')
    print(f'computer chose {emojis[comp_choices]}')

    if user_input==comp_choices:
        print('Tie! 🤝')
    elif (
        (user_input=='s' and comp_choices=='p') or
        (user_input=='p' and comp_choices=='r') or
        (user_input=='r' and comp_choices=='s')):
        print('you win 🏆')
    else:
        print('you lose 🙁')

    should_continue=input('want to continune? (y/n) :').lower()
    if should_continue=='n':
        print("Thanks for playing! See you next time! 👋")
        break
        
