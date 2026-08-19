from players import Player
from riddle_game import RiddleGame
from riddle_repository import RiddleRepository

def main():
    repository = RiddleRepository("riddles.json")
    riddles = repository.load_riddles()
    game = RiddleGame(riddles)
    game.start()



main()