from View import *
from Model import *
class Controller:
    def __init__(self):
        self.v = View()
        self.m = Model(self.v)
    def playAGame(self):
        winner = False
        playerOneTurn = True
        while winner is False:
            if playerOneTurn :
                self.v.Message(1, "Player one's turn!")
                self.v.Message(2, "")
                self.v.Message(3, "")
                while True:
                    cellnum = self.v.Click()
                    if cellnum >= 0 and cellnum <= 8:
                        ans = self.m.isValid(cellnum)
                        if ans == 1:
                            self.m.ControlX(cellnum)
                            break
                        else:
                            self.v.Message(1, "You can't steal player two's cell!")
                            self.v.Message(2, "ಠ_ಠ")
                    else:
                        self.v.Message(1, "Please click a cell inside the grid.")
                        self.v.Message(2, "ಠ_ಠ")
                if self.m.isWinner() is 1:
                    self.v.Message(1, "Congratulations player one, you win!")
                    self.v.Message(2, "\( ﾟ◡ﾟ)/")
                    break
                elif self.m.isWinner() is 2:
                    self.v.Message(1, "Draw!")
                    self.v.Message(2, "(ﾟーﾟ)")
                    break
            else :
                self.v.Message(1, "Player two's turn!")
                self.v.Message(2, "")
                self.v.Message(3, "")
                while True:
                    cellnum = self.v.Click()
                    if cellnum >= 0 and cellnum <= 8:
                        ans = self.m.isValid(cellnum)
                        if ans == 1:
                            self.m.ControlO(cellnum)
                            break
                        else:
                            self.v.Message(1, "You can't steal player two's cell!")
                            self.v.Message(2, "ಠ_ಠ")
                    else:
                        self.v.Message(1, "Please click a cell inside the grid.")
                        self.v.Message(2, "ಠ_ಠ")
                if self.m.isWinner() is 1:
                    self.v.Message(1, "Congratulations player two, you win!")
                    self.v.Message(2, "\( ﾟ◡ﾟ)/")
                    break
                elif self.m.isWinner() is 2:
                    self.v.Message(1, "Draw!")
                    self.v.Message(2, "(ﾟーﾟ)")
                    break
            playerOneTurn = not playerOneTurn
    def play(self):
        while True:
            self.v.Message(3, "Would you like to play (again)?")
            done = self.v.done()
            if done == True or done == False:
                if done is False:
                    self.v.reset()
                    self.m.resetGrid()
                    self.playAGame()
                else:
                    break
            else:
                self.v.Message(2, "You must select yes or no!")
def ControllerTest():
    c = Controller()
    c.play()
ControllerTest()