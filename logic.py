class Ship:
    def __init__(self, length, tp=1, x=None, y=None):
        self.__length = length
        self.__tp = tp
        self.__x = x
        self.__y = y
        self.__is_move = True
        self.__cells = [1 for _ in range(self.__length)]

    def set_start_coords(self, x, y):
        self.__x = x
        self.__y = y

    def get_start_coords(self):
        return (self.__x, self.__y)

    def move(self, x, y):
        pass

    def is_collide(self):
        pass

    def __getitem__(self, item):
        return self.__cells[item]

    def __setitem__(self, key, value):
        self.__cells[key] = value


class GamePole:
    def __init__(self):
        self.__ships = []