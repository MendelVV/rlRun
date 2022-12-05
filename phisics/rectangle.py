class Rectangle:

    def __init__(self, x, y, w, h):
        # x, y - центр
        self.x = x
        self.y = y
        # w, h - размеры
        self.w = w
        self.h = h

    def intersect(self, other):
        # проверка, что два прямоугольника пересекаются
        intr_x = abs(self.x - other.x) <= (self.w + other.w) / 2
        intr_y = abs(self.y - other.y) <= (self.h + other.h) / 2
        return intr_x and intr_y

    def __str__(self):
        return 'x='+str(self.x)+' y='+str(self.y)+' w='+str(self.w)+' h='+str(self.h)
