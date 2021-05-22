import copy
class Rectangle:
    def __init__(self,w,h):
        self.width = w
        self.height = h
    def __copy__(self):
        return Rectangle(self.width,self.height)
    def __str__(self):
        return 'This rectangle width is of {:.2f}'.format(self.width) + '\n' + 'This rectangle height is of {:.2f}'.format(self.height)
#new_rectangle = Rectangle(10,20)
#print(str(new_rectangle))