from abc import*
class Riddle:
    def __init__(self,riddle_id: int,question: str,correct_answer: str,difficulty: str,category: str) -> None:
        self.__id=riddle_id
        self.__question=question
        self.__correct_answer=correct_answer
        self.__difficulty=difficulty
        self.__category=category
    @abstractmethod
    def display(self):
        raise  NotImplementedError
    def check_answer(self, answer):
        return answer.lower() == self.__correct_answer.lower()
    @abstractmethod
    def get_type(self):
        pass
    def to_dict(self):
        pass
    @property
    def question(self):
        return self.__question
    @property
    def correct_answer(self):
        return self.__correct_answer
    @property
    def id(self):
        return self.__id
    @property
    def category(self):
        return self.__category
    
class MultipleChoiceRiddle(Riddle):
    def __init__(self, riddle_id, question, correct_answer, difficulty, category,possible_answers):
        super().__init__(riddle_id, question, correct_answer, difficulty, category)
        self.__possible_answers=possible_answers
    def display(self):
        print(self.question)
        number = 1
        for answer in self.get_possible_answers():
            print(f"{number}. {answer}")
            number += 1
    def check_answer(self, answer):
        if answer in self.get_possible_answers():
            return answer.lower()==self.correct_answer.lower()
        try:
            number=int(answer)
            answer=self.get_possible_answers()[number-1]
        except ValueError:
            return False

        return answer.lower()==self.correct_answer.lower()
    def get_possible_answers(self):
        return list(self.__possible_answers)

class FourAnswerRiddle(MultipleChoiceRiddle):
    def __init__(self, riddle_id, question, correct_answer, difficulty, category, possible_answers):
        super().__init__(riddle_id, question, correct_answer, difficulty, category, possible_answers)
    def get_type(self):
        return "multiple_4"

class TwoAnswerRiddle(MultipleChoiceRiddle):
    def __init__(self, riddle_id, question, correct_answer, difficulty, category, possible_answers):
        super().__init__(riddle_id, question, correct_answer, difficulty, category, possible_answers)
    def get_type(self):
            return "multiple_2"

class OpenRiddle(Riddle):
    def __init__(self, riddle_id, question, correct_answer, difficulty, category):
        super().__init__(riddle_id, question, correct_answer, difficulty, category)
    def display(self):
        print(self.question)
    def get_type(self):
        return "open"

    
