import Piece
IntToPieceAbreviation = {
    
    2: "B",
    4: "K",
    6: "Q",
    1: "P",
    5: "R",
    3: "N",

    10: "b",
    12: "k",
    14: "q",
    9: "p",
    13: "r",
    11: "n",
    
    0: " "
   

}
alphabet = [" ", "a","b","c","d","e","f","g","h"]
def PrintBoard(board):
    """Prints the board provided in a relatively neat way."""
    def PrintLine(Arr, UseConvert=True):
        for i in range(len(Arr)):
            print("  |  ",end="")
            try:
                if i != 0 and i != (9):
                    print(IntToPieceAbreviation[Arr[i]],end="")
                    
                else:
                    print(Arr[i],end="")
            except:
                print(Arr[i],end="")
        print()
    
    def PrintSeperator():
        print("-" * 100, end="")
        print()
    PrintSeperator()
    for i in range(len(board)):
        
        PrintLine([ i] + board[i])
        PrintSeperator()
    PrintSeperator()
    PrintLine(alphabet)
    PrintSeperator()
    
def AccessPointAt(board,x,y):
    return board[y][x]

class Vector2:
    x = 0
    y = 0
    def __init__(self,x,y):
        self.x = x
        self.y = y