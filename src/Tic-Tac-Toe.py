from graphics import *
def View():

    win = GraphWin("Tic-Tac-Toe Grid", 1200, 800)
    win.setCoords(-1, -4, 11, 4)
# draw box
    Rectangle(Point(0,0), Point(3, 3)).draw(win)

# draw vertical lines
    Line(Point(1, 0), Point(1, 3)).draw(win)
    Line(Point(2, 0), Point(2, 3)).draw(win)

# draw horizontal lines

    Line(Point(0, 1), Point(3, 1)).draw(win)
    Line(Point(0, 2), Point(3, 2)).draw(win)
    
    p1mouse = win.getMouse()
    p1x = p1mouse.getX()
    p1y = p1mouse.getY()
    if int(p1x) == 0 and int(p1y) == 0:
        return cell0
    elif int(p1x) == 1 and int(p1y) == 0:
        return cell1
    elif int(p1x) == 2 and int(p1y) == 0:
        return cell2
    elif int(p1x) == 0 and int(p1y) == 1:
        return cell3
    elif int(p1x) == 1 and int(p1y) == 1:
        return cell4
    elif int(p1x) == 2 and int(p1y) == 1:
        return cell5
    elif int(p1x) == 0 and int(p1y) == 2:
        return cell6
    elif int(p1x) == 1 and int(p1y) == 2:
        return cell7
    elif int(p1x) == 2 and int(p1y) == 2:
        return cell8

    input()
    drawnObjects = []

View()