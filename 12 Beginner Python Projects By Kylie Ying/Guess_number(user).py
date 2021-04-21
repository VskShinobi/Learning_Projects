import random
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"guess a number between 1 to {x} :- "))
        if guess > random_number:
            print('sorry, Your guess is high')
        elif guess < random_number:
            print('sorry, Your guess is low')
    print(f'Your got the number "{random_number}" correctly')

h = int(input("Choose Your Range between 0 to "))
guess(h)
