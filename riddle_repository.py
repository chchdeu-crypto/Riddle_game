import json
from riddels import FourAnswerRiddle, TwoAnswerRiddle, OpenRiddle

class RiddleRepository:
    def __init__(self, file_path):
        self.__file_path = file_path
    def load_riddles(self):
        with open(self.__file_path, "r") as file:
            data = json.load(file)
        riddles = []
        for riddle in data:
            if riddle["type"] == "multiple_4":
                riddles.append(FourAnswerRiddle(riddle["id"],riddle["question"],riddle["correct_answer"],riddle["difficulty"],riddle["category"],riddle["possible_answers"]))
            elif riddle["type"] == "multiple_2":
                riddles.append(TwoAnswerRiddle(riddle["id"],riddle["question"],riddle["correct_answer"],riddle["difficulty"],riddle["category"],riddle["possible_answers"]))
            elif riddle["type"] == "open":
                riddles.append(OpenRiddle(riddle["id"],riddle["question"],riddle["correct_answer"],riddle["difficulty"],riddle["category"]))
        return riddles
    