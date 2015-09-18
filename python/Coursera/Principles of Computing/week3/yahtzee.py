# -*- coding: utf-8 -*-
"""
Created on Sun Jul 06 09:37:21 2014

@author: anooptp
"""

"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
#import codeskulptor
#codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand
    Returns an integer score 
    """
    if not hand:
        return 0
        
    max_score = []
    
    for item in set(hand):
        max_score.append(hand.count(item) * item)
    return max(max_score)


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value of the held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    scores = []
    dies_sides = [ind+1 for ind in range(num_die_sides)]
    
    all_seqences = gen_all_sequences(dies_sides, num_free_dice)
    
    for item in all_seqences:
        scores.append(score(held_dice + item))
    return float(sum(scores))/ len(scores)


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    all_holds = [()]
    for item in hand:
        for subset in all_holds:
            all_holds = all_holds + [tuple(subset) + (item, )]
    return set(all_holds)



def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    res = (0.0, ())
    curr_val = float('-inf')
    
    for item in gen_all_holds(hand):
        val = expected_value(item, num_die_sides, len(hand)-len(item))
        if val > curr_val:
            curr_val = val
            res = (curr_val, item)
    return res
        

def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    
    
run_example()


import poc_holds_testsuite
poc_holds_testsuite.run_suite(gen_all_holds)
                                       
    
