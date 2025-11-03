# Hidden Treasure
# Given a 2D array representing a map of the ocean floor that includes a hidden treasure, and an array with the coordinates ([row, column]) for the next dive of your treasure search, return "Empty", "Found", or "Recovered" using the following rules:

# The given 2D array will contain exactly one unrecovered treasure, which will occupy multiple cells.

# Each cell in the 2D array will contain one of the following values:

# "-": No treasure.
# "O": A part of the treasure that has not been found.
# "X": A part of the treasure that has already been found.
# If the dive location has no treasure, return "Empty".

# If the dive location finds treasure, but at least one other part of the treasure remains unfound, return "Found".

# If the dive location finds the last unfound part of the treasure, return "Recovered".

# For example, given:

# [
#   [ "-", "X"],
#   [ "-", "X"],
#   [ "-", "O"]
# ]
# And [2, 1] for the coordinates of the dive location, return "Recovered" because the dive found the last unfound part of the treasure.

def dive(map, coordinates):
    first_hunt = map[coordinates[0]][coordinates[1]]
    
    if first_hunt == "-":
        return "Empty"
    elif first_hunt == "O":
        total_unfound = sum(row.count("O") for row in map)
        if total_unfound == 1:
            return "Recovered"
        else:
            return "Found"
    elif first_hunt == "X":
        return "Found"

dive([[ "-", "X"], [ "-", "X"], [ "-", "O"]], [2, 1])
dive([[ "-", "X"], [ "-", "X"], [ "-", "O"]], [2, 0])
dive([[ "-", "X"], [ "-", "O"], [ "-", "O"]], [1, 1])
dive([[ "-", "-", "-"], [ "X", "O", "X"], [ "-", "-", "-"]], [1, 2])
dive([[ "-", "-", "-"], [ "-", "-", "-"], [ "O", "X", "X"]], [2, 0])