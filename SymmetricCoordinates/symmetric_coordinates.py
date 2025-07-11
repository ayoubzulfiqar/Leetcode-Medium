class SymmetricCoordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_point(self):
        return (self.x, self.y)

    def reflect_x_axis(self):
        return (self.x, -self.y)

    def reflect_y_axis(self):
        return (-self.x, self.y)

    def reflect_origin(self):
        return (-self.x, -self.y)

    def reflect_line_y_equals_x(self):
        return (self.y, self.x)

    def reflect_line_y_equals_negative_x(self):
        return (-self.y, -self.x)

    def reflect_point(self, center_x, center_y):
        new_x = 2 * center_x - self.x
        new_y = 2 * center_y - self.y
        return (new_x, new_y)

    def reflect_vertical_line(self, line_x):
        new_x = 2 * line_x - self.x
        return (new_x, self.y)

    def reflect_horizontal_line(self, line_y):
        new_y = 2 * line_y - self.y
        return (self.x, new_y)

if __name__ == "__main__":
    p = SymmetricCoordinates(3, 4)
    print(f"Original point: {p.get_point()}")
    print(f"Reflected across x-axis: {p.reflect_x_axis()}")
    print(f"Reflected across y-axis: {p.reflect_y_axis()}")
    print(f"Reflected across origin: {p.reflect_origin()}")
    print(f"Reflected across y=x: {p.reflect_line_y_equals_x()}")
    print(f"Reflected across y=-x: {p.reflect_line_y_equals_negative_x()}")
    print(f"Reflected across point (1, 2): {p.reflect_point(1, 2)}")
    print(f"Reflected across vertical line x=5: {p.reflect_vertical_line(5)}")
    print(f"Reflected across horizontal line y=1: {p.reflect_horizontal_line(1)}")

    p2 = SymmetricCoordinates(-2, -5)
    print(f"\nOriginal point 2: {p2.get_point()}")
    print(f"Reflected across x-axis: {p2.reflect_x_axis()}")
    print(f"Reflected across origin: {p2.reflect_origin()}")
    print(f"Reflected across point (0,0): {p2.reflect_point(0, 0)}")
    print(f"Reflected across line y=x: {p2.reflect_line_y_equals_x()}")