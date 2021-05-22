from Circle import *
from Rectangle import *
basic_circle = Circle(2.1)
new_circle = copy.copy(basic_circle)
basic_circle = Circle(2.4)
print(str(basic_circle) + "\n" + str(new_circle))
print("-----------")
basic_rectangle = Rectangle(10,20)
new_rectangle = copy.copy(basic_rectangle)
basic_rectangle = Rectangle(20,20)
print(str(basic_rectangle) + "\n" + str(new_rectangle))
