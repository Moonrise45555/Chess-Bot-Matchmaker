class Move:
    MoveString = ""
   
    def __init__(self,moveString):
        self.MoveString = moveString
NotationDec = {
    0:"a",
    1:"b",
    2:"c",
    3:"d",
    4:"e",
    5:"f",
    6:"g",
    7:"h"
}
DecNotation = {
    "a":0,
    "b":1,
    "c":2,
    "d":3,
    "e":4,
    "f":5,
    "g":6,
    "h":7
     
}

#look up the correct stuff and convert it
def DecimalToNotation(Move):
    Move = str(Move)
    newMove = ""
    newMove = NotationDec[int(Move[0])]
    newMove = newMove + Move[1]
    newMove = newMove  + NotationDec[int(Move[2])]
    newMove = newMove + Move[3]
    return newMove
def NotationToDecimal(Move):
    Move = str(Move)
    newMove = ""
    newMove = str(DecNotation[Move[0]])
    newMove = newMove + Move[1]
    newMove = newMove + str(DecNotation[Move[2]])
    newMove = newMove + Move[3]
    return newMove




def MakeMove(mov,Board):
    Moving = Board[int(mov.MoveString[1])][int(mov.MoveString[0])]
    Board[int(mov.MoveString[1])][int(mov.MoveString[0])] = 0
    Board[int(mov.MoveString[3])][int(mov.MoveString[2])] = Moving
    return True

def IsLegalMove(mov):
    print(mov.MoveString)
    for i in mov.MoveString:
        if int(i) > 7 or int(i) < 0:
            return False
    return True
    