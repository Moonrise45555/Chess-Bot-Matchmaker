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
    sleep(1)
    k =  "e4e4"
    Move.MakeMove(Move.Move(Conversions.NotationToDecimal(k)),Board)
    
    BoardMod.PrintBoard(Board)
    sleep(1)
    
    
    BoardMod.PrintBoard(Board)

    print(PE.EvaluatePosition(Board))
    sleep(0.3)



