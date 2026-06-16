class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def get_area(self) -> float:
        """Возвращает площадь прямоугольника."""
        return self.width * self.height

    def scale(self, factor: float) -> None:
        """Умножает стороны прямоугольника на factor."""
        self.width *= factor
        self.height *= factor

    def is_square(self) -> bool:
        """Проверяет, является ли прямоугольник квадратом."""
        return self.width == self.height


rect = Rectangle(4.5, 4.5)      # это квадрат
print(rect.get_area())          # 20.25
print(rect.is_square())         # True

rect.scale(2.0)                 # увеличиваем стороны в 2 раза
print(rect.width)               # 9.0
print(rect.height)              # 9.0
print(rect.get_area())          # 81.0