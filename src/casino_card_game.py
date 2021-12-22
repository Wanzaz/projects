from random import randrange

sum = 0
while sum < 21:
    print('You have', sum, 'points')
    answer = input('Turn the card over? ')
    if answer == 'yes':
        card = randrange(2, 10)
        print('You turn over', card)
        sum = sum + card
    elif answer == 'no':
        break
    else:
        print('I do not understand! Answer "yes", or "no"')

if sum == 21:
    print('Congratulations! You won!')
elif sum > 21:
    print('Bad luck!', sum, 'points is too much!')
else:
    print('It was missing only', 21 - sum, 'points!')
