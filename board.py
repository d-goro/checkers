"""
Created on Wed Sep 25 11:21:24 2019

@author: DGorocho
"""
from rules import Rules

class Board:
    WHITE = 1
    BLACK = 2
    NONE = 0
    __currentMove = True # true if White, false otherwise

    def __init__(self):
        """
        Defines board game and its state
        """    
        #initiate board with starting position for black (2) and white (1) checkers
        self.__board = [[(j+i)%2 if j > 4 else self.BLACK if (j+i)%2 == 1 else self.NONE for i in range(8)] if j < 3 or j > 4 else [self.NONE]*8 for j in range(8)]
        self.__white = 12
        self.__black = 12
        
    
    def __repr__(self):
        return str(self.__board)

    def __str__(self):
        '''
        This method will return string representation of board and checkers in color
        Colors will be shown in any console that supports ANSI symbols (e.g. Spyder console or Cygwin on Windows and any console on Linux/Unix)
        \033[31m - red color
        \033[34m - blue color
        \033[47m - white background
        '''        
        return '\n'.join([str(line).strip('[]') for line in self.__board]).replace(',', ' ').replace('1', '\033[31m*').replace('2', '\033[34m*').replace('0', '\033[47m ')

    def __check_boundaries(self, i, j):
        return i >= 0 and i <= 7 and j >= 0 and j <= 7

    def print_state(self):
        '''
        prints simply without colors, for consoles that don't support ANSI symbold
        '''
        print('\n'.join([str(line).strip('[]') for line in self.__board]).replace(',', ' ').replace('1', '*').replace('2', '#').replace('0', ' '))        


    def elm(self, i, j):
        '''
        this method returns element from list of lists like in 2d matrix, according to the rules, where 0,0 is bottom right of the board
        '''        
        return -1 if not self.__check_boundaries(i, j) else self.__board[7 - j][7 - i]

    def is_elm(self, i, j):
        '''
         check that any element exist in specified index
        '''
        return self.__check_boundaries(i, j) and self.__board[7 - j][7 - i] != self.NONE

    def elm_set(self, i, j, val):
        '''
        this method sets element in list of lists like in 2d matrix, according to the rules, where 0,0 is bottom right of the board
        '''
        self.__board[7 - j][7 - i] = val


    def define_result(self):
        '''
        Defines game result according to checkers state
        '''
        blacks = sum([l.count(self.BLACK) for l in self.__board])
        whites = sum([l.count(self.WHITE) for l in self.__board])
        
        if blacks > 0 and whites > 0 and self.if_moves_are_possible():
            return 'Game is incomplete'
        elif whites > blacks:
            return 'first'
        elif whites < blacks:
            return 'second'
        else:
            return 'tie'

    def create_possible_dest_moves(self, x):
        '''
        creates possible destination moves for tested x - to check if game is finished
        '''
        return [(x[0], x[1] + 1), (x[0], x[1] - 1), (x[0] + 1, x[1] + 1), (x[0] - 1, x[1] - 1), (x[0] + 1, x[1]), (x[0] - 1, x[1])]

    
    def if_moves_are_possible(self):
        '''
        will test if any move is possible to decide if game is complete
        '''
        there_moves = False
        r = Rules(lambda i, j: self.elm(i, j))        
        for i in range(8):
            elms = [(i, j) for j in range(8) if self.is_elm(i, j)]
            if any(r.test_next_eat(e[0], e[1], self.elm(e[0], e[1])) for e in elms) or \
               any (r.is_valid(x, y, self.elm(x[0], x[1]) == self.WHITE) for x in elms for y in self.create_possible_dest_moves(x)):
                there_moves = True
                break
        return there_moves


    def perform_move(self, x, y):
        '''
        actually performs move
        '''
        print('White' if self.__currentMove else 'Black', " moves", x, "->", y)

        r = Rules(lambda i, j: self.elm(i, j))
        if not r.is_valid(x, y, self.__currentMove):
            raise Exception(str.format("Move {0} -> {1} is not valid!", x, y))
        
        current = self.WHITE if self.__currentMove else self.BLACK
        eaten = r.test_eat_move(x, y, self.__currentMove)
        self.elm_set(x[0], x[1], self.NONE) # checker moved
        self.elm_set(y[0], y[1], current) # checker arrived

        if eaten != -1:
            print(x, 'eats', eaten)
            self.elm_set(eaten[0], eaten[1], self.NONE) # checker eaten            
            if not r.test_next_eat(y[0], y[1], self.__currentMove):
                self.__currentMove = not self.__currentMove # next eat is impossible, so next move passes to opponent
        else:
            self.__currentMove = not self.__currentMove # it was common move, so next move  passes to opponent
        
      
        

        
