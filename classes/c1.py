### Implement a rectangle class
# Implement a class named Rectangle to store the coordinates of a rectangle given the top-left corner (x1, y1) and the bottom-right corner (x2, y2).
# Implement the class constructor with the parameters (x1, y1, x2, y2) and store them in the class instance using the self keyword.

# class Rectangle:
#   def __init__(self, x1, y1, x2, y2):
#     if x1 < x2 and y1 > y2:
#       self.x1 = x1
#       self.y1 = y1
#       self.x2 = x2
#       self.y2 = y2
#     else:
#       print("Incorrect coordinates of the rectangle!")

  

# r = Rectangle(2, 7, 8, 4)

### c2: implement getter methods
# Implement the width() and height() methods which return, respectively, the width and height of a rectangle. The tests that follow will create two objects—instances of Rectangle to test the calculations.

class Rectangle:
  def __init__(self, x1, y1, x2, y2):
    if x1 < x2 and y1 > y2:
      self.x1 = x1
      self.y1 = y1
      self.x2 = x2
      self.y2 = y2
    else:
      print("Incorrect coordinates of the rectangle!")

  def width(self):
    return self.x2 - self.x1

  def height(self):
    return self.y1 - self.y2

r = Rectangle(2, 7, 8, 4)
print(r.width())
print(r.height())