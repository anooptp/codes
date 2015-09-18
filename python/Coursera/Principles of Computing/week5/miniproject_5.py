# -*- coding: utf-8 -*-
"""
Created on Sun Jul 20 14:26:16 2014

@author: anooptp
"""
"""
Provided code for Word Wrangler game
"""

#import poc_wrangler_gui

class WordWrangler:
    """
    Game class for Word Wrangler
    """
    
    def __init__(self, word_list, remdup, intersect, mergesort, substrs):
        self._word_list = word_list
        self._subset_strings = []
        self._guessed_strings = []

        self._remove_duplicates = remdup
        self._intersect = intersect
        self._merge_sort = mergesort
        self._substrs = substrs

    def start_game(self, entered_word):
        """
        Start a new game of Word Wrangler
        """
        if entered_word not in self._word_list:
            print "Not a word"
            return
        
        strings = self._substrs(entered_word)
        sorted_strings = self._merge_sort(strings)
        all_strings = self._remove_duplicates(sorted_strings)
        self._subset_strings = self._intersect(self._word_list, all_strings)
        self._guessed_strings = []        
        for word in self._subset_strings:
            self._guessed_strings.append("*" * len(word))
        self.enter_guess(entered_word)           
        
    def enter_guess(self, guess):
        """
        Take an entered guess and update the game
        """        
        if ((guess in self._subset_strings) and 
            (guess not in self._guessed_strings)):
            guess_idx = self._subset_strings.index(guess)
            self._guessed_strings[guess_idx] = self._subset_strings[guess_idx]

    def peek(self, peek_index):
        """
        Exposed a word given in index into the list self._subset_strings
        """
        self.enter_guess(self._subset_strings[peek_index])
        
    def get_strings(self):
        """
        Return the list of strings for the GUI
        """
        return self._guessed_strings
    

def run_game(wrangler):
    """
    Start the game.
    """
    poc_wrangler_gui.run_gui(wrangler)
    
    

"""
Student code for Word Wrangler game
"""

#import urllib2
#import codeskulptor
#import poc_wrangler_provided as provided

codeskulptor.set_timeout(100)

WORDFILE = "assets_scrabble_words3.txt"

# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    new_list=[]
    for item in list1:
        if item not in new_list:
            new_list.append(item)
    return new_list

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    new_list = []
    for l1 in list1:
        if l1 in list2:
            new_list.append(l1)
            
    return new_list

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.

    This function can be iterative.
    """   
    new_list = []
    while list1 and list2:
        if list1[0] < list2[0]:
            new_list.append(list1[0])
            list1.pop(0)
        else:
            new_list.append(list2[0])
            list2.pop(0)
    new_list = new_list + list1 + list2
    return new_list


def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    if len(list1) <= 1:
        return list1
    
    half = len(list1)/2
    
    return merge(merge_sort(list1[:half]), merge_sort(list1[half:]))

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    if not word:
        return ['']
    
    list_gen = []
    
    for li_str in gen_all_strings(word[1:]):
        for index in range(len(li_str)+1):
            list_gen.append(li_str[:index] + word[0] + li_str[index:])
    return gen_all_strings(word[1:]) + list_gen


# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
#    url = codeskulptor.file2url(filename)
#    netfile = urllib2.urlopen(url)
#    
#    return [line[:-1] for line in netfile.readlines()]
    
    try:
        opened_file = open(filename)
    except IOError as e:
        print 'Your scrabble words file is missing.'
     
    return [word[:-1] for word in opened_file]
    

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
#run()

