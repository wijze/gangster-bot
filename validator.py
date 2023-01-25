#this file uses python library named re for pattern recognition
import re

# import move generator
import genMoves as moveGenerator

# function to check if input string is in valid chess move format
def checkStringFormat(toCheck):
    # compile regex pattern
    move_pattern = r'^([Oo0](-[Oo0]){1,2}|[KQRBN]?[a-h]?[1-8]?x?[a-h][1-8](\=[QRBN])?[+#]?(\s(1-0|0-1|1\/2-1\/2))?)$'
    move_regex = re.compile(move_pattern)
    # return boolean indicating if string matches pattern
    return re.search(move_regex, toCheck)

# function to parse input string and return move object
def parse_input_string(string):
    # compile regex pattern to find squares in string
    fields_regex = re.compile(r'[a-h][1-8]')
    # find the squares (from and to)
    fields = re.findall(fields_regex, string)
    # check if input string contains two squares
    if len(fields) == 2:
        # create move object with from and to positions
        move = {
            "fromX": convertField(fields[0])[0],
            "fromY": convertField(fields[0])[1],
            "toX": convertField(fields[1])[0],
            "toY": convertField(fields[1])[1]
        }
        # check if input string contains promotion
        promotions = re.findall(r'[QRBN]', string)
        if promotions:
            # if string contains only one promotion character, check if it's a valid promotion
            if len(promotions) == 1:
                promotion = promotions[0]
                if promotion in ['Q','R','B','N']:
                    move["promotion"] = promotion
                else:
                    return False
            # if string contains two promotion characters, check if the second one is a valid promotion
            elif len(promotions) == 2:
                promotion = promotions[1]
                if promotion in ['Q','R','B','N']:
                    move["promotion"] = promotion
                else:
                    return False
        return move
    else:
        return False

# function to convert field from algebraic notation to array indices
def convertField(field):
    x = ord(field[0]) - 97
    y = int(field[1]) - 1
    return [x, y]

# main function to validate move
def validateMove(string, game):
    is_move = checkStringFormat(string)
    if not is_move: return False
    played_move = parse_input_string(string)
    if not played_move: return False
    legal_moves = moveGenerator.genMoves(game.board, False, game.white_to_play)
    for move in legal_moves:
        if moveGenerator.compareMoves(move, played_move):
            return move
    return False
