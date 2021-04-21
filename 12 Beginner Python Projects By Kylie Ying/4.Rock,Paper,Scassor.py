import random

def play():
    user = input("'r' of rock, 'p'for paper, 's' for scissors:- ").lower()
    com_in = random.choice(['r','p','s'])
    # print(com_in)

    if user == com_in:
        return 'tie'

    if winner(user,com_in):
        return 'You Win'
    
    return "you lose"


def winner(player,opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

# print(play())
play()