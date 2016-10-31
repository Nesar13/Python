''' "I pledge my honor that I have abided by the Stevens Honor System." 


@author: Nesar Ahmed
Created on Apr 28, 2016
'''

class Board:
    """ a class for the connect 4 board
    """
    def __init__(self, width=7, height=6):
        """ the constructor for objects of type Board """
        self.width = width
        self.height = height
        w = self.width
        h = self.height
        z=[[' ']*w for row in range(h)]
        self.z = z

    def __repr__(self):
        """ this method returns a string representation
            for an object of type Board
        """
        h = self.height
        w = self.width
        s = ''   
        for row in range(0, h):
            s += '|'
            for col in range(0, w):
                s += self.z[row][col] + '|'
            s += '\n'
        s += (2*w+1) * '-'    
        s += '\n'
        for col in range(0, w):
            s += " " + str(col % 10)
        return s       

    def addMove(self, col, ox):
        '''adds an ox checker where ox is a variable 
        holding a string'''
        for row in range(self.height - 1, -1, -1):
            if self.z[row][col] == " ":
                self.z[row][col] = ox
                return

    def clear(self):
        '''method for clearing board'''
        for col in range(1, self.width):
            for row in range(1, self.height):
                self.z[row][col] = " "

    def setBoard( self, moveString ):
        """ takes in a string of columns and places
            alternating checkers in those columns,
            starting with 'X'
            For example, call b.setBoard('012345')
            to see 'X's and 'O's alternate on the
            bottom row, or b.setBoard('000000') to
            see them alternate in the left column.
            moveString must be a string of integers
        """
        nextCh = 'X'   # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'
    
    
    def allowsMove(self, c):
        '''method returns true if the calling Board object
        can allow a move into column c'''
        if self.z[0][c] != " " or c < 0 or c >= self.width:
            return False
        else:
            return True

    def isFull(self):
        '''checks if a column is full'''
        for row in range(0, self.height):
            for col in range(0, self.width):
                if self.z[row][col] == " ":
                    return False
        return True

    def delMove(self, c):
        '''opposite of addMove'''
        for row in range(0, self.height):
            if self.z[row][c] != " ":
                self.z[row][c] = " "
                break

    def winsFor(self, ox):
        '''returns true if the given checker has won
        the calling Board'''
        H = self.height
        W = self.width
        D = self.z
        # check for horizontal wins
        for row in range(0,H):
            for col in range(0,W-3):
                if D[row][col] == ox and D[row][col+1] == ox and D[row][col+2] == ox and D[row][col+3] == ox:
                    return True
        for col in range(0,W):
            for row in range(0,H-3):
                if D[row][col] == ox and D[row+1][col] == ox and D[row+2][col] == ox and D[row+3][col] == ox:
                    return True
        for col in range(0,W-3):
            for row in range(0,H-3):
                if D[row][col] == ox and D[row+1][col+1] == ox and D[row+2][col+2] == ox and D[row+3][col+3] == ox:
                    return True
        for col in range(0,W-3):
            for row in range(3,H):
                if D[row][col] == ox and D[row-1][col+1] == ox and D[row-2][col+2] == ox and D[row-3][col+3] == ox:
                    return True
        return False

    def hostGame(self):
        '''Allows  users to play a game in a loop'''
        print (self)
        while True:
            x_move = -1
            while(self.allowsMove(x_move) == False):
                x_move = input("X's choice: ")
            self.addMove(x_move, "X")
            print (self)
            if self.winsFor("X"):
                print ("X Wins!")
                break
            o_move = -1
            while(self.allowsMove(o_move) == False):
                o_move = input("O's choice: ")
            self.addMove(o_move, "O")
            print (self)
            if self.winsFor("O"):
                print ("O Wins!")
                break

def copyBoard(board):
    '''copies the current Board'''
    output = Board(board.width, board.height)
    for row in range(board.height):
        for col in range(board.width):
            output.z[row][col] = board.z[row][col]
    return output

def connectFour():
    '''for testing the game'''
    width = 7
    height = 6
    game = Board(width, height)
    game.hostGame()

 
if __name__ =='__main__':
    a=Board(7,6)

    
  
    
    