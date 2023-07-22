class Rectangle:

  def __init__(self, width=0, height=0):
    self.width = width
    self.height = height

  def set_width(self, new_width):
    self.width = new_width

  def set_height(self, new_height):
    self.height = new_height

  def get_area(self):
    area = self.height * self.width
    return area

  def get_perimeter(self):
    perimeter = 2 * self.height + 2 * self.width
    return perimeter

  def get_diagonal(self):
    diagonal = (self.height**2 + self.width**2)**.5
    return diagonal

  def get_picture(self):
    picture = ""
    if self.height > 50 or self.width > 50:
      picture = "Too big for picture."
    else:
      for i in range(self.height):
        picture += "*" * self.width + "\n"
    return picture
  def get_amount_inside(self, other_shape):
    n_width = self.width // other_shape.width
    n_height = self.height // other_shape.height
    amount = n_height * n_width
    return amount

  def __str__(self):
    return "Rectangle(width=" + str(self.width) + ", " + "height=" + str(
      self.height) + ")"


class Square(Rectangle):

  def __init__(self, side):
    
    super().__init__(side, side)

  def set_side(self, side):
    
    self.set_width(side)
    self.set_height(side)

  def __str__(self):
    return "Square(side=" + str(self.width) + ")"
