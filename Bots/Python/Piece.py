Pawn =  0b001
Bishop =0b010
Knight =0b011
King =  0b100
Rook =  0b101
Queen = 0b110
EnPassantPawn = 0b111
def ColorSwitch(Piece):
    """Switches the given piece between Black and white."""
    return Piece ^ 0b1000

def IsBetterFor(Arg,Eval,Side):
    """returns which evaluations is preferrable for the given side. returns it by giving an int."""
    if Side == 0:
           if Eval < Arg:
               return 0
           else:
                return 1
               
    else:
         if Eval > Arg:
               return 0
         else:
                return 1
           
