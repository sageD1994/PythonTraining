#!/usr/bin/env python3

class Rectangle():
    __w: float
    __h: float
    
    #constructor
    def __init__(self, width: float, height: float):
        if width<=0 or height<=0:
            raise ValueError('no negative parameters')
        self.__w = width
        self.__h = height
    #getter   
    @property
    def w(self):
        return self.__w
    @property
    def h(self):
        return self.__h
    #setter
    @w.setter
    def w(self, width: float):
        if width > 0:
            self.__w = width
        else:
            raise ValueError('no negative parameter')
    @h.setter
    def h(self, height: float):
        if height > 0:
            self.__h = height
        else:
            raise ValueError('no negative parameter')
    #instance method
    def area(self) -> float:
        return self.__w * self.h 
    def perimeter(self) -> float:
        return 2 * (self.__w + self.h)
    #static method
    @staticmethod 
    def sarea(width: float, height: float) -> float:
        return width*height
    #intern methods
    def ap(self):
        return { 'area': self.area(), 
                 'perimeter': self.perimeter()}
    #overload operator
    #eqal test
    def __eq__(self, other) -> bool:
        return (self.__w, self.__h) == (other.__w, other.__h)
    
r1 = Rectangle(12, 7.4)
r2 = Rectangle(8, 5)
for r in [r1, r2]:
    print('Breite:', r.w)
    print('Höhe:', r.h)
    print('Fläche:', r.area())
    print('Umfang:', r.perimeter())
    
#static methode
print(Rectangle.sarea(3,5))

#obj.instancemethode(param)
#Class.staticmethod(param)

#test setter and getter
print(r1.w)
r1.w=25
print(r1.w)

r3 =Rectangle(25,7.4)
print(r1==r3)