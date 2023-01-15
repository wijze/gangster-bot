# controls every thing

#for chat
import chatbot

# chess
import chessGame as Game

running = True
playing = False

while running:
  if playing:
    print("")
    game.board.Log(True)
    print("")
    move = chatbot.Ask(playing, game)
    if move:
      game.playMove(move)
      game.AI_move()
    else: break
  else:
    if chatbot.Ask(playing, None): 
      playing = True
      game = Game.Game()
    else: break

