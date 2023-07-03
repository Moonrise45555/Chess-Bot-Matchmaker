Board = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
StartPos = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
class Piece:
    Pawn =  0b001
    Bishop =0b010
    Knight =0b011
    King =  0b100
    Rook =  0b101
    Queen = 0b110
    def ColorSwitch(Piece):
        return Piece ^ 0b1000
class Move:
    whereFrom = ""
    whereTo = ""
    def __init__(self,wheref,wheret):
        self.whereFrom = wheref
        self.whereTo = wheret
def LoadFromFEN(FEN):
    global Board
    CurrentX = 0
    CurrentY = 0
    s = True
    for i in FEN:
        s = True
        if i == "P":
            Board[CurrentY][CurrentX] = Piece.Pawn
            print("placed white pawn at", CurrentX, " ", CurrentY)
        elif i == "B":
            Board[CurrentY][CurrentX] = Piece.Bishop
        elif i == "R":
            Board[CurrentY][CurrentX] = Piece.Rook
        elif i == "K":
            Board[CurrentY][CurrentX] = Piece.King
        elif i == "Q":
            Board[CurrentY][CurrentX] = Piece.Queen
        elif i == "N":
            Board[CurrentY][CurrentX] = Piece.Knight
        
        elif i == "p":
            Board[CurrentY][CurrentX] =  Piece.ColorSwitch(Piece.Pawn)
        elif i == "b":
            Board[CurrentY][CurrentX] =  Piece.ColorSwitch(Piece.Bishop)
        elif i == "r":
            Board[CurrentY][CurrentX] =  Piece.ColorSwitch(Piece.Rook)
        elif i == "k":
            Board[CurrentY][CurrentX] =  Piece.ColorSwitch(Piece.King)
        elif i == "q":
            Board[CurrentY][CurrentX] =  Piece.ColorSwitch(Piece.Queen)
        elif i == "n":
            Board[CurrentY][CurrentX] = Piece.ColorSwitch(Piece.Knight)

        elif i == "/":
            CurrentY += 1
            CurrentX = 0
            s = False


        else:
            CurrentX += int(i)
             

        if s:
            CurrentX += 1
       
        if CurrentY == 8:
            print("Loading FEN String failed.")
            return False
LoadFromFEN(StartPos)
for i in Board:
    print(i,"\n")
def MakeMove(mov,Board):
    temp = Board[int(mov.whereFrom[1])][int(mov.whereFrom[0])]
    Board[int(mov.whereFrom[1])][int(mov.whereFrom[0])] = 0
    Board[int(mov.whereTo[1])][int(mov.whereTo[0])] = temp
def GetPossibleMoves(board):
    for i in board:
        for j in i:
            pass
def PrintBoard(board):
    for i in board:
        print(i,"\n")
while True:
    k = input("enther sometime: ")
    MakeMove(Move(k[0:2],k[2:4]),Board)
    PrintBoard(Board)


