import PositionEvaluation
import BoardMod
import GenerateMoves
from copy import *
import Conversions
import Piece
import math

def GenerateBestMove(Board,Side, depth=2):

    Moves = GenerateMoves.GenerateAllMoves(Board,Side)
    BestMove = Moves[0]
    BestMoveValue = -math.inf if Side == 0 else math.inf
    for i in Moves:
        #goes through all moves in the current position
        TestBoard = deepcopy(Board)
        BoardMod.MakeMove(i,TestBoard)
        #makes them
        comparisonobject = GenerateBestMove(TestBoard, Piece.ColorSwitch(Side), depth - 1)[1] if depth > 0 else PositionEvaluation.EvaluatePosition(Board)
        #looks if they are better than the best value
        if Side == 0:
            if BestMoveValue < comparisonobject:
                BestMove = i
                BestMoveValue = comparisonobject
        else: 
            if BestMoveValue > comparisonobject:
                BestMove = i
                BestMoveValue = comparisonobject
    print(BestMoveValue)
    return (BestMove,BestMoveValue)

"""
def WorstCase(Board, Side):
    Side = Piece.ColorSwitch(Side)
    Moves = GenerateMoves.GenerateAllMoves(Board,Side)
    BestMove = Moves[0]
    BestMoveValue = PositionEvaluation.EvaluatePosition(Board)
    for i in Moves:
        TestBoard = deepcopy(Board)
        BoardMod.MakeMove(i,TestBoard)
        if Side == 0:
            if BestMoveValue < PositionEvaluation.EvaluatePosition(TestBoard):
                BestMove = i
                BestMoveValue = PositionEvaluation.EvaluatePosition(TestBoard)
        else: 
            if BestMoveValue > PositionEvaluation.EvaluatePosition(TestBoard):
                BestMove = i
                BestMoveValue = PositionEvaluation.EvaluatePosition(TestBoard)
    return BestMoveValue


"""
