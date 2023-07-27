import Piece
def LoadFromFEN(FEN, Board):
    CurrentX = 0
    CurrentY = 7
    s = True
    for i in FEN:
        s = True
        #Goes through all pieces and places them
        if i == "P":
            Board[CurrentY][CurrentX] = Piece.Pawn
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
            #Slash indicates moving to the next row. S needs to be false, or else the lower increase of CurrentX will set it to 1 instead of 0
            CurrentY -= 1
            CurrentX = 0
            s = False


        else:
            #it must be a number, so the cursor is shifted right by it
            CurrentX += int(i)
            s = False
             
        
        if s:
            CurrentX += 1
       
        if CurrentY == -1:
            print("Loading FEN String failed.")
            return False