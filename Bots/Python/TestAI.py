import FENLoad
import Piece
import Move
import GenerateMoves
import BoardMod
import PositionEvaluation as PE
import Conversions
from time import sleep

Board = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
StartPos = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"

    

FENLoad.LoadFromFEN(StartPos, Board)




    
assert Conversions.NotationToDecimal("a1a2") == "0102", Move.NotationToDecimal("a1a2")

assert Conversions.DecimalToNotation("0123") == "a1c3"


while True:
    k = input()
    Move.MakeMove(Move.Move(Conversions.NotationToDecimal(k)),Board)
    for i in GenerateMoves.GenerateKnightMoves(Board,8):
    
        Move.MakeMove(i,Board)
    for i in GenerateMoves.GenerateKingMoves(Board,0):
        Move.MakeMove(i,Board)
    for i in GenerateMoves.GenerateKnightMoves(Board,0):
    
        Move.MakeMove(i,Board)
    for i in GenerateMoves.GenerateKingMoves(Board,8):
        Move.MakeMove(i,Board)
    GenerateMoves.GenerateStraightMoves(Board,0)
    
    BoardMod.PrintBoard(Board)

    print(PE.EvaluatePosition(Board))
    sleep(0.3)



