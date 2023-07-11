import FENLoad
import Piece
import Move
import GenerateMoves
import BoardMod
import PositionEvaluation as PE

Board = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
StartPos = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"

    

FENLoad.LoadFromFEN(StartPos, Board)




    
assert Move.NotationToDecimal("a1a2") == "0102", Move.NotationToDecimal("a1a2")

assert Move.DecimalToNotation("0123") == "a1c3"


while True:
    k = input("enther sometime: ")
    Move.MakeMove(Move.Move(Move.NotationToDecimal(k)),Board)
    BoardMod.PrintBoard(Board)
    for i in GenerateMoves.GenerateKnightMoves(Board,8):
        Move.MakeMove(i,Board)
    print(PE.EvaluatePosition(Board)) 



