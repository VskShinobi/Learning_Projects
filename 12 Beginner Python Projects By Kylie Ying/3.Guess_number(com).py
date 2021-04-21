import random

def guess_com (y):
    low = 1
    high = y 
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f'is {guess} is low(l) or high(h) or correct(c)').lower()
        if feedback == 'h':
            high = guess - 1 
        elif feedback == 'l':
            low = guess + 1
    print('You guess it')

h = int(input("Choose Your Range between 0 to "))
guess_com(h)
