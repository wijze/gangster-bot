#this file uses python library named re for pattern recognition
import re
#checkStringFormat wants a string and wil return a true if it is in valid chess move format

move_pattern = r'^([Oo0](-[Oo0]){1,2}|[KQRBN]?[a-h]?[1-8]?x?[a-h][1-8](\=[QRBN])?[+#]?(\s(1-0|0-1|1\/2-1\/2))?)$'
move_regex = re.compile(move_pattern)

fields_regex = re.compile(r'[a-h][1-8]')

#I have copied the pattern from https://8bitclassroom.com/2020/08/16/chess-in-regex/
#it seems to work

#checkStringFormat("b4") returns true
#checkStringFormat("1") returns false
#checkStringFormat("Nbxc5") returns true
#checkStringFormat("b9") returns false

def checkStringFormat(toCheck):
  return bool(re.search(move_regex, toCheck))

def parce_inp_string(string):
  # find the squares (from and to)
  fields = re.findall(fields_regex, string)
  if(len(fields)==2):
    move = {
      "fromX": convertField(fields[0])[0],
      "fromY": convertField(fields[0])[1],
      "toX": convertField(fields[1])[0],
      "toY": convertField(fields[1])[1]
    }
  else: 
    print("please provide from field and to field, maybe later only to field for now both")
    return False
  return move

def convertField(field):
  # from [a-h][1-8] to [0-7][0-7]
  x = ord(field[0]) - 97
  y = int(field[1]) - 1
  return[x, y]

# print(ord("a") - 97), returns 0
# print(convertField("a8")), returns [0, 7]