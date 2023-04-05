import chess

def getpieces(board):
    returnMap = []

    for y in range(8):
        returnMap.append([])
        for x in range(8):
            returnMap[y].append(str(board.piece_at(chess.square(x,7-y))))
    
    return returnMap

# boardRep = getpieces(chess.Board())
# for y in range(8):
#     string = ""
#     for x in range(8):
#         string+= boardRep[y][x]
#     print(string)