'''
Created on Feb 1, 2018

@author: catad
'''

from board.board import Board
from unittest import TestCase

class Test5(TestCase):
    
    def test_winRow(self):
        board = Board()
        board.getBoard()[0] = [1,1,1,1,1,0]
        b = board.checkWinRow()
        self.assertTrue(b, "Not true")
        
        
        board.getBoard()[0] = [0,1,1,1,1,1] 
        b = board.checkWinRow()
        self.assertTrue(b, "Not true")
        
       
        
        
    def test_winCol(self):
        board = Board()
        for i in range(0,5):
            board.getBoard()[i][0] = 1
        b = board.checkWinColumn()
        self.assertTrue(b, "Not true")
        
        for i in range(1, 6):
            board.getBoard()[i][0] = 1 
        b = board.checkWinColumn()
        self.assertTrue(b, "Not true")
        
        board = Board()
        for i in range(0,5):
            board.getBoard()[i][0] = -1
        b = board.checkWinColumn()
        self.assertTrue(b, "Not true")
        
        for i in range(1, 6):
            board.getBoard()[i][0] = -1 
        b = board.checkWinColumn()
        self.assertTrue(b, "Not true")
        
        
    def test_winDiagonal(self):
        board = Board()
        for i in range(0, 6):
            board.getBoard()[i][i] = 1
        b = board.checkWinDiagonal()
        self.assertTrue(b, "Not true")
        
        for i in range(0, 6):
            for j in range(0, 6):
                if i+j == 5:
                    board.getBoard()[i][j] = 1
        b = board.checkWinDiagonal()
        self.assertTrue(b, "Not true")
        
        
    