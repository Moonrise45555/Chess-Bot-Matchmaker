import Piece
import Move
from BoardMod import Vector2
from BoardMod import AccessPointAt
from Move import GetColor
from copy import deepcopy
from Conversions import ArrayedNumericalToNumerical
def GenerateAllMoves(Board, Side):
    return GenerateKnightMoves(Board, Side) + GenerateKingMoves(Board, Side) + GenerateStraightMoves(Board,Side) + GenerateDiagonalMoves(Board,Side)


def FindAll(piece, Board):
    """Takes in a Piece int and returns an array of Vector2 containing all positions of instances of this piece."""
    pie = []
    for Y in range(8):
        for X in range(8):
            if (Board[Y][X] == piece):
                pie.append(Vector2(X,Y))
    return pie

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
        if Move.IsLegalMove(i,Board):
            retMoves.append(i)

    return [Move.Move(ArrayedNumericalToNumerical(x)) for x in retMoves]
    


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
        if Move.IsLegalMove(i,Board):
            retMoves.append(i)

    return [Move.Move(ArrayedNumericalToNumerical(x)) for x in retMoves]

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
            
            if GetColor([i ,K.y],Board)  == GetColor([K.x ,K.y],Board):
                break

            Moves.append(StartPos + [(i)] + [(StartPos[1])] )
            #negative X
        for i in range( 1 ,  7):
            if K.x - i > 7 or K.x - i < 0:
                break
            
            if GetColor([ K.x - i ,K.y],Board)  == GetColor([K.x ,K.y],Board):
                break

            Moves.append(StartPos + [(K.x - i)] + [(StartPos[1])] )
            #positive Y
        for i in range(K.y + 1 , K.y + 7):
            if i > 7 or i < 0:
                break
            
            if GetColor([K.x ,i],Board)  == GetColor([K.x ,K.y],Board):
                break

            Moves.append(StartPos + [(StartPos[0])] + [(i)] )
        #negative X
        for i in range( 1 ,  7):
            if K.y - i > 7 or K.y - i < 0:
                break
            
            if GetColor([ K.x  ,K.y- i ],Board)  == GetColor([K.x ,K.y],Board):
                break

            Moves.append(StartPos + [StartPos[0]] + [(K.y - i )] )
        


        
    for i in Moves:
        if Move.IsLegalMove(i,Board):
            retMoves.append(i)

    return [Move.Move(ArrayedNumericalToNumerical(x)) for x in retMoves]
    


def GenerateDiagonalMoves(Board,Side):

    Pieces = []
    Moves = []
    Pieces = FindAll(Piece.Bishop + Side, Board) + FindAll(Piece.Queen + Side,Board)
    retMoves = []
   

    for K in Pieces:
        #Gathers all possible moves in every direction. very same-y
        StartPos = [K.x] + [K.y]
        #positive X
        for i in range(1 ,7):
            if i + K.x > 7 or i + K.x < 0 or i + K.y > 7 or K.y + i < 0:
                break
            
            if GetColor([i + K.x ,K.y + i],Board)  == GetColor([K.x ,K.y],Board):
                break

            Moves.append(StartPos + [(K.x + i)] + [(K.y + i)] )
            #negative X
        for i in range(1 ,7):
            if  K.x - i > 7 or  K.x - i < 0 or K.y - i > 7 or K.y - i < 0:
                break
            
            if GetColor([K.x - i ,K.y - i],Board)  == GetColor([K.x ,K.y],Board):
                break

            Moves.append(StartPos + [(K.x - i)] + [(K.y - i)] )
        
        #Other

        for i in range(1 ,7):
            if  K.x - i > 7 or  K.x - i < 0 or i + K.y > 7 or K.y + i < 0:
                break
            
            if GetColor([K.x - i ,K.y + i],Board)  == GetColor([K.x ,K.y],Board):
                break

            Moves.append(StartPos + [(K.x - i)] + [(K.y + i)] )
            #negative X


        for i in range(1 ,7):
            if  K.x + i > 7 or  K.x + i < 0 or K.y - i > 7 or K.y - i < 0:
                break
            
            if GetColor([K.x + i ,K.y - i],Board)  == GetColor([K.x ,K.y],Board):
                break

            Moves.append(StartPos + [(K.x + i)] + [(K.y - i)] )

       



        
        


        
    for i in Moves:
        if Move.IsLegalMove(i,Board):
            retMoves.append(i)

    return [Move.Move(ArrayedNumericalToNumerical(x)) for x in retMoves]

def GeneratePawnMoves(Board,Side):

    Pawn = []
    Moves = []
    Pawn = FindAll(Piece.Pawn + Side, Board)
    retMoves = []
   

    for K in Pawn:
        StartPos = [K.x] + [K.y]
        YModifier = GetColor([K.x,K.y],Board)
        if  YModifier == 8:
            YModifier = -1
        if YModifier == 0:
            YModifier = 1

        #standard moving forward
        Moves.append(StartPos + [(StartPos[0] + 0)] + [(StartPos[1] + YModifier)] )
        

        
    for i in Moves:
        if Move.IsLegalMove(i,Board):
            retMoves.append(i)

    return [Move.Move(ArrayedNumericalToNumerical(x)) for x in retMoves]



        






        
                    
