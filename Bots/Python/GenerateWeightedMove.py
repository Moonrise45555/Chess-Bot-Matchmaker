import PositionEvaluation
import BoardMod
import GenerateMoves
from copy import *
import Conversions
import Piece
import math
#does not work
#also check is useless
def GenerateBestMove(Board,Side,Best=-131415 , OriginalSide=4, depth=2):
    if OriginalSide == 4:
        OriginalSide = Side
    print("depth: ", depth, "Best: ", Best,"OriginalSide: ", OriginalSide, "Side: ", Side)
    Board = deepcopy(Board)
    """Board is the board, side is the side, Best is 0, OriginalSide is Side"""
    """gathers all moves from the current position"""
    Moves = GenerateMoves.GenerateAllMoves(Board,Side)
    """sets BestMove to default to the first move. So when theres no move that improves the position, it just does the first move."""
    BestMove = Moves[0]
    """Sets the default BestMoveValue to the worst position possible for the given Side"""
    BestMoveValue = -math.inf if Side == 0 else math.inf
    if Best == -131415:
        Best = BestMoveValue
    for i in Moves:
        #goes through all moves in the current position
        #Makes that move on the board
        TestBoard = deepcopy(Board)
        BoardMod.MakeMove(i,Board)
        #makes them
        comparisonobject = GenerateBestMove(TestBoard, Piece.ColorSwitch(Side),BestMoveValue,OriginalSide, depth - 1)[1] if depth > 0 else PositionEvaluation.EvaluatePosition(Board)
        #looks if they are better than the best value
        # if yes, makes them the best option
        # or, the worst case scenario
        if Side == 0:
            if BestMoveValue < comparisonobject:
                BestMove = i
                BestMoveValue = comparisonobject
        else: 
            if BestMoveValue > comparisonobject:
                BestMove = i
                BestMoveValue = comparisonobject
        #Aplha beta pruning?
        if  Side != OriginalSide:
            if Piece.IsBetterFor(comparisonobject, Best, OriginalSide) == 1:
                return (BestMove,BestMoveValue)
    #8 = black 0 = white

    
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
