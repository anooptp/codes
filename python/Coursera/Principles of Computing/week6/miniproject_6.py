# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 17:34:05 2014

@author: anooptp
"""



"""
Mini-max Tic-Tac-Toe Player
"""

#import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
#import codeskulptor
#codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    if board.check_win() is not None:
        return SCORES[board.check_win()], (-1, -1)
    
    res = (-1, (-1, -1))
    
    for move in board.get_empty_squares():
        clone_board = board.clone()
        clone_board.move(move[0], move[1], player)
        score, _ = mm_move(clone_board, provided.switch_player(player)) 
        
        if score * SCORES[player] == 1:
            return score, move
        elif score * SCORES[player] > res[0]:
            res = (score, move)
        elif res[0] == -1:
            res = (res[0], move)
            
    return res[0] * SCORES[player], res[1]

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

provided.play_game(move_wrapper, 1, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)


#board = provided.TTTBoard(3, False, [[provided.PLAYERO, provided.PLAYERX, provided.PLAYERX], [provided.PLAYERO, provided.PLAYERX, provided.PLAYERO], [provided.PLAYERX, provided.PLAYERO, provided.PLAYERX]])
##self.assertIs(type(mm_move(board, PLAYERX)), tuple)
#score, move = mm_move(board, provided.PLAYERX)
##        self.assertIs(type(score), int)
##        self.assertIs(type(move), tuple)
#print mm_move(board, provided.PLAYERX)
##        self.assertEqual(mm_move(board, PLAYERX), (1, (-1, -1)))
#board = provided.TTTBoard(3, False, [[provided.PLAYERO, provided.PLAYERX, provided.PLAYERX], [provided.PLAYERX, provided.PLAYERO, provided.PLAYERO], [provided.PLAYERO, provided.PLAYERX, provided.PLAYERX]])
#print mm_move(board, provided.DRAW)
##        self.assertEqual(mm_move(board, DRAW), (0, (-1, -1)))
#board = provided.TTTBoard(3, False, [[provided.PLAYERO, provided.PLAYERX, provided.PLAYERX], [provided.PLAYERO, provided.PLAYERX, provided.PLAYERO], [provided.PLAYERO, provided.PLAYERO, provided.PLAYERX]])
#print mm_move(board, provided.PLAYERO)
##        self.assertEqual(mm_move(board, PLAYERO), (-1, (-1, -1)))
#
#board = provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO], [provided.PLAYERO, provided.PLAYERX, provided.PLAYERX], [provided.PLAYERO, provided.EMPTY, provided.PLAYERO]])
#print mm_move(board, provided.PLAYERX)
##        self.assertEqual(mm_move(board, PLAYERX), (1, (2, 1)))
#board = provided.TTTBoard(2, False, [[provided.EMPTY, provided.EMPTY], [provided.EMPTY, provided.EMPTY]])
#print mm_move(board, provided.PLAYERX)
##        self.assertEqual(mm_move(board, PLAYERX), (1, (0, 0)))
#
#
#board = provided.TTTBoard(3, False, [[provided.EMPTY, provided.EMPTY, provided.PLAYERX], [provided.EMPTY, provided.EMPTY, provided.EMPTY], [provided.EMPTY, provided.EMPTY, provided.EMPTY]])
#print mm_move(board, provided.PLAYERO)
##        self.assertEqual(mm_move(board, provided.PLAYERO), (0, (1, 1)))
#board = provided.TTTBoard(3, False, [[provided.PLAYERX, provided.EMPTY, provided.EMPTY], [provided.PLAYERO, provided.PLAYERO, provided.EMPTY], [provided.EMPTY, provided.PLAYERX, provided.EMPTY]])
#print mm_move(board, provided.PLAYERX)
##        self.assertEqual(mm_move(board, provided.PLAYERX), (0, (1, 2)))
#board = provided.TTTBoard(3, False, [[provided.EMPTY, provided.EMPTY, provided.PLAYERX], [provided.EMPTY, provided.EMPTY, provided.EMPTY], [provided.EMPTY, provided.EMPTY, provided.EMPTY]])
#print mm_move(board, provided.PLAYERO)
##        self.assertEqual(mm_move(board, provided.PLAYERO), (0, (1, 1)))  
