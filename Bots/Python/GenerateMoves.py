import Piece
from BoardMod import *
import BoardMod
from copy import deepcopy
from Conversions import ArrayedNumericalToNumerical
def GenerateAllMoves(Board, Side ):
    LegalMoves = [x for x in GenerateAllPseudoLegalMoves(Board,Side) if FilterPseudoLegalMoves(x,Board)]
    return LegalMoves

   

def GenerateAllPseudoLegalMoves(Board,Side):
    pseudoLegalMoves = GenerateKnightMoves(Board, Side) + GenerateKingMoves(Board, Side) + GenerateStraightMoves(Board,Side) + GenerateDiagonalMoves(Board,Side) + GeneratePawnMoves(Board,Side)
    return pseudoLegalMoves

def IsLegalMove(mov,Board, CheckCheck=True):
    """checks if the function is outside the board at some point, and if it moves onto the own colour.
    Works with move classes and arrayed numerical. 
    """

    #Exists for compatibility with old code, numerical
    if type(mov) == Move:
        for i in mov.MoveString:
            if int(i) > (7 ) or int(i) < (0 ):
                return False
        if GetColor([str(int(x) ) for x in mov.MoveString[0:2]],Board) == GetColor([str(int(x)) for x in mov.MoveString[2:4]],Board):
            return False
    
    #Works for arrayed numerical
    if type(mov) == type([]):

        for i in mov:
            if int(i) > (7 ) or int(i) < (0 ):
                return False

        if GetColor(mov[0:2],Board) == GetColor( mov[2:4],Board):
            return False
        mov = Move(str(mov[0]) + str(mov[1]) + str(mov[2]) + str(mov[3]))

   
    return True

def FilterPseudoLegalMoves(mov,Board):
    MoveColor = GetColor(AccessPointAt(Board,int(mov.MoveString[0]),int(mov.MoveString[1])))
    """Takes in a move class and a board and checks if the move is actually legal or only pseudo-legal. True if legal, false is pseudo-legal"""
    Board = deepcopy(Board)

    MakeMove(mov,Board)
    for i in GenerateAllPseudoLegalMoves(Board,Piece.ColorSwitch(MoveColor)):
        TestBoard = deepcopy(Board) 
        MakeMove(i,TestBoard)
        #if the king isnt alive, meaning the last move was illegal because we were actually in check, return false
        if not KingAlive(TestBoard,MoveColor):
            return False
    return True


def GenerateKnightMoves(Board,Side):
    """Returns all possible knight  moves for the given side in Move classes."""
    Knights = []
    Moves = []
    retMoves = []
    Knights = FindAll(Piece.Knight + Side, Board)
    for i in Knights:
        StartPos = [i.x] + [i.y]
        Moves.append(StartPos + [(StartPos[0] + 2)] + [(StartPos[1] + 1)] )
        Moves.append(StartPos + [(StartPos[0] + 1)] + [(StartPos[1] + 2)] )
        Moves.append(StartPos + [(StartPos[0] + 2)] + [(StartPos[1] - 1)] )
        Moves.append(StartPos + [(StartPos[0] - 1)] + [(StartPos[1] + 2)] )
        Moves.append(StartPos + [(StartPos[0] + 1)] + [(StartPos[1] - 2)] )
        Moves.append(StartPos + [(StartPos[0] - 2)] + [(StartPos[1] - 1)] )
        Moves.append(StartPos + [(StartPos[0] - 1)] + [(StartPos[1] - 2)] )
        Moves.append(StartPos + [(StartPos[0] - 2)] + [(StartPos[1] + 1)] )
        
    for i in Moves:
        if IsLegalMove(i,Board):
            retMoves.append(i)

    return [BoardMod.Move(ArrayedNumericalToNumerical(x)) for x in retMoves]
    


