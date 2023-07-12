import Piece
import Move
from BoardMod import Vector2
from BoardMod import AccessPointAt
from copy import deepcopy
from Conversions import ArrayedNumericalToNumerical
def GenerateAllMoves(Board, Side):
    return GenerateKnightMoves(Board, Side) + GenerateKingMoves(Board, Side)


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
        StartPos = [K.x] + [K.y]
        for i in range(K.x + 1, K.x + 7):
            print(i," ", K.y)
            if AccessPointAt(Board, i,  K.y) % 8  == AccessPointAt(Board,K.x,K.y) % 8:
                break

            Moves.append(StartPos + [(i)] + [(StartPos[1])] )
    print(Moves)
    return
        
    for i in Moves:
        if Move.IsLegalMove(i,Board):
            retMoves.append(i)

    return [Move.Move(ArrayedNumericalToNumerical(x)) for x in retMoves]





        






        
                    
