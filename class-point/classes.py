class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        
# Через сеттер и геттер??
class Circle(Point):
    def __init__(self, x, y, r) -> None:
        super().__init__(x, y)
        self.radius = r
    
    def circle_len(self):
        return 2*3.1415*self.radius
    
    def circle_sq(self):
        return 3.1415*self.radius**2


class Triangle(Point):
    def __init__(self, x1, y1) -> None:
        super().__init__(x1, y1)
        self.x


class Square(Point):
    def 
    ...

