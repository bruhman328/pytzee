"""
   File:        pytzee.py
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
        add sum of all dice rolls
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
dices = [1, 2, 3, 4, 5, 6]
sm_straight_checker = {'combo1': [1, 2, 3, 4], 'combo2' : [2, 3, 4, 5], 'combo3' : [3, 4, 5, 6]}
lrg_straight_checker = {'combo1': [1, 2, 3, 4, 5], 'combo2' : [2, 3, 4, 5, 6]}
pytzee_checker = {'combo1' : [1, 1, 1, 1, 1], 'combo2' : [2, 2, 2, 2, 2], 'combo3' : [3, 3, 3, 3, 3], 'combo4' : [4, 4, 4, 4, 4], 'combo5' : [5, 5, 5, 5, 5], 'combo6' : [6, 6, 6, 6, 6]}


three_kind_checker = {'combo1' : [1, 1, 1, 2, 2], 'combo2' : [1, 1, 1, 3, 3], 'combo3' : [1, 1, 1, 4, 4], 'combo4' : [1, 1, 1, 5, 5], 'combo4' : [1, 1, 1, 6, 6], 
                      'combo5' : [2, 2, 2, 1, 1], 'combo6' : [2, 2, 2, 3, 3], 'combo7' : [2, 2, 2, 4, 4], 'combo8' : [2, 2, 2, 5, 5], 'combo9' : [2, 2, 2, 6, 6],
                      'combo10' : [3, 3, 3, 1, 1], 'combo11' : [3, 3, 3, 2, 2], 'combo12' : [3, 3, 3, 4, 4], 'combo13' : [3, 3, 3, 5, 5], 'combo14' : [3, 3, 3, 6, 6], 
                      'combo15' : [4, 4, 4, 1, 1], 'combo16' : [4, 4, 4, 2, 2], 'combo17' : [4, 4, 4, 3, 3], 'combo18' : [4, 4, 4, 5, 5], 'combo19' : [4, 4, 4, 6, 6], 
                      'combo20' : [5, 5, 5, 1, 1], 'combo21' : [5, 5, 5, 2, 2], 'combo22' : [5, 5, 5, 3, 3], 'combo23' : [5, 5, 5, 4, 4], 'combo24' : [5, 5, 5, 6, 6],
                      'combo25' : [6, 6, 6, 1, 1], 'combo26' : [6, 6, 6, 2, 2], 'combo27' : [6, 6, 6, 3, 3], 'combo28' : [6, 6, 6, 4, 4], 'combo29' : [6, 6, 6, 5, 5]}


four_kind_checker = {'combo1': [1, 1, 1, 1, 2], 'combo2': [1, 1, 1, 1, 3], 'combo3': [1, 1, 1, 1, 4],  'combo4': [1, 1, 1, 1, 5],  'combo5': [1, 1, 1, 1, 6],  
                     'combo6': [2, 2, 2, 2, 1],  'combo7': [2, 2, 2, 2, 3],  'combo8': [2, 2, 2, 2, 4],  'combo9': [2, 2, 2, 2, 5],  'combo10': [2, 2, 2, 2, 6], 
                     'combo11': [3, 3, 3, 3, 1], 'combo12': [3, 3, 3, 3, 2], 'combo13': [3, 3, 3, 3, 4], 'combo14': [3, 3, 3, 3, 5], 'combo15': [3, 3, 3, 3, 6], 
                     'combo16': [4, 4, 4, 4, 1], 'combo17': [4, 4, 4, 4, 2], 'combo18': [4, 4, 4, 4, 3], 'combo19': [4, 4, 4, 4, 5], 'combo20': [4, 4, 4, 4, 6], 
                     'combo21': [5, 5, 5, 5, 1],'combo22': [5, 5, 5, 5, 2], 'combo23': [5, 5, 5, 5, 3], 'combo24': [5, 5, 5, 5, 4], 'combo25': [5, 5, 5, 5, 6], 
                     'combo26': [6, 6, 6, 6, 1], 'combo27': [6, 6, 6, 6, 2], 'combo28': [6, 6, 6, 6, 3],'combo29': [6, 6, 6, 6, 4], 'combo30': [6, 6, 6, 6, 5]}


full_house_checker = {
    'combo1': [1, 1, 1, 2, 2],  
    'combo2': [3, 3, 3, 2, 2],  
    'combo3': [4, 4, 4, 5, 5],  
    'combo4': [2, 2, 2, 1, 1],  
    'combo5': [5, 5, 5, 6, 6],  
    'combo6': [6, 6, 6, 4, 4],  
    'combo7': [1, 1, 1, 3, 3],  
    'combo8': [2, 2, 2, 4, 4],  
    'combo9': [3, 3, 3, 5, 5],  
    'combo10': [4, 4, 4, 2, 2]
}



def roll_dice():
    """
    :return: a list containing five integers representing dice rolls between 1 and 6.
    """
    roll_list = []
    for i in range(TOTAL_DICE):
        roll_list.append(random.randint(1, 6))
    return roll_list

 
def is_selection(combo, dice):         # checks to see if a roll_dice() fits one of the combos for the selections
    for item in combo:
        if item not in dice:
            return False
    return True


def count_num(num, set):   # checks number of times a number is in a roll_dice()
    num_count = 0
    for i in set:
        if i == num:
            num_count += 1
    if num_count == 0:
        pass
    else:
        return num_count


def your_selection(selection, dice, dict, num_counter, selection_count, selection_tracker):  # will get in a selection(pytzee, chance, etc), dice(roll_dice()), dict(this is the number of times you counted a number), 
                                                                                            #selection_count( checks to see if you already chose a selection) and selection tracker(checks points for each selection)
    if selection not in selection_count and selection in selection_tracker.keys():
        if selection == COUNT:
            num_select = int(input('What number do you want to count for? '))
            if num_select in dict.keys():
                dict[num_select] += count_num(num_select, dice)
            num_counter.append(num_select)
            if num_select in num_counter:
                print('There was already a score in that slot')
                your_selection(selection, dice, dict, num_counter, selection_count, selection_tracker)
            else:
                return count_num(num_select, dice) * num_select
        elif selection == THREE_KIND:
            selection_count.append(selection)
            if is_selection(three_kind_checker["combo1"], dice) or is_selection(three_kind_checker["combo2"], dice) or is_selection(three_kind_checker["combo3"], dice) or \
            is_selection(three_kind_checker["combo4"], dice) or is_selection(three_kind_checker["combo5"], dice) or is_selection(three_kind_checker["combo6"], dice) or \
            is_selection(three_kind_checker["combo7"], dice) or is_selection(three_kind_checker["combo8"], dice) or is_selection(three_kind_checker["combo9"], dice) or \
            is_selection(three_kind_checker["combo10"], dice) or is_selection(three_kind_checker["combo11"], dice) or is_selection(three_kind_checker["combo12"], dice) or \
            is_selection(three_kind_checker["combo13"], dice) or is_selection(three_kind_checker["combo14"], dice) or is_selection(three_kind_checker["combo15"], dice) or \
            is_selection(three_kind_checker["combo16"], dice) or is_selection(three_kind_checker["combo17"], dice) or is_selection(three_kind_checker["combo18"], dice) or \
            is_selection(three_kind_checker["combo19"], dice) or is_selection(three_kind_checker["combo20"], dice) or is_selection(three_kind_checker["combo21"], dice) or \
            is_selection(three_kind_checker["combo22"], dice) or is_selection(three_kind_checker["combo23"], dice) or is_selection(three_kind_checker["combo24"], dice) or \
            is_selection(three_kind_checker["combo25"], dice) or is_selection(three_kind_checker["combo26"], dice) or is_selection(three_kind_checker["combo27"], dice) or \
            is_selection(three_kind_checker["combo28"], dice) or is_selection(three_kind_checker["combo29"], dice):
                return sum(dice)
            else:
                print('This is not a Three of a Kind')
                your_selection(selection, dice, dict, num_counter, selection_count, selection_tracker)
        elif selection == FOUR_KIND:
            selection_count.append(selection)
            if is_selection(four_kind_checker["combo1"], dice) or is_selection(four_kind_checker["combo2"], dice) or is_selection(four_kind_checker["combo3"], dice) or \
            is_selection(four_kind_checker["combo4"], dice) or is_selection(four_kind_checker["combo5"], dice) or is_selection(four_kind_checker["combo6"], dice) or \
            is_selection(four_kind_checker["combo7"], dice) or is_selection(four_kind_checker["combo8"], dice) or is_selection(four_kind_checker["combo9"], dice) or \
            is_selection(four_kind_checker["combo10"], dice) or is_selection(four_kind_checker["combo11"], dice) or is_selection(four_kind_checker["combo12"], dice) or \
            is_selection(four_kind_checker["combo13"], dice) or is_selection(four_kind_checker["combo14"], dice) or is_selection(four_kind_checker["combo15"], dice) or \
            is_selection(four_kind_checker["combo16"], dice) or is_selection(four_kind_checker["combo17"], dice) or is_selection(four_kind_checker["combo18"], dice) or \
            is_selection(four_kind_checker["combo19"], dice) or is_selection(four_kind_checker["combo20"], dice) or is_selection(four_kind_checker["combo21"], dice) or \
            is_selection(four_kind_checker["combo22"], dice) or is_selection(four_kind_checker["combo23"], dice) or is_selection(four_kind_checker["combo24"], dice) or \
            is_selection(four_kind_checker["combo25"], dice) or is_selection(four_kind_checker["combo26"], dice) or is_selection(four_kind_checker["combo27"], dice) or \
            is_selection(four_kind_checker["combo28"], dice) or is_selection(four_kind_checker["combo29"], dice) or is_selection(four_kind_checker["combo30"], dice):
                return sum(dice)
            else:
                print('This is not a Four of a Kind')
                your_selection(selection, dice, dict, num_counter, selection_count, selection_tracker)
        elif selection == FULL_HOUSE:
            if is_selection(full_house_checker["combo1"], dice) or is_selection(full_house_checker["combo2"], dice) or is_selection(full_house_checker["combo3"], dice) or \
            is_selection(full_house_checker["combo4"], dice) or is_selection(full_house_checker["combo5"], dice) or is_selection(full_house_checker["combo6"], dice) or \
            is_selection(full_house_checker["combo7"], dice) or is_selection(full_house_checker["combo8"], dice) or is_selection(full_house_checker["combo9"], dice) or \
            is_selection(full_house_checker["combo10"]):
                house_input = input('Would you like to use full house? ')
                if house_input == 'yes':
                    selection_count.append(selection)
                    full_count += 1
                    return sum()
                elif house_input == 'no':
                    return 0
        elif selection == SM_STRAIGHT:
            selection_count.append(selection)
            if is_selection(sm_straight_checker["combo1"], dice) or is_selection(sm_straight_checker["combo2"], dice) or is_selection(sm_straight_checker["combo3"], dice):
                return sum(dice)
            else:
                print('This is not a Small Straight')
                your_selection(selection, dice, dict, num_counter, selection_count, selection_tracker)
            return 30
        elif selection == LRG_STRAIGHT:
            selection_count.append(selection)
            if is_selection(lrg_straight_checker["combo1"], dice) or is_selection(lrg_straight_checker["combo2"], dice):
                return sum(dice)
            else:
                print('This is not a Small Straight')
                your_selection(selection, dice, dict, num_counter, selection_count, selection_tracker)
        elif selection == PYTZEE:
            selection_count.append(selection)
            if is_selection(pytzee_checker["combo1"], dice) or is_selection(pytzee_checker["combo2"], dice) or is_selection(pytzee_checker["combo3"], dice) or \
            is_selection(pytzee_checker["combo4"], dice) or is_selection(pytzee_checker["combo5"], dice) or is_selection(pytzee_checker["combo6"], dice):
                return 50
            else:
                print('This is not a PYTZEE')
                your_selection(selection, dice, dict, num_counter, selection_count, selection_tracker)
        elif selection == CHANCE:
            selection_count.append(selection)
            return sum(dice)
    elif selection in selection_count and selection in selection_tracker.keys():
        print(f'You already used your {selection}')
        your_selection(selection, dice, dict, num_counter, selection_count, selection_tracker)
    elif selection not in selection_tracker.keys():
        your_selection(selection, dice, dict, num_counter, selection_count, selection_tracker)



        



def play_game(num_rounds):            # will give points based on your selection and number of rounds

    pytzee_counter = 0
    points = 0
    num_tracker = []
    selection_counter = []
    score_dict = {'Three of a Kind' : 0 , 'Four of a Kind' : 0, 'Full House' : 0, 'Small Straight' : 0, 'Large Straight' : 0, 'Yahtzee' : 0, 'Chance' : 0}
    num_count_dict = {1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0}
    for i in range(1, num_rounds + 1):
        print(f'***** Beginning Round {i} *****')
        print(f'Your score is {points}\n')
        dice_roll = roll_dice()
        print(f'You rolled: {dice_roll}')
        game_select = input('How would you like to count this dice roll? ')
        if game_select == COUNT:
            points += your_selection(game_select, dice_roll, num_count_dict, num_tracker, selection_counter, score_dict)
        elif game_select == THREE_KIND:
            score_dict['Three of a Kind'] += your_selection(game_select, dice_roll, num_count_dict, num_tracker, selection_counter, score_dict)
        elif game_select == FOUR_KIND:
            score_dict['Four of a Kind'] += your_selection(game_select, dice_roll, num_count_dict, num_tracker, selection_counter, score_dict)
        elif game_select == FULL_HOUSE:
            score_dict['Full House'] += your_selection(game_select, dice_roll, num_count_dict, num_tracker, selection_counter, score_dict)
        elif game_select == SM_STRAIGHT:
            score_dict['Small Straight'] += your_selection(game_select, dice_roll, num_count_dict, num_tracker, selection_counter, score_dict)
        elif game_select == LRG_STRAIGHT:
            score_dict['Large Straight'] += your_selection(game_select, dice_roll, num_count_dict, num_tracker, selection_counter, score_dict)
        elif game_select == PYTZEE and pytzee_counter == 0:
            score_dict['Yahtzee'] += your_selection(game_select, dice_roll, num_count_dict, num_tracker, selection_counter, score_dict)
            pytzee_counter += 1
        elif game_select == PYTZEE and pytzee_counter == 1:
            score_dict['Yahtzee'] += (your_selection(game_select, dice_roll, num_count_dict, num_tracker, selection_counter, score_dict) + 50)
        elif game_select == CHANCE:
            score_dict['Chance'] += your_selection(game_select, dice_roll, num_count_dict, num_tracker, selection_counter, score_dict)
        elif game_select == SKIP:
            points += 0
        elif game_select not in score_dict.keys():
            game_select = input('How would you like to count this dice roll? ')
        print(f'Your score is {points}\n', f'{num_count_dict}\n', score_dict)
    return 'Your final score is ', points
        
        


        


        



if __name__ == '__main__':
    points = 0
    chance_box = 0
    pytzee_counter = 0

    num_rounds = int(input('What is the number of rounds that you want to play? '))
    seed = int(input('Enter the seed or 0 to use a random seed: '))
    if seed:
        random.seed(seed)
    play_game(num_rounds)
