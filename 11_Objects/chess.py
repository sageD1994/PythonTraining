#!/usr/bin/env python3

#base class for figures
class Figure():
    col: int
    row: int
    #const
    def __init__(self, pos: str) -> None:
        if len(pos) != 2: raise ValueError('ungültige positpion')
        c = pos[0].lower()
        r = pos[1]
        if (not c in 'abcdefgh') or (not r in '12345678'):raise ValueError('ungültige positpion')
        self.col = 'abcdefgh'.find(c)
        self.row = '12345678'.find(r)
    #string for print
    def __str__(self) -> str:
        return Figure.position(self.col, self.row)
    #check if correct position
    @staticmethod
    def position(col: int, row: int) -> str:
        if row < 0 or row > 7 or col < 0 or col > 7:
            return ''
        else:
            return 'abcdefgh'[col] + '12345678'[row]     
        
#knight class
class Knight(Figure):
    def __init__(self, pos: str) -> None:
        super().__init__(pos)
    def __str__(self) -> str:
        return 'Knight@' + super().__str__()
    def findMoves(self):
        offsets = [(1,2), (2,1), (-1,2), (-2,1),
                   (1,-2), (2, -1), (-1,-2), (-2,-1)]
        positions = []
        for (coff, roff) in offsets:
            newpos = Figure.position(self.col + coff, self.row + roff)
            if newpos:
                positions += [newpos]
        return positions
    
#bishop class
class Bishop(Figure):
    def __init__(self, pos: str) -> None:
        super().__init__(pos)
    def __str__(self) -> str:
        return 'Bishop@' + super().__str__()
    def findMoves(self):
        positions = []
        for i in range(-7,8):
            if i == 0: continue
            newpos = Figure.position(self.col + i, self.row + i)
            if newpos: positions += [newpos]
            newpos = Figure.position(self.col + i, self.row - i)
            if newpos: positions += [newpos]    
        return positions
    
figures = [Knight('e5'), Bishop('B3'), Knight('h8')]  
for f in figures:
    print(f, f.findMoves())