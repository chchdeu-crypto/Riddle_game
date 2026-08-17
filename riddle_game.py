class RiddleGame:
    def __init__(self, player, riddles):
        self.__player = player
        self.__riddles = riddles
        self.__results = []
    
    def start(self):
        print(f"---riddle game---\n\nWelcome {self.__player.get_username()}!")

        for riddle in self.__riddles:
            riddle.display()
            answer = input("Your answer: ")
            while not riddle.check_answer(answer):
                print("Incorrect. Try again.")
                answer = input("Your answer: ")
            print("Correct!")