import copy
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def __copy__(self):
        return Circle(self.radius)
    def __str__(self):
        return 'This is a circle with radius of {:.2f}'.format(self.radius)
#new_circle = Circle(2.1)
#print(str(new_circle))
#cir = copy.copy(new_circle)
#new_circle = Circle(2.4)
#print(cir,new_circle)