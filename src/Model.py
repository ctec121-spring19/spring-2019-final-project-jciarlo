from View import View
'''
input: cell #'s from view
process: determines winner using Xs and Os within the grid list, determines empty cell using same list, determines where a character should be drawn and adds it to grid list, has function to reset grid
output: cell #s to display a character, win conditions
'''
class Model:
    
    def __init__(self, View):
        self.v = View
        self.grid = ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e']
    
    
    #list of ways to win Horizontal, Vertical, and Diagonal 
    def isWinner(self):
        # Horizontal Wins
        if self.grid[0] == self.grid[1] and self.grid[0] == self.grid[2] and self.grid[0] != 'e':
            return 1
        elif self.grid[3] == self.grid[4] and self.grid[3] == self.grid[5] and self.grid[3] != 'e':
            return 1
        elif self.grid[6] == self.grid[7] and self.grid[6] == self.grid[8] and self.grid[6] != 'e':
            return 1
        # Vertical Wins
        elif self.grid[0] == self.grid[3] and self.grid[0] == self.grid[6] and self.grid[0] != 'e':
            return 1
        elif self.grid[1] == self.grid[4] and self.grid[1] == self.grid[7] and self.grid[1] != 'e':
            return 1
        elif self.grid[2] == self.grid[5] and self.grid[2] == self.grid[8] and self.grid[2] != 'e':
            return 1
        # Diagonal Wins
        elif self.grid[0] == self.grid[4] and self.grid[0] == self.grid[8] and self.grid[0] != 'e':
            return 1
        elif self.grid[6] == self.grid[4] and self.grid[6] == self.grid[2] and self.grid[6] != 'e':
            return 1
        elif self.grid[0] != 'e' and self.grid[1] != 'e' and self.grid[2] != 'e' and self.grid[3] != 'e' and self.grid[4] != 'e' and self.grid[5] != 'e' and self.grid[6] != 'e' and self.grid[7] != 'e' and self.grid[8] != 'e':
            return 2
    
    def isValid(self, x):
        if self.grid[x] == 'e':
            return 1
    
    # recording location of X and telling view to draw it 
    def ControlX(self, click):
        if click == 0:
            if self.grid[0] != 'O':
                self.v.drawX(0)
                self.grid.pop(0)
                self.grid.insert(0, "X")
            else:
                self.v.Message(3, "Please choose a valid cell.")
        elif click == 1:
            if self.grid[1] != 'O':
                self.v.drawX(1)
                self.grid.pop(1)
                self.grid.insert(1, "X")
            else:
                self.v.Message(3, "Please choose a valid cell.")
        elif click == 2:
            if self.grid[2] != 'O':
                self.v.drawX(2)
                self.grid.pop(2)
                self.grid.insert(2, "X")
            else:
                self.v.Message(3, "Please choose a valid cell.")
        elif click == 3:
            if self.grid[3] != 'O':
                self.v.drawX(3)
                self.grid.pop(3)
                self.grid.insert(3, "X")
            else:
                self.v.Message(3, "Please choose a valid cell.")
        elif click == 4:
            if self.grid[4] != 'O':
                self.v.drawX(4)
                self.grid.pop(4)
                self.grid.insert(4, "X")
            else:
                self.v.Message(3, "Please choose a valid cell.")
        elif click == 5:
            if self.grid[5] != 'O':
                self.v.drawX(5)
                self.grid.pop(5)
                self.grid.insert(5, "X")
            else:
                self.v.Message(3, "Please choose a valid cell.")
        elif click == 6:
            if self.grid[0] != 'O':
                self.v.drawX(6)
                self.grid.pop(6)
                self.grid.insert(6, "X")
            else:
                self.v.Message(3, "Please choose a valid cell.")
        elif click == 7:
            if self.grid[7] != 'O':
                self.v.drawX(7)
                self.grid.pop(7)
                self.grid.insert(7, "X")
            else:
                self.v.Message(3, "Please choose a valid cell.")
        elif click == 8:
            if self.grid[8] != 'O':
                self.v.drawX(8)
                self.grid.pop(8)
                self.grid.insert(8, "X")
            else:
                self.v.Message(3, "Please choose a valid cell.")
        return click
    
    # recording location of O and telling view to draw it
    def ControlO(self, click):
        if click == 0:
            if self.grid[0] != 'X':
                self.v.drawO(0)
                self.grid.pop(0)
                self.grid.insert(0, "O")
        elif click == 1:
            if self.grid[1] != 'X':
                self.v.drawO(1)
                self.grid.pop(1)
                self.grid.insert(1, "O")
        elif click == 2:
            if self.grid[2] != 'X':
                self.v.drawO(2)
                self.grid.pop(2)
                self.grid.insert(2, "O")
        elif click == 3:
            if self.grid[3] != 'X':
                self.v.drawO(3)
                self.grid.pop(3)
                self.grid.insert(3, "O")
        elif click == 4:
            if self.grid[4] != 'X':
                self.v.drawO(4)
                self.grid.pop(4)
                self.grid.insert(4, "O")
        elif click == 5:
            if self.grid[5] != 'X':
                self.v.drawO(5)
                self.grid.pop(5)
                self.grid.insert(5, "O")
        elif click == 6:
            if self.grid[6] != 'X':
                self.v.drawO(6)
                self.grid.pop(6)
                self.grid.insert(6, "O")
        elif click == 7:
            if self.grid[7] != 'X':
                self.v.drawO(7)
                self.grid.pop(7)
                self.grid.insert(7, "O")
        elif click == 8:
            if self.grid[8] != 'X':
                self.v.drawO(8)
                self.grid.pop(8)
                self.grid.insert(8, "O")
        else:
            self.v.Message(3, "Please choose a valid cell.")
        return click
    
    # resets grid list for new game, but not the visual grid
    def resetGrid(self):
        for i in range(len(self.grid)):
            self.grid.pop(i)
            self.grid.insert(i, "e")

def ModelTest():

    ModelTest()