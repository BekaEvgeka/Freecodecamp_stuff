class Rectangle:   
    def __init__(self, w, h):
        self.width = w
        self.height = h
    
    def set_width(self, w):
        self.width = w
    
    def set_height(self, h):
        self.height = h
    
    def get_area(self):
        self.area = self.width*self.height
        return self.area
    
    def get_perimeter(self):
        self.perimeter = 2 * (self.width +self.height)
        return self.perimeter
    
    def get_diagonal(self):
        self.diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
        return self.diagonal
    
    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture"
        h = self.height
        i = 0
        line = ""
        while i < h:
            line = line + ("*"* self.width) + "\n"
            i +=1
            
        return line
    
    def __str__(self) -> str:
        return "Rectangle(width={0}, height={1})".format(self.width, self.height)
    
    def get_amount_inside(self, shape):
        timesvert = self.height // shape.height
        timeshor = self.width // shape.width 
        return timeshor * timesvert
    

class Square(Rectangle):
    def __init__(self, w, h = 0):
        super().__init__(w, h)
        self.height = w
        self.width = w
        self.side = w

    def set_side(self, s):
        self.height = s
        self.width = s
        self.side = s

    def set_height(self, h):
        self.height = h
        self.width = h
        self.side = h
    def set_width(self, w):
        self.height = w
        self.width = w
        self.side = w

    def __str__(self) -> str:
        return "Square(side={})".format(self.side)