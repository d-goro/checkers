# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 11:07:24 2019

@author: DGorocho
"""

from board import Board


def convert_to_move(line):
    return list(map(int, line.split(',')))    

def make_move(board, move):
    x = (move[0], move[1])
    y = (move[2], move[3])    
    board.perform_move(x, y)


def main(movesFile):
    b = Board()
    
    try:
        with open(movesFile) as f:
            for line in f:
                #print('Move:', line)
                make_move(b, convert_to_move(line.rstrip('\n')))
                
        print('Game result:', b.define_result())
    except Exception as e:
        print('Problem to run a game:', e)
    
    
    print(b)
    print('')
    print('printing for old console:')
    print('')
    #use this method if your consle doesn't support ANSI symbols
    b.print_state()

    
if __name__ == '__main__':
    import sys
    main(sys.argv[1])    