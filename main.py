from riddels import *
from players import Player
from riddle_game import RiddleGame

def main():
    player=Player("Chaim")
    riddles=[FourAnswerRiddle(1,"What is 5 + 7?","12","easy","math", ["10", "11", "12", "13"]),
        TwoAnswerRiddle(2,"Is Python a programming language?","yes","easy","science",["yes", "no"]),
        OpenRiddle(3,"What is the capital of France?","Paris","easy","geography")]
    game = RiddleGame(player, riddles)
    game.start()

main()
