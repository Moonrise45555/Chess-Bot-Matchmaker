Pawn =  0b001
Bishop =0b010
Knight =0b011
King =  0b100
Rook =  0b101
Queen = 0b110
def ColorSwitch(Piece):
    """Switches the given piece between Black and white."""
    return Piece ^ 0b1000