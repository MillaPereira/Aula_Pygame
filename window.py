class Window:
    __height = 0
    __width = 0
    __color = (0,0,0)

    def __init__(self, height, width, color):
        self.__height = height
        self.__width = width
        self.color = color

    def get_height(self):
        return self.__height

    def get_width(self):
        return self.__width

    def get_color(self):
        return self.__color

    def get_size(self):
        return (self.__height, self.__width)
    