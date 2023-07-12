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






def DecimalToNotation(Move):
    """Converts standalone Numerical notation to Standard notation"""
    Move = str(Move)
    newMove = ""
    newMove = NotationDec[int(Move[0])]
    newMove = newMove + Move[1]
    newMove = newMove  + NotationDec[int(Move[2])]
    newMove = newMove + Move[3]
    return newMove
def NotationToDecimal(Move):
    """converts standalone Numerical notation to standard notation"""
    Move = str(Move)
    newMove = ""
    newMove = str(DecNotation[Move[0]])
    newMove = newMove + Move[1]
    newMove = newMove + str(DecNotation[Move[2]])
    newMove = newMove + Move[3]
    return newMove
def ArrayedNumericalToNumerical(arr):
    """Converts Arrayed numerical to Standalone Numerical."""
    x = ""
    for i in arr:
        x = x + str(i)
    return x