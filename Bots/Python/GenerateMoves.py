import Piece
import Move
from BoardMod import Vector2
from BoardMod import AccessPointAt
from copy import deepcopy
def GenerateAllMoves(Board):
    return GenerateKnightMoves(Board)


def FindAll(Piece, Board):
    """Takes in a Piece int and returns an array of Vector2 containing all positions of instances of this piece."""
    pie = []
    for Y in range(8):
        for X in range(8):
            if (Board[Y][X] == Piece.Knight) or (Board[Y][X] == Piece.ColorSwitch(Piece.Knight)):
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
    return [Move.Move(str()) for x in retMoves]
    


def GenerateKingMoves(Board,Side):
    #Works One-Based

    King = []
    Moves = []
    for Y in Board:
        for X in Y:
            if AccessPointAt(Board,X,Y) == (Piece.King + Side):
                King.append(Vector2(X,Y))
    #Gathers all Kings

    for K in King:
        StartPosString = str(K[0] + 1) + str(K[1] + 1)
        StartPosInt = [int(x) for x in StartPosString]
        Moves.Append(StartPosString + str(StartPosInt[0]  - 1) + str(StartPosInt[1] - 1))
        Moves.Append(StartPosString + str(StartPosInt[0]  + 1) + str(StartPosInt[1] - 1))
        Moves.Append(StartPosString + str(StartPosInt[0]) + str(StartPosInt[1]      - 1))
        Moves.Append(StartPosString + str(StartPosInt[0] ) +     str(StartPosInt[1] + 1))
        Moves.Append(StartPosString + str(StartPosInt[0]  - 1) +     str(StartPosInt[1]))
        Moves.Append(StartPosString + str(StartPosInt[0]  + 1) +     str(StartPosInt[1]))
        Moves.Append(StartPosString + str(StartPosInt[0]  + 1) + str(StartPosInt[1] + 1))
        Moves.Append(StartPosString + str(StartPosInt[0]  - 1) + str(StartPosInt[1] + 1))
    Moves = [Move.Move(i) for i in Moves]
    retMoves = []
    for i in Moves:
        if Move.IsLegalMove(i,Board):
            retMoves.append(i)





        






        
                    
