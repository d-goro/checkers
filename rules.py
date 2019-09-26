"""
Created on Wed Sep 25 14:57:24 2019

@author: DGorocho
"""

class Rules:

    def __init__(self, elm_acc):
        #elm_acc - access method to elemnt on board that has current state of checkers defined inside
        self.__elm_acc = elm_acc

    def is_valid(self, x, y, is_white):
        '''
        This method will run set of rules that should define if desired move can be performed        
        x - source of move. Tuple where i, j define place on board
        y - destination of move. Tuple where i, j define place on board
        is_white - defines if checker is white or black
        '''
        rules = [
            lambda: self.is_source_ok(x[0], x[1], is_white),
            lambda: self.is_dest_ok(y[0], y[1]),
            lambda: self.is_diagonal(x, y, is_white)
        ]
        
        return all(rule() for rule in rules)


    def is_source_ok(self, i, j, is_white):
        elm = self.__elm_acc(i,j)        
        return elm != 0 and (elm == 1 and is_white or elm == 2 and not is_white)


    def is_dest_ok(self, i, j):
        return self.__elm_acc(i,j) == 0


    def test_next_eat(self, i, j, is_white):
        if is_white:
            possible_moves = [(i+2, j+2), (i-2, j+2)]
        else:
            possible_moves = [(i+2, j-2), (i-2, j-2)]

        return any(self.test_eat_move((i, j), p, is_white) != -1 for p in possible_moves if self.__elm_acc(p[0], p[1]) != -1)


    def test_eat_move(self, x, y, is_white):
        '''
        check if move is 'eat move' and if it so - returns place of eaten checker, otherwise - 1
        '''        
        i1 = x[0]
        j1 = x[1]
        i2 = y[0]
        j2 = y[1]        
        if (abs(i2 - i1) == 2) and (abs(j2 - j1) == 2) and self.is_dest_ok(i2, j2):
            x_change = -1
            y_change = -1
            if i2 > i1:
                x_change = 1
            if j2 > j1:
                y_change = 1

            e1 = i1 + x_change
            e2 = j1 + y_change
            
            if (is_white and self.__elm_acc(e1, e2) == 2) or (not is_white and self.__elm_acc(e1, e2) == 1):
                # here we check that we have what to eat
                return  (e1, e2)
            else:                
                return -1
        else:
            return -1


    def is_diagonal(self, x, y, is_white):
        '''
        diagonal move means that indices on axis X and Y must have difference 1 between source and destination        
        '''
        i1 = x[0]
        j1 = x[1]
        i2 = y[0]
        j2 = y[1]        
        if i1 > i2 or i1 < i2:
            # check that side is right 
            if self.test_eat_move(x, y, is_white) != -1:                
                # eating - we need to check that there was what to eat
                return True
            elif (abs(i2 - i1) == 1) and (abs(j2 - j1) == 1):
                # common move
                return True
            
        return  False
