import FENLoad
import Piece
import GenerateMoves
import BoardMod
import PositionEvaluation as PE
import Conversions
from GenerateWeightedMove import GenerateBestMove
from time import sleep

Board = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
StartPos = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
InterestingPos = "rnbqkbnr/8/8/pppppppp/2PPPP2/1P4P1/PR4RP/1NBQKBN1"
CheckPos = "rnbqk1nr/pppppppp/5b2/8/3K1R2/5N2/PPPPPPPP/RNBQ1B2"
DiagonalHorizontalPos = "5k1K/8/5p1p/6b1/5P1P/1p6/prP5/1P6"

    

FENLoad.LoadFromFEN(StartPos, Board)
BoardMod.PrintBoard(Board)



    
assert Conversions.NotationToDecimal("a1a2") == "0102", BoardMod.NotationToDecimal("a1a2")

assert Conversions.DecimalToNotation("0123") == "a1c3"

while True:
    import random
    BoardMod.MakeMove(BoardMod.Move(Conversions.NotationToDecimal(input("input a move: "))), Board)
    BoardMod.PrintBoard(Board)
    

 #   Move.MakeMove(GenerateBestMove(Board,8),Board)

    

    BoardMod.MakeMove(GenerateBestMove(Board,0)[0],Board)
    BoardMod.PrintBoard(Board)
    
    

    print(PE.EvaluatePosition(Board))



