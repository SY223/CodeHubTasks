"""Guess Game"""
import random

winning_num = random.randint(1, 10)
print('You are about to play a guess game..')
player = input('What\'s your name? ')
player = player.capitalize()
print(winning_num)

def gameGuess():
    trials = 3
    while trials != 0:
        guess = int(input(f'Enter our winning number {player}: '))
        if guess != winning_num:
            print('Its incorrect, try again..')
            trials -= 1 
            if trials < 1:
                print(f'You are out of trials {player}!')
                break
        else:
            print(f'You win {player}.')
            break           
gameGuess()






# #instruction | accept user guess
# print('You have three chances to play this game')
# print('You are to select today\'s winning number')
# while trials != 0: 
#     guess = int(input('Enter a number between 1 to 10: '))
#     if guess != winning_num:
#         trials -= 1
#         print('Your guess is wrong try again!')
#         guess = int(input('Enter another number between 1 to 10: '))
#         continue
#     else:
#         print('You win!')
#         break

# print('You are out of trials')