def GenerateKingMoves(Board,Side):

    King = []
    Moves = []
    King = FindAll(Piece.King + Side, Board)
    retMoves = []
   

    for K in King:
        StartPos = [K.x] + [K.y]
        Moves.append(StartPos + [(StartPos[0] + 0)] + [(StartPos[1] + 1)] )
        Moves.append(StartPos + [(StartPos[0] + 1)] + [(StartPos[1] + 0)] )
        Moves.append(StartPos + [(StartPos[0] + 1)] + [(StartPos[1] - 1)] )
        Moves.append(StartPos + [(StartPos[0] + 1)] + [(StartPos[1] + 1)] )
        Moves.append(StartPos + [(StartPos[0] - 1)] + [(StartPos[1] - 0)] )
        Moves.append(StartPos + [(StartPos[0] - 1)] + [(StartPos[1] + 1)] )
        Moves.append(StartPos + [(StartPos[0] - 1)] + [(StartPos[1] - 1)] )
        Moves.append(StartPos + [(StartPos[0] + 0)] + [(StartPos[1] - 1)] )
        
    for i in Moves:
        if IsLegalMove(i,Board):
            retMoves.append(i)

    return [BoardMod.Move(ArrayedNumericalToNumerical(x)) for x in retMoves]

def GenerateStraightMoves(Board,Side):
    Pieces = []
    Moves = []
    Pieces = FindAll(Piece.Rook + Side, Board) + FindAll(Piece.Queen + Side,Board)
    retMoves = []
   

    for K in Pieces:
        #Gathers all possible moves in every direction. very same-y
        StartPos = [K.x] + [K.y]
        #positive X
        for i in range(K.x + 1 , K.x + 7):
            if i > 7 or i < 0:
                break
            
            if BoardMod.GetColor([i ,K.y],Board)  == BoardMod.GetColor([K.x ,K.y],Board):
                break
            if BoardMod.GetColor([i ,K.y],Board)  == Piece.ColorSwitch(BoardMod.GetColor([K.x ,K.y],Board)):
                Moves.append(StartPos + [(i)] + [(StartPos[1])] )
                break

            Moves.append(StartPos + [(i)] + [(StartPos[1])] )
            #negative X
        for i in range( 1 ,  7):
            if K.x - i > 7 or K.x - i < 0:
                break
            
            if BoardMod.GetColor([ K.x - i ,K.y],Board)  == BoardMod.GetColor([K.x ,K.y],Board):
                break

            if BoardMod.GetColor([ K.x - i ,K.y],Board)  == Piece.ColorSwitch( BoardMod.GetColor([K.x ,K.y],Board)):
                Moves.append(StartPos + [(K.x - i)] + [(StartPos[1])] )
                break

            Moves.append(StartPos + [(K.x - i)] + [(StartPos[1])] )
            #positive Y
        for i in range(K.y + 1 , K.y + 7):
            if i > 7 or i < 0:
                break
            
            if BoardMod.GetColor([K.x ,i],Board)  == BoardMod.GetColor([K.x ,K.y],Board):
                break

            if BoardMod.GetColor([K.x ,i],Board)  == Piece.ColorSwitch(BoardMod.GetColor([K.x ,K.y],Board)):
                Moves.append(StartPos + [(StartPos[0])] + [(i)] )
                break

            Moves.append(StartPos + [(StartPos[0])] + [(i)] )
        #negative X
        for i in range( 1 ,  7):
            #if it overflows, leave
            if K.y - i > 7 or K.y - i < 0:
                break
            #if it encounters a wrong color, leave
            if BoardMod.GetColor([ K.x  ,K.y- i ],Board)  == BoardMod.GetColor([K.x ,K.y],Board):
                break

            if BoardMod.GetColor([ K.x  ,K.y- i ],Board)  == Piece.ColorSwitch(BoardMod.GetColor([K.x ,K.y],Board)):
                Moves.append(StartPos + [StartPos[0]] + [(K.y - i )] )
                break

            Moves.append(StartPos + [StartPos[0]] + [(K.y - i )] )
        


        
    for i in Moves:
        if IsLegalMove(i,Board):
            retMoves.append(i)

    return [BoardMod.Move(ArrayedNumericalToNumerical(x)) for x in retMoves]
    


