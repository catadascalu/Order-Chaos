'''
Created on Feb 1, 2018

@author: catad
'''



import random 


class Square:
    def __init__(self, row, column, value):
        self._row = row 
        self._column = column 
        self._value = value
        
    def getRow(self):
        return self._row
    
    def getCol(self):
        return self._column
    
    def getValue(self):
        return self._value
    
class Place:
    def __init__(self, row, column):
        self._row = row 
        self._column = column 
        
        
    def getRow(self):
        return self._row
    
    def getCol(self):
        return self._column
    
    
        
class Board:
    def __init__(self):
        self._board = [[0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0]]
        
    def getBoard(self):  
        return self._board
    def __str__(self):
        z = ""
        for row in self._board:
            for c in row:
                if c == 0:
                    z += "| __ |"
                if c == 1:
                    z += "| X  |"
                if c == -1:
                    z += "| O  |"
            z += "\n"
            
        return z
    
    
    def checkWinColumn(self):
        
        '''
        calculates sum  for each column and returns true if it finds 5 in a row
        input: the board as list of lists
        output: true or false
        
        '''
        
        for i in range (0, 6):
            b = self._board
            sum = b[0][i]+b[1][i]+b[2][i]+b[3][i]+b[4][i]
            sum_1 = b[1][i]+b[2][i]+b[3][i]+b[4][i]+b[5][i]
            
            
            if sum == 5 or sum == -5 or sum_1 == 5 or sum_1 == -5:
                return True
        return False    
    def checkWinRow(self):
        '''
        calculates sum  for each row and returns true if it finds 5 in a row
         input: the board as list of lists
        output: true or false
        
        '''
        for i in range(0, 6):
            b = self._board
            sum = b[i][0]+b[i][1]+b[i][2]+b[i][3]+b[i][4]
            sum_1 = b[i][1]+b[i][2]+b[i][3]+b[i][4]+b[i][5] 
            
            
            
            if sum == 5 or sum == -5 or sum_1 == 5 or sum_1 == -5:
                return True
        return False
    
    def checkWinDiagonal(self):
        
        '''
        calculates sum  for each diagonal and returns true if it finds 5 in a row
        input: the board as list of lists
        output: true or false
        
        '''
        s = 0
        s2 = 0
        b = self._board
        s = b[1][1]+b[2][2]+b[3][3]+b[4][4]+b[5][5]
        
        s2 = b[0][0]+b[2][2]+b[3][3]+b[4][4]+b[5][5]
        if s == 6 or s2 == -6 or s == -6 or s == 6:
            return True
        s = 0
        s2 = 0
        s = b[0][5]+b[1][4]+b[2][3]+b[3][2]+b[4][1]
        
        s2 = b[1][4]+b[2][3]+b[3][2]+b[4][1]+b[5][0]
                
        if s == 6 or s2 == -6 or s == -6 or s2 == 6:
            return True
        return False
                
            
    
    def checkWin(self):
        if self.checkWinColumn() == True or self.checkWinRow() == True or self.checkWinColumn() == True:
            return True
        return False
    
    def checkFull(self):
        if self.checkWin() == False:
            for i in self._board:
                if 0 in i:
                    return False
            return True
        return False
    
    
    def getValidMoves(self):
        validMoves = []
        board = self._board
        for i in range(0, 6):
            for j in range(0, 6):
                if board[i][j] == 0:
                    validMoves.append(Place(i, j))
        
        return validMoves
    
               
    def move(self, pos):
        if pos.getRow() not in [0, 1, 2, 3, 4, 5] or pos.getCol() not in [0, 1, 2, 3, 4, 5, 6]:
            raise Exception("Move outside the board")
        if self._board[pos.getRow()][pos.getCol()] != 0:
            raise Exception("Square taken")
        if pos.getValue() != 1 and pos.getValue() != -1:
            raise ValueError("Symbol not appropiate.")
        self._board[pos.getRow()][pos.getCol()] = pos.getValue()    
    
    

