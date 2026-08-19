class Player:
    def __init__(self, username):
        if len(username)<3:
            raise ValueError("Username must contain at least 3 characters")
        self.__username=username
    def get_username(self):
        return self.__username
    def rename(self, new_username):
        if len(new_username)<3:
            raise ValueError("Username must contain at least 3 characters")
        self.__username=new_username
