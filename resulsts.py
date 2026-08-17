class QuestionResult:
    def __init__(self,riddle_id,riddle_type,category,time_taken):
        self.__riddle_id=riddle_id
        self.__riddle_type=riddle_type
        self.__category=category
        self__time_taken=time_taken

class GameResult:
    def __init__(self,username,date,totatl_time,question_results):
        self.__username=username
        self.__date=date
        self.__total_time=totatl_time
        self.__question_results=question_results
    def get_total_riddles(self):
        pass
    def average_time_by_type(self):
        pass
    def average_time_by_category(self):
        pass


