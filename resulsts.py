class QuestionResult:
    def __init__(self,riddle_id,riddle_type,category,time_taken):
        self.__riddle_id=riddle_id
        self.__riddle_type=riddle_type
        self.__category=category
        self.__time_taken=time_taken
    @property
    def riddle_type(self):
        return self.__riddle_type
    @property
    def category(self):
        return self.__category
    @property
    def time_taken(self):
        return self.__time_taken

class GameResult:
    def __init__(self,username,date,total_time,question_results):
        self.__username=username
        self.__date=date
        self.__total_time=total_time
        self.__question_results=question_results
    def get_total_riddles(self):
        return len(self.__question_results)

    def average_time_by_type(self):
        average = {}
        for question in self.__question_results:
            if question.riddle_type in average:
                average[question.riddle_type][0] += question.time_taken
                average[question.riddle_type][1] += 1
            else:
                average[question.riddle_type] = [question.time_taken, 1]
        for avg in average:
            average[avg] = f"{average[avg][0] / average[avg][1]:.2f}"
        return average

    def average_time_by_category(self) -> dict[str, float]:
        average = {}
        for question in self.__question_results:
            if question.category in average:
                average[question.category][0] += question.time_taken
                average[question.category][1] += 1
            else:
                average[question.category] = [question.time_taken, 1]
        for avg in average:
            average[avg] = f"{average[avg][0] / average[avg][1]:.2f}"
        return average
    def get_total_time(self):
        return self.__total_time
    def to_csv_row(self):
        return [self.__username,self.__date,self.__total_time,self.get_total_riddles()]
    




