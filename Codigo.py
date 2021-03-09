import random as rd 
from os import system
import time
user_move = input('Jogar o dado? (S/n)').upper()
def roll_the_dice(user_move):
    while True:
        if user_move == 'S':
            random_number = rd.randrange(1,7)
            print('O dado girou e girou e parou no numero:{}'.format(random_number))
            time.sleep(1)
            user_move = input('Jogar o dado novamente? (S/n)').upper()
            system('clear')
            continue
        elif user_move == 'N':
            print('Ok guardando o dado')
            break
        else:
            user_move = input('Jogar dado? (S/n)').upper()
roll_the_dice(user_move)
