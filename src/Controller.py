from View import View
from Model import Model
class Controller:
    def __init__(self):
        self.v = View
        self.m = Model
    def playAGame(self):
        while not winner :

            if playerOneTurn :
                self.v.Message(1, "Player one's turn.")
                if self.m.Empty(self.v.Click()) == 1:
                    self.m.ControlX()
                    print(self.m.Empty(self.v.Click()))
                    if self.m.isWinner() is 1:
                        self.v.Message(1, "You Win!")
                    elif self.m.isWinner() is 2:
                        self.v.Message(1, "Draw!")
                else:
                    self.v.Message(1, "Illegal Move!")
            else :
                self.v.Message(1, "Player two's turn.")
                if self.m.Empty(self.v.Click()) == 1:
                    self.m.ControlO()
                    print(self.m.Empty(self.v.Click()))
                    if self.m.isWinner() is 1:
                        self.v.Message(1, "You Win!")
                    elif self.m.isWinner() is 2:
                        self.v.Message(1, "Draw!")
                else:
                    self.v.Message(1, "Illegal Move!")

            playerOneTurn = not playerOneTurn
def ControllerTest():
    c = Controller()
    c.playAGame()
ControllerTest()