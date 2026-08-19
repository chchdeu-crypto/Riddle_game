import time
from datetime import date
from resulsts import QuestionResult, GameResult
from players import Player

class RiddleGame:
    def __init__(self,riddles):
        self.__player=None
        self.__riddles=riddles
        self.__results=[]
    def start(self):
        username = input("Enter your username: ")
        self.__player = Player(username)
        print(f"---Riddle Game---\n\nWelcome {self.__player.get_username()}!")
        total_start = time.time()
        for riddle in self.__riddles:
            result = self.ask_riddle(riddle)
            self.__results.append(result)
        total_time=time.time() - total_start
        game_result =GameResult(self.__player.get_username(),date.today(),total_time,self.__results)
        self.print_summary(game_result)
        return game_result


    def ask_riddle(self, riddle):
        start_time = time.time()
        riddle.display()
        answer = input("Your answer: ")
        while not riddle.check_answer(answer):
            print("incorrect. Try again.")
            answer = input("your answer: ")
        time_taken = time.time()-start_time
        print(f"Correct!")
        print(f"Time: {time_taken:.2f} seconds\n")
        return QuestionResult(riddle.id,riddle.get_type(),riddle.category,time_taken)

    def print_summary(self, result):
        print("\n---Game Summary---")
        print(f"Player: {self.__player.get_username()}")
        print(f"Total riddles: {result.get_total_riddles()}")
        print(f"Total time: {result.get_total_time():.2f} seconds")
        print("Average time by type:")
        for riddle_type, average in result.average_time_by_type().items():
            print(f"{riddle_type}: {average} seconds")

        print("Average time by category:")
        for category, average in result.average_time_by_category().items():
            print(f"{category}: {average} seconds")