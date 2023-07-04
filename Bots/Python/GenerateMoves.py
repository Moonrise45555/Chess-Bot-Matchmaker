import Piece
import Move
from copy import deepcopy
def GenerateKnightMoves(Board):
    Knights = []
    Moves = []
    retMoves = []
    for Y in range(8):
        for X in range(8):
            if Board[Y][X] == Piece.Knight or Board[X][Y] == Piece.ColorSwitch(Piece.Knight):
                Knights.append([str(Y),str(X)])
    for i in Knights:
        StartPos = i[0] + i[1]
        StartPosInt = [int(i) for i in StartPos]
        Moves.append(StartPos + str(StartPosInt[0 ] + 2) +str(StartPosInt[1] + 1) )
        Moves.append(StartPos + str(StartPosInt[0] + 1) +str(StartPosInt[1] + 2) )
        if StartPosInt[1] != 0:
            Moves.append(StartPos + str(StartPosInt[0]+2 ) +str(StartPosInt[1]-1) )
        if StartPosInt[0] != 0:    
            Moves.append(StartPos + str(StartPosInt[0]-1) +str(StartPosInt[1]+2) )
        if StartPosInt[1] > 1 :
            Moves.append(StartPos + str(StartPosInt[0]+1) +str(StartPosInt[1]-2) )
        if StartPosInt[1] != 0 and StartPosInt[0] > 1:
            Moves.append(StartPos + str(StartPosInt[0]-2) +str(StartPosInt[1]-1) )
        if StartPosInt[0] != 0 and StartPosInt[1] > 1:
            Moves.append(StartPos + str(StartPosInt[0]-1) +str(StartPosInt[1]-2) )
        if StartPosInt[0] > 1 :
            Moves.append(StartPos + str(StartPosInt[0]-2) +str(StartPosInt[1]+1) )
    print(Moves)
    Moves = [Move.Move(i) for i in Moves]
    retMoves = [i for i in Moves if Move.IsLegalMove(i)]
    return retMoves
            


        
                    
