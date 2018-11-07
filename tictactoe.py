import console

class tictactoe:
    
    playerturn = "X"
    playerturntracker = 0
    
    def __init__(self):
        
        self.row1 = ["*","*","*"]
        self.row2 = ["*","*","*"]
        self.row3 = ["*","*","*"]
    
    def showgame(self):
        print(self.row1)
        print(self.row2)
        print(self.row3)
    
    def player_move(self):
      self.rowinput = input("what number row will you pick? ")
      self.columninput = input("what number column will you pick? ")
     
    def place_move(self):
      if int(self.rowinput) == 1:
          self.row1[int(self.columninput) - 1] = self.playerturn
      
      if int(self.rowinput) == 2:
          self.row2[int(self.columninput) - 1] = self.playerturn
          
      if int(self.rowinput) == 3:
          self.row3[int(self.columninput) - 1] = self.playerturn
          
    def player_turn(self):
        self.playerturntracker += 1
        if self.playerturntracker % 2 == 0:
            self.playerturn = "O"
        else:
            self.playerturn = "X"
object1 = tictactoe()
object1.showgame()

while object1.playerturntracker < 100:
    object1.player_turn()
    object1.player_move()
    object1.place_move()
    console.clear()
    object1.showgame()
