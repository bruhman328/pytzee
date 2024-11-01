"""
   File:        burger.py
   Author:      Nahom Kassaye
   Date:        10/25/2024
   Section:     14
   E-mail:      nahomk1@umbc.edu
   Description:
    Will play Yahtzee

"""

"""

    num rolls
    points = 0
    chance_box = 0
    pytzee counter = 0
    num to pick(can only pick a number once)
    if number of times it shows up 3 or 4 times <--- three or four of a long
        add up all the numbers in the roll
    if number of times it shows up 3 times and theres a pair of numbers <-- full house
        ask user if they want to use full house
        if they do, add 25 points
    if 4 in a row( 1 2 3 4 or 2 3 4 5 or 3 4 5 6)  <-- small straight
        give 30 points
    if 5 in a row( 1 2 3 4 5  or 2 3 4 5 6)  <-- large straight
        give 40 points
    if user selects pytzee and all dice are the same and pytzee counter == 0
        give 50 points
        pytzee counter += 1
    if user selects pytzee and all dice are the same and pytzee counter > 1
        give 100 points 
    if user selects chance <---- chance
        add sum of all dice rolls into chance box
    if user selects count num <--- count
        picked num * number of times it shows up
    if points >= 63
        add 35 points
    if user selects skip <--- skip
        add 0 points
        
"""


import random

TOTAL_DICE = 5
DICE_FACES = 6
COUNT = 'count'
FULL_HOUSE = 'full house'
THREE_KIND = 'three of a kind'
FOUR_KIND = 'four of a kind'
SM_STRAIGHT = 'small straight'
LRG_STRAIGHT = 'large straight'
PYTZEE = 'pytzee'
CHANCE = 'chance'
SKIP = 'skip'

"""
you can use sum()
"""

def roll_dice():
    """
    :return: a list containing five integers representing dice rolls between 1 and 6.
    """
    roll_list = []
    for i in range(TOTAL_DICE):
        roll_list.append(random.randint(1, 6))
    return roll_list



def get_num(num, set):
    num_count = 0
    for i in set:
        if i == num:
            num_count += 1
    return num_count

def your_selection():
    roll_dice()
    game_select = input('How would you like to count this dice roll? ')
    if game_select == COUNT:
        num_select = int(input('What number do you want to count for? '))
        for i in roll_dice()
    elif game_select == THREE_KIND:
        three_counter = 0
        for i in roll_dice():
            three_counter += i
        return three_counter
    elif game_select == FOUR_KIND:
        four_counter = 0
        for i in roll_dice():
            four_counter += i
        return four_counter
    elif game_select == FULL_HOUSE:
        return 25
    elif game_select == SM_STRAIGHT:
        return 30
    elif game_select == LRG_STRAIGHT:
        return 40
    elif game_select == PYTZEE:
        return 50
    elif game_select == CHANCE:
        chance_counter = 0
        for i in roll_dice():
            chance_counter += i
        return chance_counter
    elif game_select == SKIP:
        return 0

    


def scorecard():
    print('Three of a Kind  Four of a Kind  Full House  Small Straight  Large Straight  Yahtzee  Chance')
    print()

    

        


def play_game(num_rounds):
    for i in range(1, num_rounds + 1):
        print(f'***** Beginning Round {i} *****')


        



if __name__ == '__main__':
    points = 0
    chance_box = 0
    pytzee_counter = 0

    num_rounds = int(input('What is the number of rounds that you want to play? '))
    seed = int(input('Enter the seed or 0 to use a random seed: '))
    if seed:
        random.seed(seed)
    play_game(num_rounds)

