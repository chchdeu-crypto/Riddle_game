import time
from datetime import date
from resulsts import QuestionResult, GameResult

class RiddleGame:
    def __init__(self,player,riddles):
        self.__player=player
        self.__riddles=riddles
        self.__results=[]
    def start(self):
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