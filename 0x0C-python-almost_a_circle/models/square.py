#!/usr/bin/python3
"""square Class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """square Class"""
    def __init__(self, size, x=0, y=0, id=None):
        """intialize instance attributes"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, res):
        """size setter"""
        self.width = res
        self.height = res

    def __str__(self):
        """method so that it returns [square] (<id>) <x>/<y>"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.size = args[i]
                elif i == 2:
                    self.x = args[i]
                else:
                    self.y = args[i]
        else:
            if len(kwargs) > 0:
                keys = kwargs.keys()
                for i in keys:
                    if i == 'id':
                        self.id = kwargs['id']
                    elif i == 'size':
                        self.size = kwargs['size']
                    elif i == 'x':
                        self.x = kwargs['x']
                    elif i == 'y':
                        self.y = kwargs['y']

    def to_dictionary(self):
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
