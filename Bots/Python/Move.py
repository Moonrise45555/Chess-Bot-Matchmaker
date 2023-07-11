def Info():
    """Numerical notation, Standard notation, arrayed Numerical"""



class Move:
    MoveString = ""
   
    def __init__(self,moveString):
        """moveString works with numerical notation"""
        self.MoveString = moveString
NotationDec = {
    0:"a",
    1:"b",
    2:"c",
    3:"d",
    4:"e",
    5:"f",
    6:"g",
    7:"h"
}
DecNotation = {
    "a":0,
    "b":1,
    "c":2,
    "d":3,
    "e":4,
    "f":5,
    "g":6,
    "h":7
     
}
def DecimalToNotation(Move):
    """Converts standalone Numerical notation to Standard notation"""
    Move = str(Move)
    newMove = ""
    newMove = NotationDec[int(Move[0])]
    newMove = newMove + Move[1]
    newMove = newMove  + NotationDec[int(Move[2])]
    newMove = newMove + Move[3]
    return newMove
def NotationToDecimal(Move):
    """converts standalone Numerical notation to standard notation"""
    Move = str(Move)
    newMove = ""
    newMove = str(DecNotation[Move[0]])
    newMove = newMove + Move[1]
    newMove = newMove + str(DecNotation[Move[2]])
    newMove = newMove + Move[3]
    return newMove




def MakeMove(mov,Board):
    """Makes the move shown. Doesnt check if its a legal or possible move. Works only with Numerical Notation in a move class."""
    
    Moving = Board[int(mov.MoveString[1])][int(mov.MoveString[0])]
    Board[int(mov.MoveString[1])][int(mov.MoveString[0])] = 0
    Board[int(mov.MoveString[3])][int(mov.MoveString[2])] = Moving
    return True

def GetColor(tile,Board):
    """Returns the color of the tile. 8=black 4=nothing 0=white. compatible with Standalone numerical and arrayed numerical."""
    if Board[int(tile[1])][int(tile[0])] > 7:
        return 8
    else:
        if Board[int(tile[1])][int(tile[0])] == 0:
            return 4
        return 0
    
def IsLegalMove(mov,Board, Based = 0):
    """checks if the function is outside the board at some point, and if it moves onto the own colour.
    Based is currently not recommended to use. Works with move classes and arrayed numerical. 
    """

    #Exists for compatibility with old code, numerical
    if type(mov) == Move:
        for i in mov.MoveString:
            if int(i) > (7 + Based) or int(i) < (0 + Based):
                return False
        if GetColor([str(int(x) - Based) for x in mov.MoveString[0:2]],Board) == GetColor([str(int(x) - Based) for x in mov.MoveString[2:4]],Board):
            return False
        return True
    
    #Works for arrayed numerical
    if type(mov) == type([]):

        for i in mov:
            if int(i) > (7 + Based) or int(i) < (0 + Based):
                return False

            if GetColor([str(int(x) - Based) for x in mov[0:2]],Board) == GetColor([str(int(x) - Based) for x in mov[2:4]],Board):
                return False
        return True



    
   


    