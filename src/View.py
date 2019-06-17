from graphics import *
'''
input: a click from the user's mouse
process: creates the grid, converts coordinates of click to grid #'s, sets messages, determines whether yes or no is clicked
output: cell #'s, displayed messages, X or Os, true or false for question'''
class View:
    
    def __init__(self):
        self.win = GraphWin("Tic-Tac-Toe", 500, 600)
        self.items = []

        self.win.setCoords(-1, -2, 4, 4)
        # draw box
        Rectangle(Point(0,0), Point(3, 3)).draw(self.win).setFill("PaleTurquoise")
        self.win.setBackground("DarkOrange")

        # draw vertical lines
        Line(Point(1, 0), Point(1, 3)).draw(self.win).setWidth(3)
        Line(Point(2, 0), Point(2, 3)).draw(self.win).setWidth(3)

        # draw horizontal lines

        Line(Point(0, 1), Point(3, 1)).draw(self.win).setWidth(3)
        Line(Point(0, 2), Point(3, 2)).draw(self.win).setWidth(3)

        # create text objects
        self.one = Text(Point(1.5, 3.5), "").draw(self.win)
        self.one.setTextColor("Azure")
        self.one.setSize(18)

        self.two = Text(Point(1.5, 3.25), "").draw(self.win)
        self.two.setTextColor("Azure")
        self.two.setSize(18)

        self.three = Text(Point(1.5, -0.25), "").draw(self.win)
        self.three.setTextColor("Azure")
        self.three.setSize(18)


    # determines which cell is being clicked 
    def Click(self):
        p1mouse = self.win.getMouse()
        p1x = p1mouse.getX()
        p1y = p1mouse.getY()

        if int(p1x) == 0 and int(p1y) == 0:
            return 0
        elif int(p1x) == 1 and int(p1y) == 0:
            return 1
        elif int(p1x) == 2 and int(p1y) == 0:
            return 2
        elif int(p1x) == 0 and int(p1y) == 1:
            return 3
        elif int(p1x) == 1 and int(p1y) == 1:
            return 4
        elif int(p1x) == 2 and int(p1y) == 1:
            return 5
        elif int(p1x) == 0 and int(p1y) == 2:
            return 6
        elif int(p1x) == 1 and int(p1y) == 2:
            return 7
        elif int(p1x) == 2 and int(p1y) == 2:
            return 8
        else:
            return 9
    # shows a message
    def Message(self, num, sentence):
        # num is a posistional argument 1 being the highest and 7 being the lowest.
        if num == 1:
            self.one.setText(sentence)
        elif num == 2:
            self.two.setText(sentence)
        elif num == 3:
            self.three.setText(sentence)
   
    # tells where to draw X
    def drawX(self, where):
        if where == 0:
            self.items.append(Line(Point(0.1,0.1), Point(0.9,0.9)).draw(self.win))
            self.items.append(Line(Point(0.9,0.1), Point(0.1,0.9)).draw(self.win))
        elif where == 1:
            self.items.append(Line(Point(1.1,0.1), Point(1.9,0.9)).draw(self.win))
            self.items.append(Line(Point(1.9,0.1), Point(1.1,0.9)).draw(self.win))
        elif where == 2:
            self.items.append(Line(Point(2.1,0.1), Point(2.9,0.9)).draw(self.win))
            self.items.append(Line(Point(2.9,0.1), Point(2.1,0.9)).draw(self.win))
        elif where == 3:
            self.items.append(Line(Point(0.1,1.1), Point(0.9,1.9)).draw(self.win))
            self.items.append(Line(Point(0.9,1.1), Point(0.1,1.9)).draw(self.win))
        elif where == 4:
            self.items.append(Line(Point(1.1,1.1), Point(1.9,1.9)).draw(self.win))
            self.items.append(Line(Point(1.9,1.1), Point(1.1,1.9)).draw(self.win))
        elif where == 5:
            self.items.append(Line(Point(2.1,1.1), Point(2.9,1.9)).draw(self.win))
            self.items.append(Line(Point(2.9,1.1), Point(2.1,1.9)).draw(self.win))
        elif where == 6:
            self.items.append(Line(Point(0.1,2.1), Point(0.9,2.9)).draw(self.win))
            self.items.append(Line(Point(0.9,2.1), Point(0.1,2.9)).draw(self.win))
        elif where == 7:
            self.items.append(Line(Point(1.1,2.1), Point(1.9,2.9)).draw(self.win))
            self.items.append(Line(Point(1.9,2.1), Point(1.1,2.9)).draw(self.win))
        elif where == 8:
            self.items.append(Line(Point(2.1,2.1), Point(2.9,2.9)).draw(self.win))
            self.items.append(Line(Point(2.9,2.1), Point(2.1,2.9)).draw(self.win))
    
    # tells where to draw O
    def drawO(self, where):
        if where == 0:
            self.items.append(Circle(Point(0.5, 0.5), 0.45).draw(self.win))
        elif where == 1:
            self.items.append(Circle(Point(1.5, 0.5), 0.45).draw(self.win))
        elif where == 2:
            self.items.append(Circle(Point(2.5, 0.5), 0.45).draw(self.win))
        elif where == 3:
            self.items.append(Circle(Point(0.5, 1.5), 0.45).draw(self.win))
        elif where == 4:
            self.items.append(Circle(Point(1.5, 1.5), 0.45).draw(self.win))
        elif where == 5:
            self.items.append(Circle(Point(2.5, 1.5), 0.45).draw(self.win))
        elif where == 6:
            self.items.append(Circle(Point(0.5, 2.5), 0.45).draw(self.win))
        elif where == 7:
            self.items.append(Circle(Point(1.5, 2.5), 0.45).draw(self.win))
        elif where == 8:
            self.items.append(Circle(Point(2.5, 2.5), 0.45).draw(self.win))
    
    # yes or no buttons 
    def done(self):
        Rectangle(Point(0, -1), Point(1, -1.5)).draw(self.win).setFill("PaleTurquoise")
        Rectangle(Point(2, -1), Point(3, -1.5)).draw(self.win).setFill("PaleTurquoise")
        Text(Point(0.5, -1.25), "Yes").draw(self.win)
        Text(Point(2.5, -1.25), "No").draw(self.win)
        p1mouse = self.win.getMouse()
        p1x = p1mouse.getX()
        p1y = p1mouse.getY()
        
        if int(p1x) == 0 and int(p1y) == -1:
            return False
        elif int(p1x) == 2 and int(p1y) == -1:
            return True
  
    # resets visuals for game
    def reset(self):
        for i in range(len(self.items)):
            self.items[i].undraw()


def viewTest():
    v = View()
    #v.Grid()
    v.Message(1, "yo")
    v.Message(2, "aaahhh")
    v.done()
    print(v.done())
    input()


if __name__ == "__main__":
    viewTest()