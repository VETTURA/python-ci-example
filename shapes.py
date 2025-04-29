"""
Модуль для работы с геометрическими фигурами: прямоугольник, квадрат и круг.
Предоставляет методы для вычисления площади, периметра и сравнения фигур.
"""

import math


class Shape:
    """Базовый класс для всех геометрических фигур."""

    def get_area(self):
        """
        Вычисляет площадь фигуры.

        Returns:
            float: Площадь фигуры.

        Raises:
            NotImplementedError: Метод должен быть переопределен в дочернем классе.
        """
        raise NotImplementedError("Метод get_area должен быть переопределен в дочернем классе.")

    def get_perimeter(self):
        """
        Вычисляет периметр фигуры.

        Returns:
            float: Периметр фигуры.

        Raises:
            NotImplementedError: Метод должен быть переопределен в дочернем классе.
        """
        raise NotImplementedError("Метод get_perimeter должен быть переопределен в дочернем классе.")

    def __str__(self):
        """
        Возвращает строковое представление фигуры.

        Returns:
            str: Строка с описанием фигуры.

        Raises:
            NotImplementedError: Метод должен быть переопределен в дочернем классе.
        """
        raise NotImplementedError("Метод __str__ должен быть переопределен в дочернем классе.")


class Rectangle(Shape):
    """Класс прямоугольника."""

    def __init__(self, width, height):
        """
        Инициализация прямоугольника.

        Args:
            width (float): Ширина прямоугольника.
            height (float): Высота прямоугольника.

        Raises:
            ValueError: Если ширина или высота не положительные.
        """
        if width <= 0 or height <= 0:
            raise ValueError("Ширина и высота должны быть положительными числами.")
        self.__width = width
        self.__height = height

    def get_area(self):
        """Возвращает площадь прямоугольника."""
        return self.__width * self.__height

    def get_perimeter(self):
        """Возвращает периметр прямоугольника."""
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Возвращает строковое представление прямоугольника."""
        return f"Rectangle(width={self.__width}, height={self.__height})"


class Square(Rectangle):
    """Класс квадрата, наследуется от Rectangle."""

    def __init__(self, side):
        """
        Инициализация квадрата.

        Args:
            side (float): Сторона квадрата.

        Raises:
            ValueError: Если сторона не положительное число.
        """
        super().__init__(side, side)

    def __str__(self):
        """Возвращает строковое представление квадрата."""
        # Доступ к защищенному атрибуту родителя через _Rectangle__width
        return f"Square(side={self._Rectangle__width})"


class Circle(Shape):
    """Класс окружности."""

    def __init__(self, radius):
        """
        Инициализация окружности.

        Args:
            radius (float): Радиус окружности.

        Raises:
            ValueError: Если радиус не положительное число.
        """
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом.")
        self.__radius = radius

    def get_area(self):
        """Возвращает площадь круга."""
        return math.pi * self.__radius ** 2

    def get_perimeter(self):
        """Возвращает длину окружности."""
        return 2 * math.pi * self.__radius

    def __str__(self):
        """Возвращает строковое представление круга."""
        return f"Circle(radius={self.__radius})"


class GeometryUtility:
    """Утилитарный класс для сравнения фигур."""

    @staticmethod
    def compare_area(shape1, shape2):
        """
        Сравнивает площади двух фигур.

        Args:
            shape1 (Shape): Первая фигура.
            shape2 (Shape): Вторая фигура.

        Returns:
            bool: True, если площади равны, иначе False.
        """
        return shape1.get_area() == shape2.get_area()

    @staticmethod
    def compare_perimeter(shape1, shape2):
        """
        Сравнивает периметры двух фигур.

        Args:
            shape1 (Shape): Первая фигура.
            shape2 (Shape): Вторая фигура.

        Returns:
            bool: True, если периметры равны, иначе False.
        """
        return shape1.get_perimeter() == shape2.get_perimeter()


if __name__ == "__main__":
    r1 = Rectangle(3, 5)
    s1 = Square(4)
    c1 = Circle(3)

    print(r1)
    print(f"Площадь r1: {r1.get_area()}")
    print(f"Периметр r1: {r1.get_perimeter()}")

    print(s1)
    print(f"Площадь s1: {s1.get_area()}")
    print(f"Периметр s1: {s1.get_perimeter()}")

    print(c1)
    print(f"Площадь c1: {c1.get_area()}")
    print(f"Периметр c1: {c1.get_perimeter()}")

    print("Равны ли площади r1 и s1?", GeometryUtility.compare_area(r1, s1))
    print("Равны ли периметры r1 и s1?", GeometryUtility.compare_perimeter(r1, s1))
