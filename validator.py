#this file checks if a string is a contains a chess move using a regex library, see sources at the bottom of this file
#it tests a test string and prints true if the test string contains a chess move
#I have copied the pattern from https://8bitclassroom.com/2020/08/16/chess-in-regex/
#it seems to work

import re 

test_move = "b4"
pattern = r'([Oo0](-[Oo0]){1,2}|[KQRBN]?[a-h]?[1-8]?x?[a-h][1-8](\=[QRBN])?[+#]?(\s(1-0|0-1|1\/2-1\/2))?)'

print(bool(re.search(pattern, test_move)))

#https://8bitclassroom.com/2020/08/16/chess-in-regex/
#https://stackoverflow.com/questions/9012008/pythons-re-return-true-if-string-contains-regex-pattern
#https://www.ichess.net/blog/chess-notation/