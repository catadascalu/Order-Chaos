'''
Created on Feb 1, 2018

@author: catad
'''




from board.board import *
'''
board = Board()
b = board.setBoard()
print(b)
move = Square(1, 2, 1)
s = Strategy(board)

validator = Validate(board)
game = Play(board, 0, s)
control = MoveControl(game, validator)

play = Play(board, 1, s)
print(play.moveChaos(move))
print(play.moveOrder)
'''


class UI:
    def __init__(self):
        self._play = Play(strategy)
    
    def StartUI(self):
        print(str(self._play._board))
        turn = 2
        if self._play._board.checkWin() == True:
            print("Computer wins!")
        if self._play._board.checkFull() == True:
            print("User wins.")
         
        while (not self._play._board.checkWin() and not self._play._board.checkFull()):
            
            if turn%2 == 0:
                
               
                self._play.moveOrder()
            else:
                row = int(input("row: "))
                column = int(input("column: "))
                value = str(input("symbol(X or O): "))
                if value == 'X':
                    symbol = 1
                elif value == 'O':
                    symbol = -1
                else:
                    symbol = -2
                
                move = Square(row, column, symbol)
                self._play.moveChaos(move)
                
            turn += 1
            print(str(self._play._board)) 
            
            
board = Board()
strategy = Strategy(board)     
play = UI()
play.StartUI()