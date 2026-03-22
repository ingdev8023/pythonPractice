""" Given an array of strings representing chess pieces you still have on the board, calculate the value of the pieces your opponent has captured.

In chess, you start with 16 pieces:

Piece	Abbreviation	Quantity	Value
Pawn	"P"	8	1
Rook	"R"	2	5
Knight	"N"	2	3
Bishop	"B"	2	3
Queen	"Q"	1	9
King	"K"	1	0
The given array will only contain the abbreviations above.
Any of the 16 pieces not included in the given array have been captured.
Return the total value of all captured pieces, unless...
If the King has been captured, return "Checkmate". """


def get_captured_value(pieces):
    pieces_dict = {
        'P':{'Quantity': 8, 'Value': 1},
        'R':{'Quantity': 2, 'Value': 5},
        'N':{'Quantity': 2, 'Value': 3},
        'B':{'Quantity': 2, 'Value': 3},
        'Q':{'Quantity': 1, 'Value': 9},
        'K':{'Quantity': 1, 'Value': 0}
        }
    if "K" not in pieces:
        return "Checkmate"
    
    total_value = 0

    for piece in pieces:
        if piece in pieces_dict:
            pieces_dict[piece]['Quantity'] -= 1
   
    for piece,value in pieces_dict.items():
        total_value += value['Quantity']*value['Value']
        
    return total_value 


print(get_captured_value(["N", "P", "P", "B", "P", "R", "Q", "P", "P", "P", "B"]))

print(get_captured_value(["P", "P", "P", "P", "P", "P", "R", "R", "N", "B", "Q", "K"]))

print(get_captured_value(["P", "P", "P", "P", "P", "R", "B", "K"]))

print(get_captured_value(["K", "P", "P", "N", "P", "P", "R", "P", "B", "P", "N", "B"]))

print(get_captured_value(["P", "Q", "N", "P", "P", "B", "K", "P", "R", "R", "P", "P", "B", "P"]))

print(get_captured_value(["P", "K"]))

print(get_captured_value(["N", "P", "P", "B", "K", "P", "Q", "N", "P", "P", "R", "R", "P", "P", "P", "B"]))




