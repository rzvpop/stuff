class Board():
    def __init__(self, x, y):
        self.__dim_x = x
        self.__dim_y = y
        self.__pos_list = [] #[square, mark]