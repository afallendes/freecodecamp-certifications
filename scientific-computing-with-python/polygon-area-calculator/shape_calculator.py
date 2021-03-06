class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return 'Too big for picture.'
        return '\n'.join([self.width * '*' for _ in range(self.height)]) + '\n'

    def get_amount_inside(self, shape):
        if self.width < shape.width or self.height < shape.height:
            return 0
        min_width = (self.width // shape.width) *  shape.width
        min_height = (self.height // shape.height) *  shape.height
        return (min_width * min_height) // (shape.width * shape.height)

    def __repr__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        self.set_side(side)
    
    def set_height(self, side):
        self.set_side(side)

    def __repr__(self):
        return f'Square(side={self.width})'
