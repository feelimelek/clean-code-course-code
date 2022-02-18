class Point:
    def __init__(self, coordX, coordY):
        self.coordX = coordX
        self.coordY = coordY


class Rectangle:
    def __init__(self, first_point_top_left, width, height):
        self.first_point_top_left = first_point_top_left
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def points(self):
        end_point_x_axis = self.first_point_top_left.coordX + self.width
        end_point_y_axis = self.first_point_top_left.coordY + self.height
        print('First Point X-Axis (Top Left)): ' + str(self.top_left_vertice.coordX))
        print('First Point Y-Axis (Top Left)): ' + str(self.top_left_vertice.coordY))
        print('End Point X-Axis (Top Right)): ' + str(top_right))
        print('End Point Y-Axis (Bottom Left): ' + str(bottom_left))


def build_rectangle():
    center_point = Point(50, 100)
    rectangle = Rectangle(center_point, 90, 10)

    return rectangle


rectangle = build_rectangle()

print(my_rectangle.area())
rectangle.points()
