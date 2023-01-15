# controls every thing

#for chat
import chatbot

# chess
import chessGame as Game

running = True
playing = False

while running:
  if playing:
    move = chatbot.Ask(playing)
    game.playMove(move)
    game.AI_move()
  else:
    if chatbot.Ask(playing): 
      playing = True
      game = Game.Game()
    else: break

