#this file uses python library named re for pattern recognition
import re
import random
#checkStringFormat wants a string and wil return a true if it is in valid chess move format

#I have copied the pattern from https://8bitclassroom.com/2020/08/16/chess-in-regex/
#it seems to work

#checkStringFormat("b4") returns true
#checkStringFormat("1") returns false
#checkStringFormat("Nbxc5") returns true
#checkStringFormat("b9") returns false
import re
import random

def checkStringFormat(toCheck):
  move_pattern = r'^([Oo0](-[Oo0]){1,2}|[KQRBN]?[a-h]?[1-8]?x?[a-h][1-8](\=[QRBN])?[+#]?(\s(1-0|0-1|1\/2-1\/2))?)$'
  move_regex = re.compile(move_pattern)
  return bool(re.search(move_regex, toCheck))

#https://8bitclassroom.com/2020/08/16/chess-in-regex/
#https://stackoverflow.com/questions/9012008/pythons-re-return-true-if-string-contains-regex-pattern
#https://www.ichess.net/blog/chess-notation/