def GenerateDiagonalMoves(Board,Side):
    Pieces = []
    Moves = []
    Pieces = FindAll(Piece.Bishop + Side, Board) + FindAll(Piece.Queen + Side,Board)
    retMoves = []
   

    for K in Pieces:
        #Gathers all possible moves in every direction. very same-y
        StartPos = [K.x] + [K.y]
        for i in range(1 ,7):
            if i + K.x > 7 or i + K.x < 0 or i + K.y > 7 or K.y + i < 0:
                break
            
            if BoardMod.GetColor([i + K.x ,K.y + i],Board)  == BoardMod.GetColor([K.x ,K.y],Board):
                break

            if BoardMod.GetColor([i + K.x ,K.y + i],Board)  == Piece.ColorSwitch(BoardMod.GetColor([K.x ,K.y],Board)):
                Moves.append(StartPos + [(K.x + i)] + [(K.y + i)] )
                break

            Moves.append(StartPos + [(K.x + i)] + [(K.y + i)] )




            #negative X
        for i in range(1 ,7):
            if  K.x - i > 7 or  K.x - i < 0 or K.y - i > 7 or K.y - i < 0:
                break
            
            if BoardMod.GetColor([K.x - i ,K.y - i],Board)  == BoardMod.GetColor([K.x ,K.y],Board):
                break

            if BoardMod.GetColor([K.x - i ,K.y - i],Board)  == Piece.ColorSwitch(BoardMod.GetColor([K.x ,K.y],Board)):
                Moves.append(StartPos + [(K.x - i)] + [(K.y - i)] )
                break

            Moves.append(StartPos + [(K.x - i)] + [(K.y - i)] )
        
        #Other

        for i in range(1 ,7):
            if  K.x - i > 7 or  K.x - i < 0 or i + K.y > 7 or K.y + i < 0:
                break
            
            if BoardMod.GetColor([K.x - i ,K.y + i],Board)  == BoardMod.GetColor([K.x ,K.y],Board):
                break

            if BoardMod.GetColor([K.x - i ,K.y + i],Board)  == Piece.ColorSwitch(BoardMod.GetColor([K.x ,K.y],Board)):
                Moves.append(StartPos + [(K.x - i)] + [(K.y + i)] )
                break

            Moves.append(StartPos + [(K.x - i)] + [(K.y + i)] )
            #negative X


        for i in range(1 ,7):
            if  K.x + i > 7 or  K.x + i < 0 or K.y - i > 7 or K.y - i < 0:
                break
            
            if BoardMod.GetColor([K.x + i ,K.y - i],Board)  == BoardMod.GetColor([K.x ,K.y],Board):
                break
            if BoardMod.GetColor([K.x + i ,K.y - i],Board)  == Piece.ColorSwitch(BoardMod.GetColor([K.x ,K.y],Board)):
                Moves.append(StartPos + [(K.x + i)] + [(K.y - i)] )
                break

            Moves.append(StartPos + [(K.x + i)] + [(K.y - i)] )

       



        
        


        
    for i in Moves:
        if IsLegalMove(i,Board):
            retMoves.append(i)

    return [BoardMod.Move(ArrayedNumericalToNumerical(x)) for x in retMoves]

def GeneratePawnMoves(Board,Side):
    Pawn = []
    Moves = []
    Pawn = FindAll(Piece.Pawn + Side, Board)
    retMoves = []
   

    for K in Pawn:
        StartPos = [K.x] + [K.y]
        YModifier = BoardMod.GetColor([K.x,K.y],Board)
        if  YModifier == 8:
            YModifier = -1
        if YModifier == 0:
            YModifier = 1

        #standard moving forward
        if  BoardMod.AccessPointAt(Board,StartPos[0],StartPos[1] + YModifier) == 0:
            Moves.append(StartPos + [(StartPos[0] + 0)] + [(StartPos[1] + YModifier)] )
        #double moving forward
        if BoardMod.IsAtStartLane(Board, K) and BoardMod.AccessPointAt(Board,StartPos[0],StartPos[1] + YModifier) == 0 and BoardMod.AccessPointAt(Board,StartPos[0],StartPos[1] + YModifier * 2) == 0:
            Moves.append(StartPos + [(StartPos[0] + 0)] + [(StartPos[1] + YModifier * 2)] )
        #pawn taking

        if BoardMod.GetColor( [StartPos[0] - 1 , StartPos[1] + YModifier], Board ) == BoardMod.GetColor(Piece.ColorSwitch(BoardMod.AccessPointAt(Board,K))) :
            Moves.append(StartPos + [(StartPos[0] - 1)] + [(StartPos[1] + YModifier)])




        if BoardMod.GetColor([StartPos[0] + 1,StartPos[1] + YModifier], Board) == BoardMod.GetColor(Piece.ColorSwitch(BoardMod.AccessPointAt(Board,K))) :
            Moves.append(StartPos + [(StartPos[0] + 1)] + [(StartPos[1] + YModifier)])


            
        

        
    for i in Moves:
        if IsLegalMove(i,Board):
            retMoves.append(i)

    return [BoardMod.Move(ArrayedNumericalToNumerical(x)) for x in retMoves]



        






        
                    
