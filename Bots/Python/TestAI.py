import FENLoad
import Piece
import Move
import GenerateMoves

Board = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
StartPos = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"

    

FENLoad.LoadFromFEN(StartPos, Board)




def PrintBoard(board):
    print("0[a ,b ,c ,d ,e ,f ,g ,h]")
    for i in range(len(Board)):
        print(i,end="")
        print(Board[i],"\n")
    print("0[a ,b ,c ,d ,e ,f ,g ,h]")
    
assert Move.NotationToDecimal("a1a2") == "0102", Move.NotationToDecimal("a1a2")

assert Move.DecimalToNotation("0123") == "a1c3"


while True:
    k = input("enther sometime: ")
    Move.MakeMove(Move.Move(Move.NotationToDecimal(k)),Board)
    PrintBoard(Board)
    for i in GenerateMoves.GenerateKnightMoves(Board):
        Move.MakeMove(i,Board) 
#Note to myself: large portions arent wowrking. the GenerateKnightMoves function isnt correctly moving into the x axis, and executing all moves in it Moves PAWNs???



