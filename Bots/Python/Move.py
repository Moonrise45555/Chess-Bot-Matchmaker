def Info():
    """Numerical notation, Standard notation, arrayed Numerical"""



class Move:
    MoveString = ""
   
    def __init__(self,moveString):
        """moveString works with numerical notation"""
        self.MoveString = moveString






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
    
def IsLegalMove(mov,Board):
    """checks if the function is outside the board at some point, and if it moves onto the own colour.
    Based is currently not recommended to use. Works with move classes and arrayed numerical. 
    """

    #Exists for compatibility with old code, numerical
    if type(mov) == Move:
        for i in mov.MoveString:
            if int(i) > (7 ) or int(i) < (0 ):
                return False
        if GetColor([str(int(x) ) for x in mov.MoveString[0:2]],Board) == GetColor([str(int(x)) for x in mov.MoveString[2:4]],Board):
            return False
        return True
    
    #Works for arrayed numerical
    if type(mov) == type([]):

        for i in mov:
            if int(i) > (7 ) or int(i) < (0 ):
                return False

        if GetColor(mov[0:2],Board) == GetColor( mov[2:4],Board):
            return False
        return True



    
   


    