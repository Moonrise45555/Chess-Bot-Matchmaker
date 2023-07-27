
from copy import deepcopy
import Piece
IntToPieceAbreviation = {
    
    2: "B",
    4: "K",
    6: "Q",
    1: "P",
    5: "R",
    3: "N",

    10: "b",
    12: "k",
    14: "q",
    9: "p",
    13: "r",
    11: "n",
    
    0: " "
   

}
alphabet = [" ", "a","b","c","d","e","f","g","h"]
def PrintBoard(board):
    """Prints the board provided in a relatively neat way."""
    def PrintLine(Arr, UseConvert=True):
        for i in range(len(Arr)):
            print("  |  ",end="")
            try:
                if i != 0 and i != (9):
                    print(IntToPieceAbreviation[Arr[i]],end="")
                    
                else:
                    print(Arr[i],end="")
            except:
                print(Arr[i],end="")
        print()
    
    def PrintSeperator():
        print("-" * 100, end="")
        print()
    PrintSeperator()
    for i in range(len(board)):
        
        PrintLine([ i] + board[i])
        PrintSeperator()
    PrintSeperator()
    PrintLine(alphabet)
    PrintSeperator()
    
def AccessPointAt(board,Arg0,Arg1=[]):
    """Supports Vector2 and arrays."""
    if type(Arg0) == type(Vector2(0,0)):
        return board[Arg0.y][Arg0.x]

    return board[int(Arg1)][int(Arg0)]
def MakeMove(mov,Board):
    """Makes the move shown. Doesnt check if its a legal or possible move. Works only with Numerical Notation in a move class."""
    
    Moving = Board[int(mov.MoveString[1])][int(mov.MoveString[0])]
    Board[int(mov.MoveString[1])][int(mov.MoveString[0])] = 0
    Board[int(mov.MoveString[3])][int(mov.MoveString[2])] = Moving
    return True

def IsAtStartLane(Board, Position):
    """Takes in the position of a Pawn and returns whether that pawn is at its starting place. Accepts Vector2."""
    if AccessPointAt(Board,Position) == 1:
        if Position.y == 1:
            return True
        else:
            return False

    if AccessPointAt(Board, Position) == 9:
        if Position.y == 6:
            return True
        else:
            return False
    ValueError
class Vector2:
    x = 0
    y = 0
    def __init__(self,x,y):
        self.x = x
        self.y = y

def Info():
    """Numerical notation eg "1234", Standard notation eg d4d2, arrayed Numerical"""



class Move:
    MoveString = ""
   
    def __init__(self,moveString):
        """moveString works with numerical notation"""
        self.MoveString = moveString

def GetColor(tile,Board = ""):
    """Returns the color of the tile. 8=black 4=nothing 0=white. compatible with Vector2, Standalone numerical and arrayed numerical.
    if passed with a single int, it will return the color of the piece passed."""
    if type(tile) == type(1):
        if tile == 0:
            return 4
        if tile >= 8:
            return 8
        else:
            return 0
    if type(tile) == type(Vector2(0,0)):
        tile = [tile.x, tile.y]
    
    try:
        if Board[int(tile[1])][int(tile[0])] > 7:
            return 8
        else:
            if Board[int(tile[1])][int(tile[0])] == 0:
                return 4
            return 0
    except:
        return 4
    

def FindAll(piece, Board):
    """Takes in a Piece int and returns an array of Vector2 containing all positions of instances of this piece."""
    pie = []
    for Y in range(8):
        for X in range(8):
            if (Board[Y][X] == piece):
                from BoardMod import Vector2
                pie.append(Vector2(X,Y))
    return pie
def KingAlive(Board,Side):
    if FindAll(Piece.King + Side, Board) == []:
        return False
    return True
