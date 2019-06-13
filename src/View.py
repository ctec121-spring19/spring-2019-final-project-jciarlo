from graphics import *
class View:
    def __init__(self):
        self.win = GraphWin("Tic-Tac-Toe Grid", 1200, 800)
        self.said = []
        self.items = []

        self.win.setCoords(-1, -4, 11, 4)
        # draw box
        Rectangle(Point(0,0), Point(3, 3)).draw(self.win)

        # draw vertical lines
        Line(Point(1, 0), Point(1, 3)).draw(self.win)
        Line(Point(2, 0), Point(2, 3)).draw(self.win)

        # draw horizontal lines

        Line(Point(0, 1), Point(3, 1)).draw(self.win)
        Line(Point(0, 2), Point(3, 2)).draw(self.win)

        # create text objects
        self.one = Text(Point(6, 3), "").draw(self.win)
        self.two = Text(Point(6, 2.5), "").draw(self.win)

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

    def Message(self, num, sentence):
        # num is a posistional argument 1 being the highest and 7 being the lowest.
        if num == 1:
            self.one.setText(sentence)
        elif num == 2:
            self.two.setText(sentence)
    def eraseMessages(self):
        for i in range(len(self.said)):
                self.said[i].undraw()
    def drawX(self, where):
        if where == 0:
            self.items.append(Line(Point(0,0), Point(1,1)).draw(self.win))
            Line(Point(1,0), Point(0,1)).draw(self.win)
        elif where == 1:
            Line(Point(1,0), Point(2,1)).draw(self.win)
            Line(Point(2,0), Point(1,1)).draw(self.win)
        elif where == 2:
            Line(Point(2,0), Point(3,1)).draw(self.win)
            Line(Point(3,0), Point(2,1)).draw(self.win)
        elif where == 3:
            Line(Point(0,1), Point(1,2)).draw(self.win)
            Line(Point(1,1), Point(0,2)).draw(self.win)
        elif where == 4:
            Line(Point(1,1), Point(2,2)).draw(self.win)
            Line(Point(2,1), Point(1,2)).draw(self.win)
        elif where == 5:
            Line(Point(2,1), Point(3,2)).draw(self.win)
            Line(Point(3,1), Point(2,2)).draw(self.win)
        elif where == 6:
            Line(Point(0,2), Point(1,3)).draw(self.win)
            Line(Point(1,2), Point(0,3)).draw(self.win)
        elif where == 7:
            Line(Point(1,2), Point(2,3)).draw(self.win)
            Line(Point(2,2), Point(1,3)).draw(self.win)
        elif where == 8:
            Line(Point(2,2), Point(3,3)).draw(self.win)
            Line(Point(3,2), Point(2,3)).draw(self.win)
    def drawO(self, where):
        if where == 0:
            self.items.append(Circle(Point(0.5, 0.5), 0.5).draw(self.win))
        elif where == 1:
            Circle(Point(1.5, 0.5), 0.5).draw(self.win)
        elif where == 2:
            Circle(Point(2.5, 0.5), 0.5).draw(self.win)
        elif where == 3:
            Circle(Point(0.5, 1.5), 0.5).draw(self.win)
        elif where == 4:
            Circle(Point(1.5, 1.5), 0.5).draw(self.win)
        elif where == 5:
            Circle(Point(2.5, 1.5), 0.5).draw(self.win)
        elif where == 6:
            Circle(Point(0.5, 2.5), 0.5).draw(self.win)
        elif where == 7:
            Circle(Point(1.5, 2.5), 0.5).draw(self.win)
        elif where == 8:
            Circle(Point(2.5, 2.5), 0.5).draw(self.win)

def viewTest():
    v = View()
    #v.Grid()
    v.Message(1, "yo")
    v.Message(2, "aaahhh")
    input()
    v.Message(1, "")
    v.Message(2, "")
    input()
if __name__ == "__main__":
    viewTest()