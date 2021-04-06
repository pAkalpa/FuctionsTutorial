import random
import time


def display_intro():
    print('''
    You are in the Kingdom of Dragons. In front of you, 
    you see two caves. In one cave, the dragon is friendly 
    and will share his treasure with you. The other dragon 
    is hungry and will eat you on sight.''')


def choose_cave():
    cave = ''
    while cave != '1' and cave != '2' and cave != '3' and cave != '4':
        print('Which cave will you go into? (1-4)')
        cave = str(input())
    return cave


def check_cave(chosen_cave):
    print('You approach the cave...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! ')
    print('He opens his jaws and...')
    time.sleep(2)
    friendlyCave = random.randint(1, 4)
    # print(friendlyCave)
    if chosen_cave == str(friendlyCave):
        print('Gives you his treasure!')
    else:
        print('Gobbles you down!')


def Main():
    play_again = ''
    while play_again != 'n':
        display_intro()
        cave_number = choose_cave()
        check_cave(cave_number)
        play_again = str(
            input('Do you want to play again? (y or n)\n')).lower()


Main()
