'''
Created on Feb 1, 2018

@author: catad
'''
'''
from move.move import Move
from move.move import Validate
from board.board import Play


class MoveControl:
    def __init__(self, game, validator):
        
        self._game = game
        self._validator = validator
        
    def placeMove(self, move):
        try:
            self._validator.validate(move)
            self._game.move(move)
            
        except Exception as e:
            print(e) 
            
    '''
                            
        