class Strategy:
    def __init__(self, board):
        self._board = board
        
    def checkWinningMoves(self):  
        for row in self._board.getBoard():
            s = 0
            print(type(row))
            for c in row:
                s = s+c 
            if s == 4 or s == -4:
                for i in range(0, 3):
                    if self._board.getBoard()[row][i]==self._board.getBoard()[row][i+1] and self._board.getBoard()[row][i+1] == self._board.getBoard()[row][i+2] and self._board.getBoard()[row][i+3] == self._board.getBoard()[row][i+4]:
                        return row, i
                        
        for j in range(0, 6):
            s = 0
            for i in range(0,6):
                s = s + self._board.getBoard()[i][j]
                
                if s == 4 or s == -4:
                    for k in range(0, 3):
                        if self._board.getBoard()[k][j] == self._board.getBoard()[k+1][j] and self._board.getBoard()[k+1][j] == self.board.getBoard()[k+2][j] and self.board.getBoard()[k+2][j] == self._board.getBoard()[k+3][j]:
                            return j, k 
                
    '''            
    def checkMostSurrounded(self):
        max = 0
        squareR = 0
        squareC = 0
        value = 0
        
        for j in range(1, 5):
            nr = 0
            if self._board[1][j] == 0:
                if self._board[1][j-1] != 0:
                    nr += 1
                if self._board[1][j+1] != 0:
                    nr += 1
                for i in range(j-1, )
                        
    '''   
                       
   
    def countSymbols(self):
        nrO = 0
        nrX = 0
        for row in self._board.getBoard():
            for c in row:
                if c == 1:
                    nrO += 1
                elif c == -1:
                    nrX += 1
                    
        if nrO >= nrX:
            return  1
        elif nrX > nrO:
            return -1
        
        
    def getValidMoves(self):
        validMoves = []
        board = self._board.getBoard()
        for i in range(0, 6):
            for j in range(0, 6):
                if board[i][j] == 0:
                    validMoves.append(Place(i, j))
        
        return validMoves
    
               
    
            
   
class Play:
    def __init__(self, strategy):
        self._board = Board()
        
        self._strategy = strategy
        
    def moveOrder(self):
        validMoves = self._board.getValidMoves()
        maxSymbol = self._strategy.countSymbols()
        if maxSymbol == 1 or maxSymbol == -1:
            pos = random.randint(0, len(validMoves)-1)
            place = validMoves[pos]
            row = place.getRow()
            column = place.getCol()
            symbol = maxSymbol
    
            move = Square(row, column, symbol)
        
            try:
                self._board.move(move)
                b = self._board
                return b
            except Exception as e:
                print(e)
             
        pos = random.randint(0, len(validMoves)-1)
        place = validMoves[pos]
        symbol = random.randint(0, 1)
        
        row = place.getRow()
        column = place.getCol()
    
        move = Square(row, column, symbol)
        
        try:
            self._board.move(move)
            b = self._board
            return b
        except Exception as e:
            print(e)
        
        
    def moveChaos(self, move):
        try:
            self._board.move(move)
            b = self._board
            return b
        except Exception as e :
            print(e)
        
    '''    
    def move(self, move):
        if self._turn %2 == 0:
            move = self.moveOrder()
            if move in self._strategy.getValidMoves():
                if move.getSymbol == 1:
                    self._board.getBoard()[move.getRow()][move.getColumn()] == 1
                elif move.getSymbol == -1:
                        self.board.getBoard()[move.getRow()][move.getColumn()] == -1
                        
                b = self._board.setBoard()
                return b 
                
        elif self._turn %2 != 0:
            move = self.moveChaos(move)
            if move in self._strategy.getValidMoves():
                if move.getSymbol == 1:
                    self._board.getBoard()[move.getRow()][move.getColumn()] == 1
                elif move.getSymbol == -1:
                    self.board.getBoard()[move.getRow()][move.getColumn()] == -1
            
                b = self._board.setBoard()
                return b 
                
        '''        



          
        
                    
        
        
