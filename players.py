class Player:
    def __init__(self, username):
        self.__username=username
    def get_username(self):
        return self.__username
    def rename(self, new_username):
        self.__username=new_username
        