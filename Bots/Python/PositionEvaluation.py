PieceValues = {
    2: 3.3,
    4: 10000,
    6: 9,
    1: 1,
    5: 5,
    3: 3,

    10: -3.3,
    12: -10000,
    14: -9,
    9: -1,
    13: -5,
    11: -3,
    
    0:0
}
def EvaluatePosition(Board):
    Score = 0.0
    for i in Board:
        for j in i:
            Score += PieceValues[j]
    return round(Score, 2)
